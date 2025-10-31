# TSC Core v2.2.2 - Complete Final Version

# Triadic Self-Coherence (TSC) — Core

**Version:** 2.2.2 (Braided Algebra Integration)
**Status:** Normative (measurement calculus)
**Dependency:** This document depends on **C≡ v2.2.2** (C-Calculus).

---

## −1 · Scope Note (What This Document Claims)

**TSC claims (operational):**
- Coherence is measurable as **dimensional consistency** across $\alpha/\beta/\gamma$.
- Triadic articulation is **sufficient** for this measurement (demonstrated by application).
- TSC **self-coheres** by its own standards (measurable via reflexive application in Operational $\S11$).

**TSC does not claim (out of scope):**
- Reality "is fundamentally triadic" (metaphysical necessity).
- Triadic structure is uniquely necessary (exclusivity).
- Coherence has ontological priority over other properties.

**$S_3$ invariance (normative).** All constructions MUST be invariant under any permutation of $\{\alpha, \beta, \gamma\}$. Implementations MUST NOT condition control flow on role names (R/I/E); only on axis labels. Role is a gauge of presentation.

**Validation stance:** Continuous **self-application** (see Operational $\S11$). If $C_{\Sigma}(\text{TSC})$ stays high across versions with dimension floors met, the framework is internally consistent for its purpose—no metaphysical commitment required.

---

## 0 · Objects and Notation

We work within the semantics of C≡. The primitive is $\mathbf{C}$ (cohering), residing in the carrier set $D$.

**Aspects (orthogonal axes).** $\alpha, \beta, \gamma$ denote three co-equal coordinates of articulation. Aspect set $\mathcal{A} = \{\alpha, \beta, \gamma\}$.

**Observation context.** For each axis $a\in\mathcal{A}$, a context $\Omega_a$ is a structured space (metric space, measure space, or abstract set with declared structure) in which observations reside.

**Articulation.** An articulation $A_a : D \to \mathcal{P}(\Omega_a)$ projects an element of the carrier set (typically $\mathbf{C}$) into an observable set $O_a \subset \Omega_a$.

**Structural summary.** A summary $S_a = (d_a, p_a, \mathcal{H}_a, \mathcal{I}_a)$ compresses $O_a$ into:
- $d_a$: a representative metric or embedding dimension
- $p_a$: a probability distribution over features
- $\mathcal{H}_a$: entropy of $p_a$ (to avoid collision with axis $\alpha$, we write $\mathcal{H}_a := -\sum_i p_a(i) \log p_a(i)$)
- $\mathcal{I}_a$: a set of invariants (e.g., conserved quantities, symmetry generators)

**Alignment.** An alignment $\sigma$ between summaries $S_a$ and $S_b$ is a correspondence (transport plan, matching, or structural map) with an associated cost or discrepancy $\Delta(S_a, S_b; \sigma)$.

**Coherence predicate.** $\mathrm{Coh}(S_a, S_b; \sigma) \in [0,1]$ measures how consistently $S_a$ and $S_b$ describe the same underlying cohering, given alignment $\sigma$.

**Ensemble.** An alignment ensemble $\mathcal{A}_{ab}$ is a finite family of alignment methods. We aggregate over the ensemble to produce a mean coherence and variance.

**Parameters.** Coherence parameters $\theta \in [0,1]$, $\lambda_{\alpha}, \lambda_{\beta}, \lambda_{\gamma} > 0$, $\Delta n > 0$, $\Theta\in(0,1]$, $\varepsilon > 0$ (numerical floor).

---

### 0.1 Confidence Intervals & Out-of-Distribution Gate (normative)

**Confidence intervals (CI).** All coherence scores MUST be reported with confidence bounds $[\text{CI}_{\text{lo}}, \text{CI}_{\text{hi}}]$ at a declared level (default 95%). Bootstrap over observation indices and ensemble members to estimate CI.

The alignment ensemble for each pair $(a,b)$ MUST satisfy $|\mathcal{A}_{ab}| \ge 3$ to enable variance and CI estimation.

**Out-of-distribution detection (OOD).** Maintain a reference distribution of historical $C_{\Sigma}$ values. For each new verification, compute a stability statistic $Z_t$ (e.g., z-score, KL divergence, Wasserstein distance) measuring deviation from the reference. If $Z_t \ge Z_{\text{crit}}$ (default 0.95 quantile), flag as out-of-distribution and trigger policy change (see Operational $\S10$).

---

## 1 · Axioms (Measurement Requirements)

**Distinction:** These are Core's measurement axioms, distinct from C≡'s algebraic axioms (C1-C6). Core axioms govern what makes a phenomenon measurable; C≡ axioms govern the structure of cohering itself.

**A1 (Completeness).** Every well-posed phenomenon admits an articulation into $(\Omega_\alpha, \Omega_\beta, \Omega_\gamma)$ such that observations $O_\alpha, O_\beta, O_\gamma$ are non-empty and summaries $S_\alpha, S_\beta, S_\gamma$ are well-defined.

**A2 (Commensurability).** For any pair of axes $(a,b)$, there exists a family of alignments $\mathcal{A}_{ab}$ such that the coherence predicate $\mathrm{Coh}(S_a, S_b; \sigma)$ is well-defined for all $\sigma \in \mathcal{A}_{ab}$. The predicate is symmetric: $\mathrm{Coh}(S_a, S_b; \sigma) = \mathrm{Coh}(S_b, S_a; \sigma^{-1})$ for appropriate inversion.

**Implementation note.** Symmetry is enforced by requiring bi-directional evaluation (forward and inverse alignments averaged) or ensembles closed under inversion (if $\sigma \in \mathcal{A}_{ab}$ then $\sigma^{-1} \in \mathcal{A}_{ba}$).

**A3 (Scale-equivariance).** Coherence is stable under scale transformations $\phi$: if $\phi$ acts uniformly on all axes, then $C_{\Sigma}(\phi(O_\alpha), \phi(O_\beta), \phi(O_\gamma)) \approx C_{\Sigma}(O_\alpha, O_\beta, O_\gamma)$ within a declared tolerance $\delta$.

**A4 (Self-articulation stability).** Applying an articulation $A_a$ twice ($A_a \circ A_a$) yields results $\equiv$-equivalent to $A_a(\mathbf{C})$ up to measurement noise. This is the empirical echo of the tripling rule $\equiv \equiv \equiv \to \equiv$ (C≡ Axiom C1).

---

## 2 · Coherence Predicate (Concrete Construction)

### 2.1 Discrepancy (Weight $\theta$ Separated from Axis $\alpha$)

Given summaries $S_a = (d_a, p_a, \mathcal{H}_a, \mathcal{I}_a)$ and $S_b = (d_b, p_b, \mathcal{H}_b, \mathcal{I}_b)$ and an alignment $\sigma$, define the discrepancy:

$$
\Delta(S_a, S_b; \sigma) = \theta \cdot \Delta_{\text{struct}}(d_a, d_b, \mathcal{I}_a, \mathcal{I}_b; \sigma) + (1 - \theta) \cdot \Delta_{\text{dist}}(p_a, p_b; \sigma)
$$

where:
- $\Delta_{\text{struct}}$ measures misalignment of structure/invariants (e.g., $|d_a - d_b|$ plus violations of $\mathcal{I}_a \cap \mathcal{I}_b$)
- $\Delta_{\text{dist}}$ measures distributional divergence (e.g., Jensen-Shannon divergence after alignment)
- $\theta \in [0,1]$ is a weighting parameter (default 0.7)

**Parameter provenance.** If $\theta$ is tuned from held-out data, the selection procedure MUST be recorded in provenance and $\theta$ frozen **before** computing final $C_{\Sigma}$.

**Scale discipline (Witness).** If either $\Delta_{\text{struct}}$ or $\Delta_{\text{dist}}$ requires feature scaling, provide a **1-Lipschitz calibration** into a common metric space and **record the calibration map or bound** in the provenance. (See Operational $\S4$ for Scale-Equivariance Witness enforcement).

---

### 2.2 Alignments (Correspondence for Comparison)

An alignment ensemble $\mathcal{A}_{ab}$ contains $|\mathcal{A}_{ab}| \ge 3$ distinct alignment methods (e.g., Gromov-Wasserstein, optimal transport with varying regularization, structural matching). Each $\sigma \in \mathcal{A}_{ab}$ produces a cost $\Delta(S_a, S_b; \sigma)$.

**Lipschitz bounds (Witness).** Each Summary operator MUST satisfy Lipschitz continuity with constant $L_{\text{sum}}$. Each alignment $\sigma \in \mathcal{A}_{ab}$ MUST have a bounded distortion constant $L_{\text{align}}$. These constants MUST be determined and **recorded in provenance** to support the coalgebra fixed-point theorem ($\S4.1$).

---

### 2.3 Exponential Coherence

Define the pairwise coherence:

$$
\mathrm{Coh}(S_a, S_b; \sigma) = \exp(-\lambda_{ab} \cdot \Delta(S_a, S_b; \sigma))
$$

where $\lambda_{ab} > 0$ is the sensitivity parameter for the $(a,b)$ pair. This maps discrepancy into $[0,1]$ with $\mathrm{Coh} \to 1$ as $\Delta \to 0$.

---

### 2.4 Ensemble Aggregation

For each pair $(a,b)$, compute:

$$
\overline{\mathrm{Coh}}_{ab} = \frac{1}{|\mathcal{A}_{ab}|} \sum_{\sigma \in \mathcal{A}_{ab}} \mathrm{Coh}(S_a, S_b; \sigma)
$$

$$
\mathrm{Var}_{ab} = \frac{1}{|\mathcal{A}_{ab}|} \sum_{\sigma} (\mathrm{Coh}^{(\sigma)}_{ab} - \overline{\mathrm{Coh}}_{ab})^2
$$

The mean $\overline{\mathrm{Coh}}_{ab}$ is our best estimate of pairwise coherence; $\mathrm{Var}_{ab}$ serves as a witness (see Operational $\S4$).

---

## 3 · Dimensional Scores

### 3.1 Pattern Stability ($\alpha_c$)

$\alpha_c$ measures how stable the $\alpha$-axis observations are under re-articulation or perturbation. One construction:

$$
\alpha_c = \exp(-\lambda_{\alpha} \cdot d_{\alpha}(S_{\alpha}, S'_{\alpha}))
$$

where $S'_{\alpha}$ is a summary from a perturbed or resampled $O_{\alpha}$, $d_{\alpha}$ is a declared metric on summaries (e.g., Wasserstein distance between $p_{\alpha}$ and $p'_{\alpha}$), and $\lambda_{\alpha} > 0$ is a sensitivity parameter.

**Protocol for $S'_{\alpha}$.** If re-run or disjoint split is infeasible, a **bootstrap-jackknife protocol** is allowed, but MUST include **block bootstrap** if observations are temporally or spatially correlated. Minimum block size $\Delta n$ is governed by $\S0$.

---

### 3.2 Process Stability ($\gamma_c$)

Let $t \in I_\gamma$ be indices from a declared temporal windowing policy (recorded in provenance). For successive observations $O_{\gamma}^{(t)}$ and $O_{\gamma}^{(t+1)}$, compute summaries $S_{\gamma}^{(t)}$ and $S_{\gamma}^{(t+1)}$, then:

$$
\gamma_c = \exp(-\lambda_{\gamma} \cdot W_{1}^{(d_{\gamma})}(p_{\gamma}^{(t)}, p_{\gamma}^{(t+\Delta t)}))
$$

where $W_1$ is the 1-Wasserstein distance between distributions and $\lambda_{\gamma} > 0$ is a sensitivity parameter.

**Grounding.** The ground metric $d_{\gamma}$ on the support of $p_{\gamma}$ and the time step $\Delta t$ MUST be fixed and recorded. If raw features are heterogeneous, provide a 1-Lipschitz calibration into a common metric space and record the calibration map.

**Alternative (coalgebraic).** $\gamma_c$ can also be defined via a dynamical operator $F: S_{\gamma}^{(t+1)} = F(S_{\gamma}^{(t)})$. Then $\gamma_c$ measures convergence to a fixed point or attractor.

---

### 3.3 Relational Coherence ($\beta_c$)

$$
\beta_c = (\overline{\mathrm{Coh}}_{\alpha\beta} \cdot \overline{\mathrm{Coh}}_{\beta\gamma} \cdot \overline{\mathrm{Coh}}_{\gamma\alpha})^{1/3}
$$

This is the geometric mean of the three pairwise coherences around the cycle $\alpha \to \beta \to \gamma \to \alpha$.

**Sensitivity.** Pairwise coherence uses the $\beta$-axis sensitivity: substitute $\lambda_{ab} \leftarrow \lambda_\beta$ in $\S2.3$ when computing $\overline{\mathrm{Coh}}_{ab}$ for all pairs in the cycle.

**Symmetry requirement.** For $S_3$ invariance, all three pairwise measurements MUST satisfy:
1. **Ensemble Cardinality:** $|\mathcal{A}_{\alpha\beta}| = |\mathcal{A}_{\beta\gamma}| = |\mathcal{A}_{\gamma\alpha}|$.
2. **Common Sensitivity:** $\lambda_{ab} = \lambda_\beta$ for all pairs.
3. **Identical Estimation Depth:** Identical bootstrap depth for CI estimation.

The specific aligners within each ensemble may differ per pair (adapted to each $\Omega_a$ structure).

---

## 4 · Aggregate Coherence ($C_{\Sigma}$)

The overall coherence is the geometric mean of the three dimensional scores:

$$
C_{\Sigma} = (\alpha_c \cdot \beta_c \cdot \gamma_c)^{1/3}
$$

**Rationale.** The geometric mean is used because it:
1. **Enforces Degeneracy:** $C_{\Sigma}=0$ if any $a_c=0$, preventing compensation.
2. **Preserves $S_3$-Symmetry:** Invariant under axis permutation (P1).
3. **Provides Homogeneity:** Compatible with the exponential coherence predicate ($\S2.3$).
4. **Enables Additivity:** The resulting leverage ($\lambda_{\Sigma}$) is additive in $\ln(a_c)$ ($\S8$).

**Explicit Floors.** All scores $a_c$ MUST be bounded below by the numerical floor $\varepsilon$ ($\S0$) before aggregation: $C_{\Sigma}$ is computed from $\max(a_c, \varepsilon)$ for each dimension.

**Weighted generalization.** For non-uniform weights $w_{\alpha}, w_{\beta}, w_{\gamma} > 0$ with $\sum w = 3$:

$$
C_{\Sigma} = \exp\left(\frac{1}{3} \cdot (w_{\alpha} \ln \alpha_c + w_{\beta} \ln \beta_c + w_{\gamma} \ln \gamma_c)\right)
$$

**Default (unweighted).** When $w_{\alpha} = w_{\beta} = w_{\gamma} = 1$ ($\sum w = 3$), this formula reduces to the geometric mean: $C_{\Sigma} = (\alpha_c \cdot \beta_c \cdot \gamma_c)^{1/3}$.

---

### 4.1 Coalgebra Stability Theorem (Sketch)

**Setup.** Let $\mathcal{S}^3$ be the space of summary triples $(S_{\alpha}, S_{\beta}, S_{\gamma})$ equipped with a metric $d_{\mathcal{S}}$. Define the triadic update operator which incorporates alignment-based updates:

$$
T: \mathcal{S}^3 \to \mathcal{S}^3
$$
$$
T(S_{\alpha}, S_{\beta}, S_{\gamma}) := (T_{\alpha}(S_{\beta}, S_{\gamma}), T_{\beta}(S_{\gamma}, S_{\alpha}), T_{\gamma}(S_{\alpha}, S_{\beta}))
$$

where each $T_a$ incorporates alignment-based updates from the other two axes.

**Claim (Contraction).** If the Lipschitz constants ($L_{\text{sum}}, L_{\text{align}}$) and the exponential sensitivity ($\lambda$) are chosen such that the product of the bounds satisfies:

$$
\lambda \cdot L_{\text{sum}} \cdot L_{\text{align}} < 1
$$

then $T$ is a contraction mapping on $\mathcal{S}^3$, and a unique fixed point $(\mathcal{S}^{*}_{\alpha}, \mathcal{S}^{*}_{\beta}, \mathcal{S}^{*}_{\gamma})$ exists. This fixed point represents a maximally coherent articulation.

**Compatibility with braided structure (Property).** The update operators $T_{a}$ MUST respect the natural isomorphisms $\varphi_{ab}$ (C≡ Axiom C5') such that the fixed point satisfies $\varphi_{ab}(T(\cdot)) \cong T(\varphi_{ab}(\cdot))$. (The formal proof of compatibility is deferred but required for structural soundness).

---

## 5 · Verification Interface (Input/Output Specification)

**Input specification.**
- Contexts: $\Omega_{\alpha}, \Omega_{\beta}, \Omega_{\gamma}$ (with declared structure: metric, measure, topology)
- Articulations: $A_{\alpha}, A_{\beta}, A_{\gamma}$ (algorithms producing observations)
- Alignment ensembles: $\mathcal{A}_{\alpha\beta}, \mathcal{A}_{\beta\gamma}, \mathcal{A}_{\gamma\alpha}$ (each with $|\mathcal{A}_{ab}| \ge 3$)
- **Parameters:** $\theta, \lambda_{\alpha}, \lambda_{\beta}, \lambda_{\gamma}, \Delta n, \varepsilon, \Theta \in \mathbb{R}^{+}$
- **Controller Settings:** $\tau_{\text{braid}}, Z_{\text{crit}} \in \mathbb{R}^{+}$ (defer policy to Operational)

**Output specification.**
- Dimensional scores: $\alpha_{c}, \beta_{c}, \gamma_{c} \in [0,1]$
- Aggregate: $C_{\Sigma} \in [0,1]$
- Confidence intervals: $[\text{CI}_{\text{lo}}, \text{CI}_{\text{hi}}]$ at declared level (default 95%)
- Pairwise coherences: $\overline{\mathrm{Coh}}_{\alpha\beta}, \overline{\mathrm{Coh}}_{\beta\gamma}, \overline{\mathrm{Coh}}_{\gamma\alpha}$
- Ensemble variances: $\mathrm{Var}_{\alpha\beta}, \mathrm{Var}_{\beta\gamma}, \mathrm{Var}_{\gamma\alpha}$
- **Dimensional leverage:** $\lambda_{\alpha}, \lambda_{\beta}, \lambda_{\gamma}, \lambda_{\Sigma} \in \mathbb{R}_{\ge 0}$ ($\S8$)
- **Stability Witnesses:** $L_{\text{sum}}, L_{\text{align}}$ (Lipschitz constants $\S2.2$), $\delta_{\text{MFI}}$ (Operational $\S4$)
- **OOD Statistic:** $Z_{t}$ (deviation from reference distribution $\S0.1$)
- **Provenance Bundle:** Complete record of all parameters, seeds, sampler indices, summary schemas, alignment ensemble specs, witness stats

**Naming.** In machine outputs use `C_sigma` for $C_{\Sigma}$, and `CI_lo`/`CI_hi` for the confidence bounds.

**Policy boundary.** The Core defines what to compute; Operational (next layer) defines when to accept/reject, how to handle controller states, and provenance requirements.

---

## 6 · Properties (Formal Guarantees)

**P1 ($S_3$-invariance).** All constructions are invariant under permutations of $\{\alpha,\beta,\gamma\}$. Formally: for any permutation $\pi \in S_3$,

$$
C_{\Sigma}(O_{\alpha}, O_{\beta}, O_{\gamma}) = C_{\Sigma}(O_{\pi(\alpha)}, O_{\pi(\beta)}, O_{\pi(\gamma)})
$$

**Proof sketch:** Follows directly from the geometric mean ($\S4$) and the axis-symmetric definitions of $\alpha_c, \beta_c, \gamma_c$ and their sensitivities ($\S3.3$).

**P2 (Normalization).** Perfect alignment ($\Delta = 0$ for all pairs) yields $C_{\Sigma} = 1$. Complete incoherence ($\Delta \to \infty$) yields $C_{\Sigma} \to 0$ (or $\varepsilon$ with floor).

**P3 (Monotonicity).** Improving any single dimensional score (holding others fixed) cannot decrease $C_{\Sigma}$.

**P4 (Degeneracy guard).** If any $\alpha_c, \beta_c$, or $\gamma_c$ equals zero, then $C_{\Sigma} = 0$ (or $\varepsilon^{1/3}$ with floor).

**P5 (Lipschitz continuity).** $C_{\Sigma}$ is Lipschitz continuous in the joint metric on $(O_{\alpha}, O_{\beta}, O_{\gamma})$, with constant:

$$
L_{C_{\Sigma}} \le L_{\text{sum}} \cdot L_{\text{align}} \cdot \max\{\lambda_{\alpha}, \lambda_{\beta}, \lambda_{\gamma}\}
$$

This follows from composition of Lipschitz maps ($\S2.2$) and the contraction bound ($\S4.1$).

---

## 7 · Composition (Modularity)

**Hierarchical articulation.** A phenomenon $P \in D$ may decompose into sub-phenomena $P_1, ..., P_n \in D$, each with its own triad $(\alpha_i, \beta_i, \gamma_i)$ and coherence $C_{\Sigma}(P_i)$.

**Composition rule (log-concave aggregation).** The coherence of the composite is bounded below by the geometric mean of the parts in log-space:

$$
C_{\Sigma}(P) \ge \exp\left(\frac{1}{n} \sum_{i=1}^{n} \ln C_{\Sigma}(P_i)\right) - \varepsilon_{\text{comp}}
$$

where $\varepsilon_{\text{comp}} \ge 0$ is the **coupling penalty** bounded by the discrepancy of the declared alignment between sub-phenomena. This **log-concave behavior** ensures that coherent modules remain coherently articulable under composition (modular stability).

**Coalgebraic link.** This modularity is a necessary consequence of the contraction property established in $\S4.1$.

**Fractal property.** Triadic structure recurs at every scale. Increasing resolution in any dimension causes the other two to emerge in measurement (holographic property).

---

## 8 · Diagnostics (Dimensional Leverage)

To pinpoint where coherence is lost, define dimensional leverage:

$$
\lambda_a = -\ln(\max(a_c, \varepsilon)) \quad \text{for } a \in \{\alpha, \beta, \gamma\}
$$

The aggregate leverage is:

$$
\lambda_{\Sigma} = \frac{1}{\sum w} \sum_{a \in \mathcal{A}} w_a \lambda_a
$$

(with $\sum w = 3$ by convention so unweighted aggregation matches the geometric mean; $\sum w = 1$ is equivalent up to scaling).

**Interpretation.** Higher $\lambda_a$ indicates dimension $a$ contributes more to incoherence. Policy (Operational layer) can allocate effort proportionally to $\lambda_a$ (recognition flow parameter $R_C$, see Operational $\S11.6$).

**Coherence energy.** An alternative additive view:

$$
E_{\Sigma} = -\frac{1}{3}(\ln \alpha_c + \ln \beta_c + \ln \gamma_c) = \lambda_{\Sigma}
$$

Minimizing $E_{\Sigma}$ is equivalent to maximizing $C_{\Sigma}$.

**Coherence-Energy Duality.** This definition satisfies the identity $\lambda_{\Sigma} = -\ln(C_{\Sigma})$ when $\sum w = 3$ and clamping is ignored ($\varepsilon \to 0$). Minimizing aggregate leverage is equivalent to maximizing aggregate coherence.

**Weight Convention.** The default is $w_{\alpha} = w_{\beta} = w_{\gamma} = 1$ ($\sum w = 3$).

---

## 9 · Relation to Traditional Concepts

**Emergence.** What appears as "emergent" properties at scale often reflects coarse-graining within a single coherent triad, not a new ontological level. Check if $C_{\Sigma}$ remains high across scales.

**Consciousness.** Treating $\alpha$ (pattern) and $\beta$ (relation) as separate domains producing each other creates a false gap. They are co-dimensions of experiencing ($\gamma$). The "hard problem" dissolves as a dimensional confusion.

**Self-reference.** The tripling rule ($\equiv \equiv \equiv \to \equiv$) normalizes self-application. TSC measuring itself (Operational $\S11$) is stable, not paradoxical, when $C_{\Sigma}(\text{TSC}) \ge \Theta$ with floors met.

**Representation.** Following Manzotti's spread mind: there are no $\alpha \leftrightarrow \beta$ "maps." $\alpha$ and $\beta$ are co-dimensions of the same process ($\gamma$). Alignment ensembles compare measurements, not translate between inner/outer domains.

---

## 10 · What This Document Does Not Define

- **Solver choice.** Alignment methods (Gromov-Wasserstein, optimal transport variants, etc.) are policy, not math. Core specifies the interface (cost $\Delta$, ensemble structure) but not the algorithm.
- **Acceptance thresholds.** The value of $\Theta$ (pass/fail threshold on $C_{\Sigma}$) lives in Operational.
- **Witness floors.** Specific values for variance floors, Lipschitz bounds, entropy floors are policy (Operational $\S2$).
- **Controller states.** HANDSHAKE, OPTIMIZE, REINFLATE, etc. are operational constructs (Operational $\S5$).
- **Provenance format.** The Core defines what to compute; Operational defines what to log and how.

---

## 11 · Implementation Notes (Informative)

**Summary construction.** For discrete observations $O_a$:
- $d_a$: intrinsic dimension (e.g., via PCA, manifold learning)
- $p_a$: empirical distribution over bins or features
- $\mathcal{H}_a$: Shannon entropy of $p_a$
- $\mathcal{I}_a$: detected symmetries (e.g., via group averaging) or conserved quantities

**Alignment methods.** Recommended starting ensemble:
1. Entropic-regularized optimal transport (varied $\varepsilon$)
2. Gromov-Wasserstein (for metric-only contexts)
3. Structural matching (for graph/relational contexts)

**Bootstrapping CI.** Resample observation indices with replacement; recompute $C_{\Sigma}$; take 2.5th and 97.5th percentiles for 95% CI.

**OOD tracking.** Maintain a rolling window (e.g., last 20 verifications) of $C_{\Sigma}$ values. Compute robust z-score: $Z_t = (C_{\Sigma}^{(t)} - \text{median}) / \text{IQR}$. Flag if $Z_t \ge Z_{\text{crit}}$.

---

**End — TSC Core v2.2.2 (Normative Measurement Calculus).**

