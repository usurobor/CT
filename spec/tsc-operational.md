# Triadic Self‑Coherence (TSC) — Operational
**Version:** v2.0.0  
**Dependency:** This document depends only on the definitions in **TSC — Core** (aspects H/V/D, contexts Ω, articulations A, summaries S, alignments σ, coherence predicate Coh, metrics H_c/V_c/D_c, aggregate C_Σ). It introduces no additional ontology.

---

## 0 · Purpose and Position in the Stack

**Purpose.** The Operational layer is the **policy and procedure** that turns the Core’s measurement calculus into a **repeatable verification process** with **verdicts**, **witnesses**, and **governance**. It answers:

- *What to run* (protocol),  
- *With which parameters* (policy),  
- *When to accept or reject* (verdict rules),  
- *How to remain stable and reproducible over time* (witnesses, logging, controller).

**What it adds (and only this):**
1. A **verification protocol** over the Core’s constructs.  
2. **Parameter registry** and recommended **default budgets**.  
3. **Witnesses** guarding against degenerate or ill‑posed comparisons.  
4. A minimal **controller** that adapts solver ensembles and budgets.  
5. **Reproducibility and provenance** requirements.

---

## 1 · Assumed Core Objects (for reference)

From the Core we use, without redefining:
- Aspects \( \{H,V,D\} \), contexts \( \Omega_X \), articulations \( O_X=A_X(\equiv) \).
- Summaries \( S_X = (d_X, p_X, H_X, \mathcal{I}_X) \).
- Alignment ensembles \( \mathcal{A}_{XY} \) and pairwise \( \overline{\mathrm{Coh}}_{XY} \) with ensemble variance.
- Metrics \( H_c, V_c, D_c \) and aggregate \( C_\Sigma=(H_c V_c D_c)^{1/3} \).

---

## 2 · Parameter Registry (Policy)

All parameters MUST be fixed **before** observation and logged with the verdict.

### 2.1 Coherence and Aggregation
- \( \alpha \in [0,1] \) — geometric vs. distributional weighting (default **0.7**).
- \( \lambda > 0 \) — sensitivity of Coh to discrepancy Δ (default **4.0**).
- \( \Theta \in (0,1] \) — pass threshold on \( C_\Sigma \) (default **0.80**).

### 2.2 Stability and Witness Floors
- **Ensemble variance floor** on each pair:  
  \( \mathrm{Var}[\mathrm{Coh}^{(\sigma)}_{XY}] \le \texttt{var\_floor} \) (default **2×10⁻²**).
- **Lipschitz‑slope guard** (95th‑percentile):  
  \( \texttt{Lipschitz95} \le \texttt{L\_max} \) (default **20**).
- **Entropy/variance floors** per aspect to avoid collapsed summaries:  
  `entropy_floor_H`, `entropy_floor_V`, `entropy_floor_D` (defaults domain‑specific; record explicitly).
- **Minimum sample size** per aspect: `n_min` (default **32** observations).

### 2.3 Alignment Ensemble Policies (State‑dependent)
A family \( \mathcal{A}_{XY} \) of admissible aligners is declared a priori; policy picks subsets per controller state (§5).

Recommended presets:
- **OPTIMIZE**: tight entropic regularization, diverse priors.  
- **REINFLATE**: looser regularization, robust costs (e.g., Huber), expanded locality priors.  
- **MINIMAL_INFO**: centroid pre‑clustering ≤ 128; coarse regularization.  
- **LOCKDOWN**: reuse last high‑fidelity alignments; compute lower‑bound Coh only.  
- **HANDSHAKE**: small orthogonal ensembles to re‑establish stability.

> Exact numerical settings are implementation choices; record them with the run.

---

## 3 · Verification Protocol (Normative)

**Inputs.** \( \Omega_H,\Omega_V,\Omega_D \); \( A_H,A_V,A_D \); alignment ensembles \( \mathcal{A}_{HV},\mathcal{A}_{VD},\mathcal{A}_{DH} \); parameters from §2.

**Outputs.** Verdict ∈ {PASS, FAIL, FAIL_DEGENERATE}, metrics \( (H_c,V_c,D_c,C_\Sigma) \), witnesses, and a provenance bundle.

**Steps.**

1. **Articulate**  
   \( O_X \leftarrow A_X(\equiv) \) for \( X\in\{H,V,D\} \).  
   Assert \( |O_X| \ge n_{\min} \) (witness).

2. **Summarize**  
   \( S_X \leftarrow \mathrm{Summary}(O_X) \).  
   Check aspect entropy/variance floors (witness).

3. **Align (ensemble)**  
   For each pair \( (X,Y)\in\{(H,V),(V,D),(D,H)\} \):  
   run every \( \sigma \in \mathcal{A}_{XY} \) → compute \( \mathrm{Coh}^{(\sigma)}_{XY} \).  
   Aggregate to \( \overline{\mathrm{Coh}}_{XY} \) and \( \mathrm{Var}_{XY} \).  
   Check \( \mathrm{Var}_{XY} \le \texttt{var\_floor} \) (witness).  
   Record \( \texttt{Lipschitz95} \) from mapped vs. original distances (witness).

4. **Compute metrics**  
   - \( V_c = (\overline{\mathrm{Coh}}_{HV}\overline{\mathrm{Coh}}_{VD}\overline{\mathrm{Coh}}_{DH})^{1/3} \).  
   - \( H_c, D_c \) per Core (use your declared stability/dynamics constructions).  
   - \( C_\Sigma = (H_c V_c D_c)^{1/3} \).

5. **Confidence (optional but recommended)**  
   Bootstrap indices and ensemble members to estimate a lower confidence bound \( \underline{C_\Sigma} \).

6. **Verdict**  
   - If any witness fails → **FAIL_DEGENERATE**.  
   - Else if \( C_\Sigma \ge \Theta \) (or \( \underline{C_\Sigma}\ge \Theta \) if using CI) → **PASS**.  
   - Else → **FAIL**.

7. **Provenance bundle (must ship)**  
   Context contracts, seeds, sampler indices, summary schemas, alignment ensemble specs, parameter values, \( \overline{\mathrm{Coh}}_{XY} \), \( \mathrm{Var}_{XY} \), witnesses, \( H_c,V_c,D_c,C_\Sigma \).

---

## 4 · Witnesses (Degeneracy Guards)

Witnesses are **monitors**, not metrics. Failure invalidates a run irrespective of \( C_\Sigma \).

- **Sample sufficiency:** \( |O_X| \ge n_{\min} \) for all aspects.  
- **Summary health:** \( H_X \ge \texttt{entropy\_floor\_X} \) and declared variance floors satisfied.  
- **Alignment stability:** \( \mathrm{Var}_{XY} \le \texttt{var\_floor} \) for each pair.  
- **Bounded distortion:** \( \texttt{Lipschitz95} \le \texttt{L\_max} \).  
- **Scale drift (if used):** coherence drift under declared \(\phi\) stays within the budgeted δ.

Each witness MUST include: the statistic, the floor/budget, and the decision.

---

## 5 · Controller (Minimal Adaptive Policy)

A small state machine that **selects ensembles and budgets** to keep verification stable and efficient. It does not change Core math.

**States and actions.**
- **HANDSHAKE** (calibrate) → choose orthogonal priors to reduce \( \mathrm{Var}_{XY} \) below floor.  
  Exit to **OPTIMIZE** when stable.
- **OPTIMIZE** (steady) → use high‑fidelity ensembles; maintain default budgets.  
  If \( C_\Sigma < \Theta \) but witnesses pass → remain or move to **REINFLATE** per policy.
- **REINFLATE** (robustify) → increase regularization, robust costs, broaden priors; aim to reduce variance and distortion.  
  Return to **OPTIMIZE** on stability; move to **MINIMAL_INFO** if resources constrained.
- **MINIMAL_INFO** (coarse) → cluster, coarse ensembles, expanded δ tolerances.  
  Go back to **OPTIMIZE** when resources permit.
- **LOCKDOWN** (freeze & monitor) → reuse last known‑good alignments; compute lower‑bound Coh and drift witnesses only.  
  Leave when conditions normalize.

**Transitions (sketch).**
- Enter **HANDSHAKE** on first run or after repeated variance failures.  
- Move **OPTIMIZE** → **REINFLATE** if \( C_\Sigma \ll \Theta \) while witnesses pass.  
- Move to **LOCKDOWN** on resource exhaustion or persistent instability.

All transitions and actions MUST be logged with reasons.

---

## 6 · Reproducibility and Provenance

Every verdict MUST be accompanied by a **reproducibility bundle** sufficient for third‑party recomputation:

- Context contracts and feature schemas for \( \Omega_X \).  
- Seeds for all randomized steps (samplers, bootstraps, solvers).  
- Definitions of \( \mathrm{Summary} \) per aspect.  
- Full alignment ensemble specs and policies used (including hyperparameters).  
- Parameter registry values (§2).  
- Raw coherence results \( \mathrm{Coh}^{(\sigma)}_{XY} \), means, variances, witness stats.  
- Final \( H_c,V_c,D_c,C_\Sigma \) (and confidence bounds if computed).

---

## 7 · What This Is Not (bounded clarification)

- **Not an ontology.** No new objects beyond those in the Core are introduced.  
- **Not a translation theory.** Alignment ensembles are **comparison devices** for measurement, not claims about inner mappings.  
- **Not a solver mandate.** The Operational layer defines **families** and **policies**; concrete solvers are interchangeable if they satisfy the ensemble‑stability witness and declared constraints.  
- **Not a metric redesign.** \( H_c,V_c,D_c,C_\Sigma \) remain as in the Core; this layer governs *how* to evaluate and *when* to accept.

---

## 8 · Minimal Reference Pseudocode

```text
INPUT: Ω_H,Ω_V,Ω_D; A_H,A_V,A_D; 𝒜_HV,𝒜_VD,𝒜_DH; params (α,λ,Θ,...)
STATE: controller_state ∈ {HANDSHAKE, OPTIMIZE, REINFLATE, MINIMAL_INFO, LOCKDOWN}

1  O_H ← A_H(≡); O_V ← A_V(≡); O_D ← A_D(≡)
2  Assert |O_X| ≥ n_min ∀X; else FAIL_DEGENERATE
3  S_H ← Summary(O_H); S_V ← Summary(O_V); S_D ← Summary(O_D)
4  For each (X,Y) in {(H,V),(V,D),(D,H)}:
5      Choose ensemble E := policy(controller_state, 𝒜_XY)
6      For each σ in E: Cohσ ← exp(−λ Δ(S_X,S_Y; σ))
7      Coh̄_XY ← meanσ Cohσ; Var_XY ← varσ Cohσ
8      Record Lipschitz95 from mapped vs original distances
9  Check witnesses (Var floors, Lipschitz, entropy/variance, n_min)
10 If any witness fails → FAIL_DEGENERATE
11 V_c ← (Coh̄_HV Coh̄_VD Coh̄_DH)^(1/3)
12 H_c, D_c ← declared constructions
13 C_Σ ← (H_c V_c D_c)^(1/3)
14 If C_Σ ≥ Θ → PASS else FAIL
15 Emit provenance bundle and controller actions taken