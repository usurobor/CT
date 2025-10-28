"""
reference/tsc_controller_fp.py
Functional-core, effect-interpreter controller for TSC Operational Addendum v1.2.9
(Compatible with Core ≥ v1.1.19)

Principles
- Pure domain + pure transitions (no hidden state changes).
- Effects are data (ADTs), interpreted by a tiny side-effect layer.
- Names align with the spec: Metrics, WitnessFloors, OOD, Θ, Z_crit, etc.
"""

from __future__ import annotations
from dataclasses import dataclass, replace
from enum import Enum, auto
from typing import Any, Callable, Iterable, Mapping, Optional, Tuple, Union, Literal

# ----------------------------- Domain ---------------------------------------

Dim = Literal["H","V","D"]

class State(Enum):
    OPTIMIZE = auto()
    REINFLATE = auto()
    MINIMAL_INFO = auto()
    LOCKDOWN = auto()
    HANDSHAKE = auto()

class Verdict(Enum):
    PASS = auto()
    FAIL = auto()
    FAIL_DEGENERATE = auto()
    FAIL_DEGENERATE_D = auto()

@dataclass(frozen=True)
class Metrics:
    H_c: float; V_c: float; D_c: float
    C_sigma: float
    C_sigma_CI: Tuple[float, float]  # (lo, hi)

@dataclass(frozen=True)
class WitnessFloors:
    nu_min: float; H_min: float; L_min: float
    nu_min_D: float; H_min_D: float

@dataclass(frozen=True)
class WitnessStatus:
    H_variance: float = 0.0
    H_entropy: float  = 0.0
    H_lipschitz: float = 0.0
    D_entropy: float  = 0.0
    D_variance: float = 0.0
    def hv_fails(self, f: WitnessFloors) -> bool:
        return (self.H_variance < f.nu_min) or (self.H_entropy < f.H_min) or (self.H_lipschitz < f.L_min)
    def d_fails(self, f: WitnessFloors) -> bool:
        return (self.D_entropy < f.H_min_D) or (self.D_variance < f.nu_min_D)

@dataclass(frozen=True)
class OODStatus:
    Z_t: float; Z_crit: float
    p_ref_hash: Optional[str] = None

@dataclass(frozen=True)
class TauBudget:
    tau_max: float
    H: float = 0.0; V: float = 0.0; D: float = 0.0
    def shrink_worst(self, factor: float = 0.5) -> TauBudget:
        trip = {"H": self.H, "V": self.V, "D": self.D}
        worst = max(trip, key=trip.get)
        trip[worst] = max(0.0, trip[worst] * factor)
        return TauBudget(self.tau_max, trip["H"], trip["V"], trip["D"])

@dataclass(frozen=True)
class PolicyConfig:
    Theta: float = 0.80
    delta: float = 0.05
    Z_crit: float = 0.95
    M_Z: int = 3
    epsilon_H: float = 0.05
    M_R: int = 3
    M_M: int = 5
    M_H: int = 10

@dataclass(frozen=True)
class VerifyPolicy:
    name: str = "default"
    params: Mapping[str, Any] = None

# ----------------------------- Effects (ADTs) --------------------------------

@dataclass(frozen=True)
class VerifyPolicy:
    name: str = "default"
    params: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class FreezeMetricsAndTrust:
    pass

@dataclass(frozen=True)
class SetAllKiToMin:
    pass

@dataclass(frozen=True)
class OversampleFailingDimensions:
    policy: VerifyPolicy

@dataclass(frozen=True)
class ReduceTauForWorstDimension:
    witnesses: "WitnessStatus"  # quotes ok since we imported annotations from __future__

@dataclass(frozen=True)
class RecenterAndRetuneLambdaMu:
    pass

@dataclass(frozen=True)
class ReallocateTauForProductiveAdaptation:
    pass

@dataclass(frozen=True)
class ApplySimplifyActions:
    # e.g., "witness_health" or "J_cost"
    target: str

@dataclass(frozen=True)
class ResetCounters:
    names: Tuple[str, ...] = ()

Effect = Union[
    FreezeMetricsAndTrust,
    SetAllKiToMin,
    OversampleFailingDimensions,
    ReduceTauForWorstDimension,
    RecenterAndRetuneLambdaMu,
    ReallocateTauForProductiveAdaptation,
    ApplySimplifyActions,
    ResetCounters,
]

# ----------------------------- Pure Verifier ---------------------------------
Index = Any
SampleIndexSet   = Callable[[State, VerifyPolicy], Iterable[Index]]
ComputeMetrics   = Callable[[Iterable[Index]], Metrics]
ComputeWitnesses = Callable[[Iterable[Index]], WitnessStatus]
ComputeOOD       = Callable[[Iterable[Index]], OODStatus]

@dataclass(frozen=True)
class VerifyEnv:
    sample_index_set: SampleIndexSet
    compute_metrics:   ComputeMetrics
    compute_witnesses: ComputeWitnesses
    compute_ood:       ComputeOOD

def verify_tsc_plus(
    *, state: State, policy: VerifyPolicy, floors: WitnessFloors, cfg: PolicyConfig, env: VerifyEnv
) -> Tuple[Verdict, Metrics, WitnessStatus, OODStatus, Tuple[Index, ...]]:
    I = tuple(env.sample_index_set(state, policy))
    M = env.compute_metrics(I); W = env.compute_witnesses(I); O = env.compute_ood(I)
    lo, _ = M.C_sigma_CI
    if O.Z_t >= cfg.Z_crit: return Verdict.FAIL, M, W, O, I
    if W.hv_fails(floors):  return Verdict.FAIL_DEGENERATE, M, W, O, I
    if W.d_fails(floors):   return Verdict.FAIL_DEGENERATE_D, M, W, O, I
    return (Verdict.PASS if lo >= cfg.Theta else Verdict.FAIL, M, W, O, I)

# ----------------------------- Pure Transition -------------------------------
@dataclass(frozen=True)
class Counters:
    ood_clear: int = 0
    drift: int = 0
    handshake_passes: int = 0

@dataclass(frozen=True)
class ControllerState:
    state: State = State.OPTIMIZE
    tau: TauBudget = TauBudget(0.10)
    counters: Counters = Counters()

def transition(
    *, floors: WitnessFloors, cfg: PolicyConfig, policy: VerifyPolicy,
    ctrl: ControllerState, verdict: Verdict, witnesses: WitnessStatus, ood: OODStatus
) -> Tuple[ControllerState, Tuple[Effect, ...]]:
    s, c, tau = ctrl.state, ctrl.counters, ctrl.tau
    eff: list[Effect] = []

    # LOCKDOWN entry/exit
    if s != State.LOCKDOWN and ood.Z_t >= cfg.Z_crit:
        eff += [FreezeMetricsAndTrust(), SetAllKiToMin()]
        return ControllerState(State.LOCKDOWN, TauBudget(tau.tau_max,0,0,0), replace(c, ood_clear=0)), tuple(eff)
    if s == State.LOCKDOWN:
        if ood.Z_t < cfg.Z_crit:
            n = replace(c, ood_clear=c.ood_clear+1)
            if n.ood_clear >= cfg.M_Z:
                eff += [ResetCounters(("lockdown","drift"))]
                return ControllerState(State.OPTIMIZE, tau, replace(n, ood_clear=0, drift=0)), tuple(eff)
            return replace(ctrl, counters=n), tuple(eff)
        return replace(ctrl, counters=replace(c, ood_clear=0)), tuple(eff)

    # HANDSHAKE
    if s == State.HANDSHAKE:
        if verdict == Verdict.PASS:
            n = replace(c, handshake_passes=c.handshake_passes+1)
            return (ControllerState(State.OPTIMIZE, tau, replace(n, handshake_passes=0))
                    if n.handshake_passes >= cfg.M_H else replace(ctrl, counters=n)), tuple(eff)
        return replace(ctrl, counters=replace(c, handshake_passes=0)), tuple(eff)

    # DEGENERATE → REINFLATE
    if verdict in (Verdict.FAIL_DEGENERATE, Verdict.FAIL_DEGENERATE_D):
        eff += [OversampleFailingDimensions(policy), ReduceTauForWorstDimension(witnesses),
                ApplySimplifyActions("witness_health")]
        return replace(ctrl, state=State.REINFLATE), tuple(eff)

    # DRIFT FAIL
    if verdict == Verdict.FAIL:
        if s != State.MINIMAL_INFO:
            n = replace(c, drift=c.drift+1)
            if n.drift > cfg.M_M:
                eff += [ApplySimplifyActions("J_cost")]
                return ControllerState(State.MINIMAL_INFO, tau.shrink_worst(), n), tuple(eff)
            eff += [RecenterAndRetuneLambdaMu(), ReallocateTauForProductiveAdaptation()]
            return replace(ctrl, counters=n), tuple(eff)
        # already in MINIMAL_INFO; exit decided by interpreter via policy checks
        return ctrl, tuple(eff)

    # PASS → reset minimal counters, stay/return to OPTIMIZE
    eff += [ResetCounters(("drift","handshake"))]
    return ControllerState(State.OPTIMIZE, tau, replace(c, drift=0, handshake_passes=0)), tuple(eff)

# ----------------------------- Interpreter -----------------------------------
class Hooks:
    """Implement these in your runtime. This default prints nothing and mutates nothing."""
    def freeze_metrics_and_trust(self) -> None: pass
    def set_all_Ki_to_min(self) -> None: pass
    def oversample_failing_dimensions(self, policy: VerifyPolicy) -> None: pass
    def reduce_tau_for_worst_dimension(self, tau: TauBudget, witnesses: WitnessStatus) -> TauBudget: return tau
    def recenter_and_retune_lambda_mu(self) -> None: pass
    def reallocate_tau_for_productive_adaptation(self, tau: TauBudget) -> TauBudget: return tau
    def apply_simplify_actions(self, target: str) -> None: pass
    def reset_counters(self, names: Tuple[str,...]) -> None: pass
    def witnesses_above_margins_for(self, required_steps: int, epsilon_H: float) -> bool: return False
    def pass_M_M_with_non_increasing_J_cost(self, required_steps: int) -> bool: return False

def interpret(effects: Iterable[Effect], *, hooks: Hooks, tau: TauBudget, witnesses: WitnessStatus) -> TauBudget:
    for e in effects:
        if   isinstance(e, FreezeMetricsAndTrust): hooks.freeze_metrics_and_trust()
        elif isinstance(e, SetAllKiToMin): hooks.set_all_Ki_to_min()
        elif isinstance(e, OversampleFailingDimensions): hooks.oversample_failing_dimensions(e.policy)
        elif isinstance(e, ReduceTauForWorstDimension): tau = hooks.reduce_tau_for_worst_dimension(tau, e.witnesses)
        elif isinstance(e, RecenterAndRetuneLambdaMu): hooks.recenter_and_retune_lambda_mu()
        elif isinstance(e, ReallocateTauForProductiveAdaptation): tau = hooks.reallocate_tau_for_productive_adaptation(tau)
        elif isinstance(e, ApplySimplifyActions): hooks.apply_simplify_actions(e.target)
        elif isinstance(e, ResetCounters): hooks.reset_counters(e.names)
    return tau

# ----------------------------- One-step runner -------------------------------
def step(
    *, ctrl: ControllerState, floors: WitnessFloors, cfg: PolicyConfig,
    policy: VerifyPolicy, env: VerifyEnv, hooks: Hooks
) -> ControllerState:
    verdict, M, W, O, I = verify_tsc_plus(state=ctrl.state, policy=policy, floors=floors, cfg=cfg, env=env)
    next_ctrl, effs = transition(floors=floors, cfg=cfg, policy=policy, ctrl=ctrl, verdict=verdict, witnesses=W, ood=O)
    new_tau = interpret(effects=effs, hooks=hooks, tau=next_ctrl.tau, witnesses=W)
    # Optional: use hooks.witnesses_above_margins_for / pass_M_M_with_non_increasing_J_cost to refine exits
    return replace(next_ctrl, tau=new_tau)

# ----------------------------- Tiny self-test --------------------------------
if __name__ == "__main__":
    # Minimal fake environment (pure)
    def sample_index_set(state: State, policy: VerifyPolicy): return range(32)
    def compute_metrics(I): return Metrics(0.91,0.90,0.92,0.91,(0.86,0.95))
    def compute_witnesses(I): return WitnessStatus(0.02,0.25,0.06,0.22,0.015)
    def compute_ood(I): return OODStatus(0.10,0.95)
    env = VerifyEnv(sample_index_set, compute_metrics, compute_witnesses, compute_ood)

    # Floors, policy, config
    floors = WitnessFloors(1e-3, 0.1, 1e-3, 1e-4, 0.05)
    policy = VerifyPolicy()
    cfg = PolicyConfig()

    # Hooks (no-op)
    hooks = Hooks()

    # Run a few steps
    ctrl = ControllerState()
    for i in range(3):
        ctrl = step(ctrl=ctrl, floors=floors, cfg=cfg, policy=policy, env=env, hooks=hooks)
        print(f"step={i} state={ctrl.state.name} τ=({ctrl.tau.H:.3f},{ctrl.tau.V:.3f},{ctrl.tau.D:.3f})")
