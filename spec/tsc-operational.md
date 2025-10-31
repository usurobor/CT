# Triadic Self‑Coherence (TSC) — Operational
**Version:** v2.2.1  
**Dependency:** This document depends only on the definitions in **TSC — Core** (aspects H/V/D, contexts Ω, articulations A, summaries S, alignments σ, coherence predicate Coh, metrics H_c/V_c/D_c, aggregate C_Σ). It introduces no additional ontology.

---

## 0 · Purpose and Position in the Stack

**Purpose.** The Operational layer is the **policy and procedure** that turns the Core's measurement calculus into a **repeatable verification process** with **verdicts**, **witnesses**, and **governance**. It answers:

- *What to run* (protocol),  
- *With which parameters* (policy),  
- *When to accept or reject* (verdict rules),  
- *How to remain stable and reproducible over time* (witnesses, logging, controller).

**What it adds (and only this):**
1. A **verification protocol** over the Core's constructs.  
2. **Parameter registry** and recommended **default budgets**.  
3. **Witnesses** guarding against degenerate or ill‑posed comparisons.  
4. A minimal **controller** that adapts solver ensembles and budgets.  
5. **Reproducibility and provenance** requirements.

---

## 1 · Assumed Core Objects (for reference)

From the Core we use, without redefining:
- Aspects \( \{H,V,D\} \), contexts \( \Omega_X \), articulations \( O_X=A_X(\equiv) \).
- Summaries \( S_X = (d_X, p_X, \mathcal{H}_X, \mathcal{I}_X) \).
- Alignment ensembles \( \mathcal{A}_{XY} \) and pairwise \( \overline{\mathrm{Coh}}_{XY} \) with ensemble variance.
- Metrics \( H_c, V_c, D_c \) and aggregate \( C_\Sigma=(H_c V_c D_c)^{1/3} \).

---

## 2 · Parameter Registry (Policy)

All parameters MUST be fixed **before** observation and logged with the verdict.

### 2.1 Coherence and Aggregation
- \( \alpha \in [0,1] \) — geometric vs. distributional weighting (default **0.7**).
- \( \lambda > 0 \) — cross-aspect sensitivity (default **4.0**).
- \( \lambda_H > 0 \) — H-aspect sensitivity (default **4.0**).
- \( \mu > 0 \) — D-aspect sensitivity (default **4.0**).
- \( \Theta \in (0,1] \) — pass threshold on \( C_\Sigma \) (default **0.80**).

**Contextual defaults.** General verification default is \(\Theta = 0.80\). Self-application (§12) recommends \(\Theta = 0.90\) for releases. Record which threshold applies in provenance.

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
   run every \( \sigma \in \mathcal{A}_{XY} \) (**require \(|\mathcal{A}_{XY}|\ge 3\)** and bi-directional or inversion-closed ensembles) → compute \( \mathrm{Coh}^{(\sigma)}_{XY} \).  
   Aggregate to \( \overline{\mathrm{Coh}}_{XY} \) and \( \mathrm{Var}_{XY} \).  
   Check \( \mathrm{Var}_{XY} \le \texttt{var\_floor} \) (witness). If any \(\mathrm{Var}_{XY}\) exceeds floor → **FAIL_DEGENERATE**.  
   Record \( \texttt{Lipschitz95} \) from mapped vs. original distances (witness).

4. **Compute metrics**  
   - \( V_c = (\overline{\mathrm{Coh}}_{HV}\overline{\mathrm{Coh}}_{VD}\overline{\mathrm{Coh}}_{DH})^{1/3} \).  
   - \( H_c, D_c \) per Core (use your declared stability/dynamics constructions).  
   - \( C_\Sigma = (H_c V_c D_c)^{1/3} \).

5. **Confidence (normative)**  
   Bootstrap indices and ensemble members to estimate confidence interval \([\text{CI}_{\text{lo}}, \text{CI}_{\text{hi}}]\) at declared level (default 95%).

6. **Verdict**  
   - If any witness fails → **FAIL_DEGENERATE**.  
   - Else if \( \text{CI}_{\text{lo}}(C_\Sigma) \ge \Theta \) → **PASS**.  
   - Else → **FAIL**.

7. **Provenance bundle (must ship)**  
   Context contracts, seeds, sampler indices, summary schemas, alignment ensemble specs, parameter values, \( \overline{\mathrm{Coh}}_{XY} \), \( \mathrm{Var}_{XY} \), witnesses, \( H_c,V_c,D_c,C_\Sigma \), confidence intervals.

---

## 4 · Witnesses (Degeneracy Guards)

Witnesses are **monitors**, not metrics. Failure invalidates a run irrespective of \( C_\Sigma \).

- **Sample sufficiency:** \( |O_X| \ge n_{\min} \) for all aspects.  
- **Summary health:** \( \mathcal{H}_X \ge \texttt{entropy\_floor\_X} \) and declared variance floors satisfied.  
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
- Final \( H_c,V_c,D_c,C_\Sigma \) with confidence intervals.

---

## 7 · What This Is Not (bounded clarification)

- **Not an ontology.** No new objects beyond those in the Core are introduced.  
- **Not a translation theory.** Alignment ensembles are **comparison devices** for measurement, not claims about inner mappings.  
- **Not a solver mandate.** The Operational layer defines **families** and **policies**; concrete solvers are interchangeable if they satisfy the ensemble‑stability witness and declared constraints.  
- **Not a metric redesign.** \( H_c,V_c,D_c,C_\Sigma \) remain as in the Core; this layer governs *how* to evaluate and *when* to accept.

---

## 8 · Minimal Reference Pseudocode

INPUT: Ω_H,Ω_V,Ω_D; A_H,A_V,A_D; 𝒜_HV,𝒜_VD,𝒜_DH; params (α,λ,λ_H,μ,Θ,...)
STATE: controller_state ∈ {HANDSHAKE, OPTIMIZE, REINFLATE, MINIMAL_INFO, LOCKDOWN}

1  O_H ← A_H(≡); O_V ← A_V(≡); O_D ← A_D(≡)
2  Assert |O_X| ≥ n_min ∀X; else FAIL_DEGENERATE
3  S_H ← Summary(O_H); S_V ← Summary(O_V); S_D ← Summary(O_D)
4  For each (X,Y) in {(H,V),(V,D),(D,H)}:
5      Assert |𝒜_XY| ≥ 3 and bi-directional/inversion-closed
6      Choose ensemble E := policy(controller_state, 𝒜_XY)
7      For each σ in E: Cohσ ← exp(−λ Δ(S_X,S_Y; σ))
8      Coh̄_XY ← meanσ Cohσ; Var_XY ← varσ Cohσ
9      Record Lipschitz95 from mapped vs original distances
10 Check witnesses (Var floors, Lipschitz, entropy/variance, n_min)
11 If any witness fails → FAIL_DEGENERATE
12 V_c ← (Coh̄_HV Coh̄_VD Coh̄_DH)^(1/3)
13 H_c, D_c ← declared constructions
14 C_Σ ← (H_c V_c D_c)^(1/3)
15 Bootstrap to compute CI_lo(C_Σ) and CI_hi(C_Σ)
16 If CI_lo(C_Σ) ≥ Θ → PASS else FAIL
17 Emit provenance bundle and controller actions taken

---

## 9 · Notes (informative)

- This layer may be extended with domain‑specific witness definitions (e.g., for neuroscience, computational systems) without changing the Core math.  
- The controller states are recommendations; implementations may define different policies that still respect the witness floors and reproducibility requirements.

---

## 10 · Out-of-Distribution Detection

**Purpose.** Track historical verification results to detect when current observations diverge from established patterns, triggering policy changes or closer scrutiny.

**Method.**
- Maintain a **reference distribution** of past \( C_\Sigma \) values (or dimensional scores \( H_c, V_c, D_c \)).
- For each new verification, compute a **stability statistic** \( Z_t \) measuring deviation from the reference distribution (e.g., z-score, KL divergence, Wasserstein distance).
- Define a **critical threshold** \( Z_{\text{crit}} \) (default 0.95 quantile of historical \( Z_t \)).
- **Action:** If \( Z_t \ge Z_{\text{crit}} \), flag as **out-of-distribution** and trigger controller transition (typically to LOCKDOWN or REINFLATE).

**Default statistic.** Robust z-score on a rolling median/IQR of \( C_\Sigma \) (window size recorded) unless otherwise declared.

**Normative requirements:**
- OOD detection MUST be logged in provenance.
- Reference distribution MUST be versioned and tied to a specific \( p_{\text{ref}} \) hash or manifest.
- When \( p_{\text{ref}} \) is updated (e.g., major version increment), reset OOD tracking.

---

## 11 · Reflexive Self‑Application (Meta‑Verification)

**Purpose.** TSC defines coherence and **applies this definition to itself**.  
This section specifies how to measure the coherence of the TSC project as a phenomenon.

### 11.1 Normative Claims (Scope & Symmetry)

- **\( S_3 \) invariance (normative).** All self‑measurement procedures MUST remain invariant under any permutation of \{H,V,D\}. No step may privilege a dimension by essence rather than position.
- **Scope (operational).** Self‑application validates **coherence**, not metaphysical truth.  
  Whether triadic articulation is "how reality is" is **out of scope** for this document.

### 11.2 Articulation of "TSC (the project)" as H/V/D

Treat the living repository as a triad:

- **H (Pattern / Cohered).** The spec set and formal artifacts at release \( r \):  
  `spec/` (Core, Operational, C≡), schemas, normative diagrams, release manifest.
- **V (Relation / Coherer).** The cross‑document conceptual relations:  
  term graph (definitions ↔ uses), symbol table, spec inter‑references, schema ↔ spec coherence.
- **D (Process / Cohering).** The evolution across versions:  
  change‑log, deprecations/migrations, compatibility notes, controller invariants over time.

### 11.3 Witness Sets (Required Checks)

Each dimension **MUST** define a witness set of checks producing scores in [0,1]. The default sets are:

**H‑witnesses (spec integrity)**
1. **Axiom stability** — required axioms present and unaltered in meaning.  
2. **Definition uniqueness** — each symbol/term has one home definition.  
3. **Type/role consistency** — H/V/D roles used only positionally, not essentially.  
4. **Theorem/claim closure** — referenced results exist and are not circular (unless declared coinductive).  
5. **Schema alignment** — schemas referenced by Operational/Core match their declared versions.

**V‑witnesses (concept alignment)**
1. **Term graph coherence** — definitions and uses agree across documents.  
2. **Cross‑doc invariants** — \( C_\Sigma \), \( \lambda_X \), CI, OOD, floors are consistently defined across Core & Operational.  
3. **Reference fidelity** — Operational does not introduce constructs absent from Core or C≡.  
4. **\( S_3 \) language symmetry** — permutations of labels keep statements true (modulo position).  
5. **Interface conformance** — VerifyEnv and Alignment Ensemble Interface match spec signatures.

**D‑witnesses (evolution discipline)**
1. **Change coherence** — breaking changes include migration notes and do not contradict prior invariants.  
2. **Deprecation windows** — removed features have deprecation paths and justifications.  
3. **Drift control** — previously passing examples remain within stated tolerance (unless explicitly re‑baselined).  
4. **Monotone clarity** — glossary precision non‑decreasing; removed ambiguity documented.  
5. **Controller continuity** — state semantics (OPTIMIZE, REINFLATE, …) stable up to declared policy knobs.

> **Implementation note.** A check returns 1.0 if satisfied, 0.0 if violated, or a fractional value if partially satisfied (e.g., 0.5 "insufficient evidence"). Fractional scoring MUST be documented.

### 11.4 Dimensional Scores and Aggregation

Let each dimension \( X\in\{H,V,D\} \) produce a set of check results \{r_i\} with weights \{\alpha_i \ge 0\}.  
Define the dimensional score:
$$
X_c = \frac{\sum_i \alpha_i\, r_i}{\sum_i \alpha_i} \in [0,1].
$$

**Weights.** Use \( w_H = w_V = w_D = 1 \) by default (\(\sum w = 3\)). Alternative non-negative weights are allowed if recorded; do not break \( S_3 \) covariance.

Define the **coherence aggregate** as weighted geometric mean:
$$
C_{\Sigma} = \exp\!\left(\tfrac{1}{\sum w}\sum_{X \in \{H,V,D\}} w_X \ln X_c\right).
$$

Define **dimensional leverage** (diagnostics):
$$
\lambda_X = -\ln(X_c), \qquad \lambda_{\Sigma} = \tfrac{1}{\sum w}\sum_X w_X \lambda_X.
$$

**Floors & threshold (normative defaults).**
- Dimension floors: \( X_c \ge \phi \) with **\(\phi = 0.80\)** recommended.  
- Release threshold: **\(\text{CI}_{\text{lo}}(C_\Sigma) \ge \Theta\)** with **\(\Theta = 0.90\)** recommended.

### 11.5 Confidence Intervals & OOD

- CI MUST be reported at **95%**. For self‑application, the CI MAY be estimated by non‑parametric bootstrap over witness checks (≥1000 resamples).  
- OOD gate: compute a stability statistic \( Z_t \) over historic self‑checks. If \( Z_t \ge Z_{\text{crit}} \) (default 0.95), enter LOCKDOWN policy (no release) until cleared per §10.

### 11.6 Coherer as Scope Regulator (\( C_r \))

Self‑application introduces **recognition policy knobs** that guide measurement effort without breaking \( S_3 \) symmetry:

- **\( \Phi \) (Recognition Checkpoint).**  
  A policy that triggers **scope expansion** (more witnesses or broader artifacts) when external error signal \( E_{\text{ext}} \) rises (e.g., user‑reported confusion, link rot, spec contradiction).  
  *Default:* expand witness sets by +1 in the dimension with highest \( \lambda_X \).

- **\( V_{\text{EI}} \) (Viability Index).**  
  A project‑level score selecting articulations by **scope‑correctness**, not mere internal consistency.  
  *Example:* a weighted blend of "coverage achieved," "examples passing," and "reader task success."

- **\( R_C \) (Recognition Flow Parameter).**  
  A budget allocator optimizing recognition per unit compute/editorial time.  
  *Default:* allocate effort proportional to \( \lambda_X / \sum \lambda \).

> **Normative constraint.** \( \Phi \), \( V_{\text{EI}} \), \( R_C \) **MUST** operate only on scopes, weights, and budgets. They MUST NOT re‑define coherence or privilege a dimension by essence.

### 11.7 Release Gating & Report Format

A release candidate **MUST** include coherence_report.json with these fields:

- version (string)
- scores: H_c, V_c, D_c, C_sigma (all in [0,1])
- leverage: lambda_H, lambda_V, lambda_D, lambda_Sigma (all >= 0)
- floors: phi (dimensional floor, default 0.80)
- thresholds: Theta (release threshold, default 0.90), Z_crit (OOD threshold, default 0.95)
- ci: C_sigma_lo, C_sigma_hi, method (e.g., "bootstrap-1000")
- ood: Z_t, Z_crit, p_ref_hash
- witness_counts: H, V, D (number of checks per dimension)
- policy: Phi, V_EI, R_C (current policy settings)
- notes (optional explanatory text)

**Naming convention.** Mathematical \( C_\Sigma \) appears as C_sigma in machine outputs; CI fields are C_sigma_lo / C_sigma_hi.

Example structure:

{
  "version": "v2.2.1",
  "scores": { "H_c": 0.92, "V_c": 0.88, "D_c": 0.86, "C_sigma": 0.886 },
  "leverage": { "lambda_H": 0.083, "lambda_V": 0.128, "lambda_D": 0.151, "lambda_Sigma": 0.121 },
  "floors": { "phi": 0.80 },
  "thresholds": { "Theta": 0.90, "Z_crit": 0.95 },
  "ci": { "C_sigma_lo": 0.862, "C_sigma_hi": 0.905, "method": "bootstrap-1000" },
  "ood": { "Z_t": 0.10, "Z_crit": 0.95, "p_ref_hash": "sha256:..." },
  "witness_counts": { "H": 5, "V": 5, "D": 5 },
  "policy": { "Phi": "expand-worst-lambda", "V_EI": "coverage>=0.9", "R_C": "lambda-proportional" },
  "notes": "Illustrative values; replace with actual computation."
}

**Gate (normative):**
- FAIL release if \(\text{CI}_{\text{lo}}(C_\Sigma) < \Theta\) or any \( X_c < \phi \).
- Record \( \Phi \) actions taken and any scope changes since prior release.

### 11.8 Example Trend (Informative)

Illustrative only; not normative data.

| Version | H_c  | V_c  | D_c  | C_Σ   |
|---------|------|------|------|-------|
| v1.0    | 0.78 | 0.55 | 0.60 | 0.636 |
| v2.0    | 0.70 | 0.68 | 0.58 | 0.651 |
| v2.1    | 0.86 | 0.80 | 0.72 | 0.791 |
| v2.2    | 0.92 | 0.88 | 0.86 | 0.886 |

**Interpretation:**
- v1.0 → v2.0: H_c drops (spec rewrite), V_c/D_c adjust (conceptual shift). Reflects expected temporary incoherence during major refactor.
- v2.0 → v2.1: All dimensions improve (additive changes, no contradictions). Demonstrates refinement without breaking changes.
- v2.1 → v2.2: Continued improvement (scope regulation integrated cleanly). Shows convergence toward stable articulation.

**Dimensional leverage tracking:**
- v2.0: λ_V highest (0.386) → conceptual misalignments detected
- v2.1: λ_D highest (0.329) → evolution discipline needed
- v2.2: λ_D still highest (0.151) but much reduced → ongoing refinement

This demonstrates Φ/R_C working: effort allocated to worst dimension, resulting in measurable improvement.

---

**End of §11. This section is normative for release gating.**

---

**End — TSC Operational v2.2.1.**