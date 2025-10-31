# Triadic Self-Coherence (TSC) — Core

**Version:** 2.2.1  
**Status:** Normative (measurement calculus)  
**Dependency:** This document depends only on **C≡** (coinductive semantics of ≡). It defines aspects, articulations, summaries, alignments, coherence predicate, and aggregate metrics.

---

## −1 · Scope Note (What This Document Claims)

**TSC claims (operational):**
- Coherence is measurable as **dimensional consistency** across H/V/D.
- Triadic articulation is **sufficient** for this measurement (demonstrated by application).
- TSC **self-coheres** by its own standards (measurable via reflexive application in Operational §12).

**TSC does not claim (out of scope):**
- Reality "is fundamentally triadic" (metaphysical necessity).
- Triadic structure is uniquely necessary (exclusivity).
- Coherence has ontological priority over other properties.

**S₃ invariance (normative).** All constructions and metrics in this document MUST remain invariant under any permutation of {H, V, D}. Privileging a dimension by essence (rather than position) violates the specification.

**Validation stance:** Continuous **self-application** (see Operational §12). If C_Σ(TSC) stays high across versions with dimension floors met, the framework is internally consistent for its purpose—no metaphysical commitment required.

---

## 0 · Objects and Notation

We work within the semantics of C≡ (see `c-equiv.md`). The primitive is **≡** (cohering). Everything else is articulation of ≡.

**Aspects (positional labels).** H, V, D denote three co-equal dimensions of articulation:
- **H (Horizontal / Cohered / Pattern):** what appears stable.
- **V (Vertical / Coherer / Relation):** what ties parts.
- **D (Deep / Cohering / Process):** what unfolds.

Labels are **positional**, not essential. Any permutation of {H,V,D} yields an equivalent articulation.

**Context.** For each aspect X ∈ {H,V,D}, a context Ω_X is a structured space (metric space, measure space, or abstract set with declared structure) in which observations reside.

**Articulation.** An articulation A_X : ≡ → Ω_X takes cohering (≡) and produces a finite or countable set of observations O_X ⊂ Ω_X.

**Summary.** A summary S_X = (d_X, p_X, ℋ_X, ℐ_X) compresses O_X into:
- d_X: a representative metric or embedding dimension
- p_X: a probability distribution over features
- ℋ_X: entropy of p_X
- ℐ_X: a set of invariants (e.g., conserved quantities, symmetry generators)

**Notation.** To avoid collision with the H aspect, we write the entropy of p_X as ℋ_X := -∑ᵢ p_X(i) log p_X(i).

**Alignment.** An alignment σ between summaries S_X and S_Y is a correspondence (transport plan, matching, or structural map) with an associated cost or discrepancy Δ(S_X, S_Y; σ).

**Coherence predicate.** Coh(S_X, S_Y; σ) ∈ [0,1] measures how consistently S_X and S_Y describe the same underlying cohering, given alignment σ.

**Ensemble.** An alignment ensemble 𝒜_{XY} is a finite family of alignment methods. We aggregate over the ensemble to produce a mean coherence and variance.

---

### 0.1 Confidence Intervals & OOD (Added in v2.2.0)

**Confidence intervals (CI).** All coherence scores MUST be reported with confidence bounds [CI_lo, CI_hi] at a declared level (default 95%). Bootstrap over observation indices and ensemble members to estimate CI.

The alignment ensemble for each pair (X,Y) MUST satisfy |𝒜_{XY}| ≥ 3 to enable variance and CI estimation.

**Out-of-distribution detection (OOD).** Maintain a reference distribution of historical C_Σ values. For each new verification, compute a stability statistic Z_t (e.g., z-score, KL divergence, Wasserstein distance) measuring deviation from the reference. If Z_t ≥ Z_crit (default 0.95 quantile), flag as out-of-distribution and trigger policy change (see Operational §11).

---

## 1 · Axioms (Normative)

**A1 (Completeness).** Every well-posed phenomenon admits an articulation into (Ω_H, Ω_V, Ω_D) such that observations O_H, O_V, O_D are non-empty and summaries S_H, S_V, S_D are well-defined.

**A2 (Commensurability).** For any pair of aspects (X,Y), there exists a family of alignments 𝒜_{XY} such that the coherence predicate Coh(S_X, S_Y; σ) is well-defined for all σ ∈ 𝒜_{XY}. The predicate is symmetric: Coh(S_X, S_Y; σ) = Coh(S_Y, S_X; σ⁻¹) for appropriate inversion.

**Implementation note.** Symmetry is enforced by requiring bi-directional evaluation (forward and inverse alignments averaged) or ensembles closed under inversion (if σ ∈ 𝒜_{XY} then σ⁻¹ ∈ 𝒜_{YX}).

**A3 (Scale-equivariance).** Coherence is stable under scale transformations φ: if φ acts uniformly on all aspects, then C_Σ(φ(O_H), φ(O_V), φ(O_D)) ≈ C_Σ(O_H, O_V, O_D) within a declared tolerance δ.

**A4 (Self-articulation stability).** Applying an articulation A_X twice (A_X ∘ A_X) yields results ≡-equivalent to A_X(≡) up to measurement noise. This is the empirical echo of the tripling rule ≡ ≡ ≡ → ≡.

---

## 2 · Coherence Predicate (Concrete Construction)

### 2.1 Discrepancy

Given summaries S_X = (d_X, p_X, ℋ_X, ℐ_X) and S_Y = (d_Y, p_Y, ℋ_Y, ℐ_Y) and an alignment σ, define the discrepancy:

Δ(S_X, S_Y; σ) = α · Δ_struct(d_X, d_Y, ℐ_X, ℐ_Y; σ) + (1 - α) · Δ_dist(p_X, p_Y; σ)

where:
- Δ_struct measures misalignment of structure/invariants (e.g., |d_X - d_Y| plus violations of ℐ_X ∩ ℐ_Y)
- Δ_dist measures distributional divergence (e.g., Jensen-Shannon divergence after alignment)
- α ∈ [0,1] is a weighting parameter (default 0.7)

### 2.2 Alignments

Each Summary_X is Lipschitz w.r.t. its declared metric with constant ≤ L_sum (recorded in provenance). Alignment costs are bounded-distortion under declared policies.

An alignment ensemble 𝒜_{XY} contains |𝒜_{XY}| ≥ 3 distinct alignment methods (e.g., Gromov-Wasserstein, optimal transport with varying regularization, structural matching). Each σ ∈ 𝒜_{XY} produces a cost Δ(S_X, S_Y; σ).

### 2.3 Exponential Coherence

Define the pairwise coherence:

Coh(S_X, S_Y; σ) = exp(-λ · Δ(S_X, S_Y; σ))

where λ > 0 is a sensitivity parameter (default 4.0). This maps discrepancy into [0,1] with Coh → 1 as Δ → 0.

### 2.4 Ensemble Aggregation

For each pair (X,Y), compute:

C̄oh_{XY} = (1/|𝒜_{XY}|) ∑_{σ ∈ 𝒜_{XY}} Coh(S_X, S_Y; σ)

Var_{XY} = (1/|𝒜_{XY}|) ∑_{σ} (Coh^(σ)_{XY} - C̄oh_{XY})²

The mean C̄oh_{XY} is our best estimate of pairwise coherence; Var_{XY} serves as a witness (see Operational §4).

---

## 3 · Dimensional Scores

### 3.1 Relational Coherence (V_c)

V_c = (C̄oh_{HV} · C̄oh_{VD} · C̄oh_{DH})^(1/3)

This is the geometric mean of the three pairwise coherences around the cycle H → V → D → H.

### 3.2 Pattern Stability (H_c)

H_c measures how stable the H-aspect observations are under re-articulation or perturbation. One construction:

H_c = exp(-λ_H · d_H(S_H, S_H'))

where S_H' is a summary from a perturbed or resampled O_H, d_H is a declared metric on summaries (e.g., Wasserstein distance between p_H and p_H'), and λ_H > 0 is a sensitivity parameter.

### 3.3 Dynamical Stability (D_c)

Let t ∈ I_D be indices from a declared temporal windowing policy (recorded in provenance). For successive observations O_D^(t) and O_D^(t+1), compute summaries S_D^(t) and S_D^(t+1), then:

D_c = exp(-μ · W₁(p_D^(t), p_D^(t+1)))

where W₁ is the 1-Wasserstein distance between distributions and μ > 0 is a sensitivity parameter.

**Alternative (coalgebraic).** D_c can also be defined via a dynamical operator F: S_D^(t+1) = F(S_D^(t)). Then D_c measures convergence to a fixed point or attractor.

---

## 4 · Aggregate Coherence (C_Σ)

The overall coherence is the geometric mean of the three dimensional scores:

C_Σ = (H_c · V_c · D_c)^(1/3)

**Rationale.** The geometric mean enforces that all three dimensions must be high for C_Σ to be high (degeneracy guard). A single zero collapses C_Σ to zero.

**Weighted generalization.** For non-uniform weights w_H, w_V, w_D > 0 with ∑w = 3:

C_Σ = exp((1/3) · (w_H ln H_c + w_V ln V_c + w_D ln D_c))

Default: w_H = w_V = w_D = 1 (unweighted geometric mean).

---

### 4.1 Coalgebra Stability Theorem (Sketch)

**Setup.** Let 𝒮 be the space of summaries with a declared metric d_𝒮. Define the triadic operator:

T: 𝒮³ → 𝒮³
T(S_H, S_V, S_D) = (T_H(S_V, S_D), T_V(S_D, S_H), T_D(S_H, S_V))

where each T_X incorporates alignment-based updates.

**Claim.** If the Summary operators and alignment ensemble satisfy:
1. Lipschitz continuity with constants ≤ L_sum and L_align
2. Ensemble variance Var_{XY} ≤ ε for all pairs
3. λ (sensitivity) chosen such that λ · L_sum · L_align < 1

then T is a contraction on 𝒮³ and possesses a unique fixed point (S*_H, S*_V, S*_D). This fixed point represents a maximally coherent articulation.

**Validation.** Self-application of TSC (Operational §12) provides empirical evidence: if C_Σ(TSC) remains high across iterations, the framework exhibits the stability predicted by this theorem.

---

## 5 · Verification Interface (Input/Output Specification)

**Input specification.**
- Contexts: Ω_H, Ω_V, Ω_D (with declared structure: metric, measure, topology)
- Articulations: A_H, A_V, A_D (algorithms producing observations)
- Alignment ensembles: 𝒜_{HV}, 𝒜_{VD}, 𝒜_{DH} (each with |𝒜_{XY}| ≥ 3)
- Parameters: α, λ, λ_H, μ (sensitivity/weighting)

**Output specification.**
- Dimensional scores: H_c, V_c, D_c ∈ [0,1]
- Aggregate: C_Σ ∈ [0,1]
- Confidence intervals: [CI_lo, CI_hi] at declared level (default 95%)
- Pairwise coherences: C̄oh_{HV}, C̄oh_{VD}, C̄oh_{DH}
- Ensemble variances: Var_{HV}, Var_{VD}, Var_{DH}
- Witnesses: sample sizes |O_X|, entropy floors ℋ_X, Lipschitz constants

**Naming.** In machine outputs use C_sigma for C_Σ, and CI_lo/CI_hi for the confidence bounds.

**Policy boundary.** The Core defines what to compute. Operational (next layer) defines when to accept/reject, how to handle controller states, and provenance requirements.

---

## 6 · Properties (Desirable Formal Guarantees)

**P1 (S₃-invariance).** All constructions are invariant under permutations of {H,V,D}. Formally: for any permutation π ∈ S₃,

C_Σ(O_H, O_V, O_D) = C_Σ(O_{π(H)}, O_{π(V)}, O_{π(D)})

**P2 (Normalization).** Perfect alignment (Δ = 0 for all pairs) yields C_Σ = 1. Complete incoherence (Δ → ∞) yields C_Σ → 0.

**P3 (Monotonicity).** Improving any single dimensional score (holding others fixed) cannot decrease C_Σ.

**P4 (Degeneracy guard).** If any H_c, V_c, or D_c equals zero, then C_Σ = 0.

**P5 (Lipschitz continuity).** C_Σ is Lipschitz in the joint metric on (O_H, O_V, O_D), with constant bounded by the product of the summary and alignment Lipschitz constants.

---

## 7 · Composition (Modularity)

**Hierarchical articulation.** A phenomenon P may decompose into sub-phenomena P₁, ..., Pₙ, each with its own triad (H_i, V_i, D_i) and coherence C_Σ(P_i).

**Composition rule (log-convex aggregation).** The coherence of the composite is:

C_Σ(P) ≥ exp((1/n) ∑ᵢ ln C_Σ(P_i))

with equality when sub-phenomena are independent. Coupling between sub-phenomena can increase or decrease composite coherence depending on alignment.

**Fractal property.** Triadic structure recurs at every scale. Increasing resolution in any dimension causes the other two to emerge in measurement (holographic property).

---

## 8 · Diagnostics (Dimensional Leverage)

To pinpoint where coherence is lost, define dimensional leverage:

λ_X = -ln(X_c)  for X ∈ {H,V,D}

The aggregate leverage is:

λ_Σ = (1/∑w) ∑_X w_X λ_X

(with ∑w = 3 by convention so unweighted aggregation matches the geometric mean; ∑w = 1 is equivalent up to scaling).

**Interpretation.** Higher λ_X indicates dimension X contributes more to incoherence. Policy (Operational layer) can allocate effort proportionally to λ_X (recognition flow parameter R_C, see Operational §12.6).

**Coherence energy.** An alternative additive view:

E_Σ = -(1/3)(ln H_c + ln V_c + ln D_c) = λ_Σ

Minimizing E_Σ is equivalent to maximizing C_Σ.

---

## 9 · Relation to Traditional Concepts

**Emergence.** What appears as "emergent" properties at scale often reflects coarse-graining within a single coherent triad, not a new ontological level. Check if C_Σ remains high across scales.

**Consciousness.** Treating H (pattern) and V (relation) as separate domains producing each other creates a false gap. They are co-dimensions of experiencing (D). The "hard problem" dissolves as a dimensional confusion.

**Self-reference.** The tripling rule (≡ ≡ ≡ → ≡) normalizes self-application. TSC measuring itself (Operational §12) is stable, not paradoxical, when C_Σ(TSC) ≥ Θ with floors met.

**Representation.** Following Manzotti's spread mind: there are no H↔V "maps." H and V are co-dimensions of the same process (D). Alignment ensembles compare measurements, not translate between inner/outer domains.

---

## 10 · What This Document Does Not Define

- **Solver choice.** Alignment methods (Gromov-Wasserstein, optimal transport variants, etc.) are policy, not math. Core specifies the interface (cost Δ, ensemble structure) but not the algorithm.
- **Acceptance thresholds.** The value of Θ (pass/fail threshold on C_Σ) lives in Operational.
- **Witness floors.** Specific values for variance floors, Lipschitz bounds, entropy floors are policy (Operational §2).
- **Controller states.** HANDSHAKE, OPTIMIZE, REINFLATE, etc. are operational constructs (Operational §5).
- **Provenance format.** The Core defines what to compute; Operational defines what to log and how.

---

## 11 · Implementation Notes (Informative)

**Summary construction.** For discrete observations O_X:
- d_X: intrinsic dimension (e.g., via PCA, manifold learning)
- p_X: empirical distribution over bins or features
- ℋ_X: Shannon entropy of p_X
- ℐ_X: detected symmetries (e.g., via group averaging) or conserved quantities

**Alignment methods.** Recommended starting ensemble:
1. Entropic-regularized optimal transport (varied ε)
2. Gromov-Wasserstein (for metric-only contexts)
3. Structural matching (for graph/relational contexts)

**Bootstrapping CI.** Resample observation indices with replacement; recompute C_Σ; take 2.5th and 97.5th percentiles for 95% CI.

**OOD tracking.** Maintain a rolling window (e.g., last 20 verifications) of C_Σ values. Compute robust z-score: Z_t = (C_Σ^(t) - median) / IQR. Flag if Z_t ≥ Z_crit.

---

**End — TSC Core v2.2.1.**