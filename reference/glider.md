# Reference Example: Conway’s Life Glider
*Status: Informative (Recommended Harness)*

This document provides a worked example demonstrating high triadic coherence.

---

## 1. Articulation

- **H (pattern):** 5‑cell motif class, identified up to translation/rotation.  
- **V (relation):** neighbor relation; translational symmetry group `G = Z²`.  
- **D (process):** Life update rule (B3/S23); one step `U_D`.

---

## 2. Witnesses & Registrations

- **w_H:** extract motif class ID from grid snapshots; `μ_H` = class code.  
- **w_V:** register symmetry signature and neighbor constraints; `μ_V` = `(G, neighborhood vector)` descriptor.  
- **w_D:** apply `U_D`; track orbit length and displacement vector.

Independence: `w_*` run on separate pipelines with distinct preprocessing seeds.

---

## 3. Ensemble Checks

### 3.1 Commutation
- Run: `μ_H ∘ U_D` vs `U_D ∘ μ_H` (with `μ_V` contextualization).  
- Expectation: equivalence up to known displacement; `E_comm ≈ 1`.

### 3.2 Conservation
- V‑invariants: cell count modulo translation; glider’s displacement per 4 steps.  
- Check: invariants visible in H and preserved by D; `E_cons ≈ 1`.

### 3.3 Symmetry
- `G = Z²` translations. Verify D‑equivariance: U_D(g·x) = g·U_D(x),  ∀g ∈ G

- Score: near 1 across runs (violations ≈ 0).

### 3.4 Scale
- Coarse‑grain: group 2×2 blocks; Fine‑grain: sub‑cell sampling (super‑resolution sim).  
- `C_Σ^(s)` stable within τ = 0.02; `E_scale ≈ 1`.

---

## 4. Scores (Illustrative)

- `H_c = 0.995`  
- `V_c = 0.996`  
- `D_c = 0.997`  
- `C_Σ = (0.995·0.996·0.997)^(1/3) ≈ 0.996`

Permutation test (random role relabeling): `ΔC_Σ < 1e-4`.

---

## 5. Notes

- This harness can be used as a **positive control** to validate any TSC implementation.  
- For a **negative control**, use randomized initial grids (soup); expect low invariants and low `C_Σ`.
