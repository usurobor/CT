# TSC v1.2.9 — Spec Compliance Checklist

## Foundations
- [ ] A1–A4 not modified; equal-weight geometric mean for C_Σ preserved.
- [ ] Φ_info implemented with fixed Θ=0.80; CI lower bound used for PASS.

## Verification Protocol
- [ ] π_verify(state) implemented:
  - [ ] OPTIMIZE uses importance/adversarial sampling.
  - [ ] REINFLATE oversamples failing dimensions.
  - [ ] LOCKDOWN/HANDSHAKE use random sampling vs p_ref.
- [ ] VERIFY_TSC_PLUS computes (H_c, V_c, D_c, C_Σ), witnesses, Z_t, CI, δ_C.
- [ ] Verdicts: PASS / FAIL / FAIL/DEGENERATE / FAIL/DEGENERATE_D.

## State Machine & Hysteresis
- [ ] States: OPTIMIZE, REINFLATE, MINIMAL_INFO, LOCKDOWN, HANDSHAKE; plus META-OPTIMIZE.
- [ ] Transitions match §5.1 with hysteresis (ε_H, M_R, M_M, M_Z, M_H).
- [ ] LOCKDOWN is triggered solely by Z_t ≥ Z_crit (no threshold lowering).

## Managed Resources & Actions
- [ ] J_cost = w_info·I(C) + w_verify·Cost(VERIFY,π) used in MINIMAL_INFO.
- [ ] τ-budget enforced per §6.2 across all states; τ→0 in LOCKDOWN/HANDSHAKE.
- [ ] “Simplify” levers implemented: κ increase, regularization, pruning, π_verify simplification.

## Distributed Protocol
- [ ] Trust α_i(t) ∝ exp(–k·σ_i²(t)), normalized.
- [ ] Per-agent cadence K_i follows K_base·α_i·(1 – ρ_C·Δδ_C,i), clipped to [K_min, K_max].
- [ ] HANDSHAKE: new agents have α=0, τ=0, K→K_min until M_H local PASS.

## Observability
- [ ] Log schema adheres to OBSERVABILITY_SCHEMA.yaml.
- [ ] All required fields recorded each verification step.
- [ ] p_ref hash and π_verify parameters logged.

## Defaults (may be tuned but must be declared)
- [ ] Θ=0.80; β=0.5; w_iso=0.3; ε=1e-4.
- [ ] ε_H=0.05; M_R=3; M_M=5; Z_crit=0.95; M_Z=3; M_H=10.
- [ ] K_base=64; K_min=4; K_max=128; ρ_C=0.2; τ_max=0.10.
