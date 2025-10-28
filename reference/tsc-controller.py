from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Tuple, Optional

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

@dataclass
class Metrics:
    H_c: float; V_c: float; D_c: float
    C_sigma: float; C_sigma_CI: Tuple[float, float]

@dataclass
class WitnessFloors:
    nu_min: float; H_min: float; nu_min_D: float; H_min_D: float
    L_min: float  # Lipschitz floor

@dataclass
class WitnessStatus:
    H_variance: float; H_entropy: float; H_lipschitz: float
    D_entropy: float; D_variance: float

@dataclass
class OODStatus:
    Z_t: float; Z_crit: float; p_ref_hash: Optional[str] = None

@dataclass
class TauBudget:
    tau_max: float
    tau_alloc: Dict[str, float]  # {"H":..., "V":..., "D":...}

@dataclass
class VerifyPolicy:
    name: str
    params: Dict

THETA = 0.80

def verify_tsc_plus(state: State,
                    sampler: VerifyPolicy,
                    floors: WitnessFloors,
                    compute_metrics,      # callable -> Metrics
                    compute_witnesses,    # callable -> WitnessStatus
                    compute_ood           # callable -> OODStatus
                   ) -> Tuple[Verdict, Metrics, WitnessStatus, OODStatus]:
    # 1) sample I ~ π_verify(state)
    # 2) compute metrics/witnesses/ood
    M = compute_metrics()
    W = compute_witnesses()
    O = compute_ood()

    lo, hi = M.C_sigma_CI
    passes_ci = (lo >= THETA)

    # witness checks
    hv_fail = (W.H_variance < floors.nu_min or
               W.H_entropy  < floors.H_min or
               W.H_lipschitz < floors.L_min)
    d_fail = (W.D_entropy < floors.H_min_D or
              W.D_variance < floors.nu_min_D)

    if O.Z_t >= O.Z_crit:
        return (Verdict.FAIL, M, W, O)  # LOCKDOWN trigger handled in repair

    if hv_fail:
        return (Verdict.FAIL_DEGENERATE, M, W, O)
    if d_fail:
        return (Verdict.FAIL_DEGENERATE_D, M, W, O)
    if passes_ci:
        return (Verdict.PASS, M, W, O)
    return (Verdict.FAIL, M, W, O)

def coherence_repair_plus(state: State,
                          verdict: Verdict,
                          metrics: Metrics,
                          witnesses: WitnessStatus,
                          ood: OODStatus,
                          tau: TauBudget,
                          policy: VerifyPolicy,
                          params: Dict) -> State:
    # params expected: ε_H, M_R, M_M, M_Z, N, J_cost_trend, witness_margins, counters, etc.
    if ood.Z_t >= ood.Z_crit:
        # LOCKDOWN actions
        freeze_metrics_and_trust()
        set_all_Ki_to_min()
        tau.tau_alloc = {"H":0.0, "V":0.0, "D":0.0}
        params["lockdown_counter"] = params.get("lockdown_counter", 0) + 1
        if params["lockdown_counter"] >= params.get("M_Z", 3) and ood.Z_t < ood.Z_crit:
            params["lockdown_counter"] = 0
            return State.OPTIMIZE
        return State.LOCKDOWN

    if state == State.HANDSHAKE:
        # local verify loop; α=0; τ=0; K→K_min
        if verdict == Verdict.PASS:
            params["handshake_passes"] = params.get("handshake_passes", 0) + 1
            if params["handshake_passes"] >= params.get("M_H", 10):
                return State.OPTIMIZE
        else:
            params["handshake_passes"] = 0
        return State.HANDSHAKE

    if verdict == Verdict.FAIL_DEGENERATE or verdict == Verdict.FAIL_DEGENERATE_D:
        # enter/continue REINFLATE
        oversample_failing_dimensions(policy)
        reduce_tau_for_worst_dimension(tau, witnesses)
        apply_simplify_actions(target="witness_health")
        if witnesses_above_margins_for(params.get("M_R",3), params.get("ε_H",0.05)):
            return State.OPTIMIZE
        return State.REINFLATE

    if verdict == Verdict.FAIL:
        # drift: OPTIMIZE repair or escalate to MINIMAL_INFO if persists
        params["drift_counter"] = params.get("drift_counter", 0) + 1
        if params["drift_counter"] > params.get("N",5):
            apply_simplify_actions(target="J_cost")
            shrink_tau(tau)
            if pass_M_M_with_non_increasing_J_cost(params):
                params["drift_counter"] = 0
                return State.OPTIMIZE
            return State.MINIMAL_INFO
        recenter_and_retune_lambda_mu()
        reallocate_tau_for_productive_adaptation(tau)
        return State.OPTIMIZE

    if verdict == Verdict.PASS:
        reset_counters(params, keys=["drift_counter","handshake_passes","lockdown_counter"])
        return State.OPTIMIZE

    return state
