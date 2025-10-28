flowchart TD
  %% States
  O[OPTIMIZE\nObjective: minimize Φ_info\nτ: allocate to productive adaptation]
  R[REINFLATE\nObjective: maximize J_witness (dynamic weights)\nπ_verify: oversample failing dims\nτ: reduce for worst dim]
  M[MINIMAL_INFO\nObjective: minimize J_cost = w_info·I(C)+w_verify·Cost(VERIFY,π)\nτ: shrink as needed]
  L[LOCKDOWN\nTrigger: Z_t ≥ Z_crit\nObjective: min W1(p_t, p_ref)\nActions: freeze metrics/α, K_i→K_min, τ→0]
  H[HANDSHAKE (new agent)\nα=0, τ=0, K→K_min\nLocal PASS for M_H → OPTIMIZE]
  META[[META-OPTIMIZE (𝓡_meta)\nTunes {κ⃗, λ, μ}\nObjective: w_iso·∑W1(...) − (1−w_iso)·E||∇_θ C_Σ||²]]

  %% Transitions (with hysteresis)
  O -->|DEGENERATE* & Z_t<Z_crit| R
  O -->|FAIL persists > N & Z_t<Z_crit| M
  O -->|Z_t ≥ Z_crit| L

  R -->|PASS & witnesses ≥ floors+ε_H for M_R| O
  R -->|Z_t ≥ Z_crit| L

  M -->|PASS for M_M & J_cost non-increasing| O
  M -->|Z_t ≥ Z_crit| L

  L -->|Z_t < Z_crit for M_Z| O

  H -->|Local PASS for M_H| O

  %% Meta-controller runs across states
  META --- O
  META --- R
  META --- M
  META --- L
  META --- H

  %% Notes
  classDef s fill:#f7f7ff,stroke:#666,stroke-width:1px;
  class O,R,M,L,H s
