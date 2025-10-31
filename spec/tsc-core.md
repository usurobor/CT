```markdown
# Triadic Self‑Coherence (TSC) — Core

**Version:** v2.2.0 (C≡‑native, self‑contained)

**Status.** This file is normative and self‑contained. It defines the primitives, axioms, constructions, metrics, and semantics of Triadic Self‑Coherence. It depends on no other file.

---

## −1 · Ontological Bedrock (C≡)

**Primitive.** $\equiv$ denotes a phenomenon understood as a *self‑labeling relation*.

**Aspectual articulation.** Every phenomenon articulates as three co‑constitutive aspects:
- **H** — structural / causal articulation (what holds together),
- **V** — relational / phenomenal articulation (how parts stand together),
- **D** — dynamical / functional articulation (how change/agency unfolds).

**Relational priority.** Relation is primary; relata crystallize within ongoing cohering. The three aspects are *co‑labels* of one phenomenon and admit role‑exchange across scales.

> The remainder of this file specifies how to measure whether the three articulations of the *same* phenomenon cohere.

### Scope Note (Normative)

This specification defines **coherence measurement** as **dimensional consistency** across H/V/D with $S_3$ invariance. It remains **agnostic** about whether triadic articulation is ontologically fundamental, emergent, or observer‑relative. Such questions lie **outside measurement scope**.

**Operational test:** The framework's credibility derives from **self‑coherence**.  
If TSC measured as a phenomenon achieves **CI_lo($C_\Sigma$) $\ge \Theta$** with all dimension floors met, Core is internally consistent for its stated purpose.

---

## 0 · Objects and Notation

- **Aspects.** $\mathcal{A}=\{H,V,D\}$.

- **Observation context.** For each $X\in\mathcal{A}$, fix a set (or measurable/metric space) $\Omega_X$ within which aspect $X$ is observable.

- **Articulation operator.** For each $X$, an operator
  $$
  A_X:\ \text{Phenomena}\ \rightsquigarrow\ \mathcal{P}(\Omega_X)
  $$
  returns a finite observation set $O_X := A_X(\equiv) \subseteq \Omega_X$.

- **Structural summary.** Each observation set $O_X$ admits a *summary*
  $$
  S_X = \mathrm{Summary}(O_X) = \big(d_X,\ p_X,\ H_X,\ \mathcal{I}_X\big),
  $$
  where:
  - $d_X:\, O_X\times O_X\to \mathbb{R}_{\ge 0}$ is a metric (pairwise structure),
  - $p_X$ is a probability mass function over declared features of $O_X$ (distributional profile),
  - $H_X := -\sum_i p_X(i)\log p_X(i)$ (entropy; base of log is declared),
  - $\mathcal{I}_X$ is an optional set of declared invariants (e.g., spectra, motif counts).

- **Parameters.** Coherence parameters $\alpha\in[0,1]$, $\lambda>0$ (cross-aspect sensitivity), $\lambda_H>0$ (H-aspect sensitivity), $\mu>0$ (D-aspect sensitivity). Tolerances $\tau,\varepsilon,\delta\ge 0$. A pass threshold $\Theta\in(0,1]$. A confidence level for estimates (default 95%).

### 0.1 Confidence Intervals and Out-of-Distribution Detection

All reported scores $X_c, C_\Sigma$ **must** include confidence intervals at declared level (default 95%).

**Bootstrap CI (default method).** Resample alignment ensemble $\mathcal{A}_{XY}$ with replacement (≥1000 resamples); recompute $\overline{\mathrm{Coh}}_{XY}$ for each resample; report 2.5th and 97.5th percentiles as $[\text{CI}_{\text{lo}}, \text{CI}_{\text{hi}}]$.

**Analytic CI (alternative).** Use delta method with ensemble variance if alignments are approximately normal.

**OOD detection.** Track historical $C_\Sigma$ distribution across prior verifications; compute stability statistic $Z_t$; flag if $Z_t \ge Z_{\text{crit}}$ (see Operational §12 for specification).

---

## 1 · Axioms (Aspectual)

**A1 · Aspect completeness (verification sufficiency).** For each $X\in\mathcal{A}$ there exist admissible contexts $\Omega_X$ and operators $A_X$ such that $O_X=A_X(\equiv)$ carries sufficient structure for non‑trivial cross‑aspect coherence evaluation with any $Y\in\mathcal{A}$.

**A2 · Cross‑aspect commensurability.** For any $X,Y\in\mathcal{A}$ there exists a *coherence predicate*
$$
\mathrm{Coh}_{XY}:\ \mathcal{P}(\Omega_X)\times\mathcal{P}(\Omega_Y)\to [0,1],
$$
satisfying:  
**symmetry** $\mathrm{Coh}_{XY}(O_X,O_Y)=\mathrm{Coh}_{YX}(O_Y,O_X)$,  
**reflexivity** $\mathrm{Coh}_{XX}(O_X,O_X)=1$,  
**weak transitivity:** if $\mathrm{Coh}_{XY}\ge \tau$ and $\mathrm{Coh}_{YZ}\ge \tau$, then $\mathrm{Coh}_{XZ}\ge \tau-\varepsilon$.

**A3 · Scale‑equivariance.** For declared scale morphisms $\phi_X:\Omega_X\to\Omega_X$,
$$
\mathrm{Coh}_{XY}(\phi_X(O_X),\,\phi_Y(O_Y))=\mathrm{Coh}_{XY}(O_X,O_Y)\ \pm\ \delta(\phi_X,\phi_Y),
$$
with bounded drift $\delta$.

**A4 · Self‑articulation stability.** Iterated self‑observation (articulating the articulation, etc.) converges to a stable class: there exists a unique (up to tolerance) fixed point of the triadic self‑application (formalized in §4).

---

## 2 · Coherence Construction

### 2.1 Summaries (constructive)
Given $O_X$, compute $S_X=(d_X,p_X,H_X,\mathcal{I}_X)$ as in §0.  
The map $\mathrm{Summary}$ is fixed *before* verification and may be domain‑specific.

### 2.2 Alignments (correspondence for comparison)
An **alignment** between $O_X$ and $O_Y$ is any weighted correspondence $\sigma_{XY}$ associating elements of $O_X$ to elements of $O_Y$ such that declared *structure‑preserving* constraints hold. A concrete model may be a **transport plan** (e.g., Optimal Transport), graph matching, kernel alignment, or any correspondence satisfying declared structure-preserving constraints.

An **alignment ensemble** $\mathcal{A}_{XY}$ is any finite family of admissible alignments, fixed in advance.

**Normative requirement.** The ensemble $\mathcal{A}_{XY}$ **must** include at least 3 distinct alignments to support variance estimation. Variance **must** remain below declared stability floor; otherwise the comparison is **degenerate**.

### 2.3 Discrepancy and predicate
Define the discrepancy between summaries via alignment $\sigma$:
$$
\Delta_{XY}^{(\sigma)}(S_X,S_Y)
:= \alpha\,\mathbb{E}_{(i,j)}\big|\,d_X(o_i,o_j)-d_Y(\sigma o_i,\sigma o_j)\,\big|
\ +\ (1-\alpha)\,\mathrm{JSD}(p_X\Vert p_Y),
$$
where $\mathrm{JSD}$ is the Jensen–Shannon divergence.

The **pairwise coherence** for a chosen $\sigma$ is
$$
\mathrm{Coh}^{(\sigma)}_{XY}(O_X,O_Y) = \exp\!\big(-\lambda\,\Delta_{XY}^{(\sigma)}(S_X,S_Y)\big)\in[0,1].
$$

The **ensemble coherence** and **stability** are
$$
\overline{\mathrm{Coh}}_{XY} := \mathbb{E}_{\sigma\in \mathcal{A}_{XY}}\big[\mathrm{Coh}^{(\sigma)}_{XY}\big],
\qquad
\mathrm{Var}_{XY} := \mathrm{Var}_{\sigma\in \mathcal{A}_{XY}}\big[\mathrm{Coh}^{(\sigma)}_{XY}\big].
$$

---

## 3 · Per‑Aspect Metrics and Aggregate

### 3.1 Within‑aspect stability ($H_c$)

Let $\{O_H^{(r)}\}_r$ be repeated H‑articulations (≥2 required). Define $H_c$ as the ensemble-averaged coherence between the resulting summaries:
$$
H_c\ :=\ \mathbb{E}_{r\neq s}\left[\exp\!\big(-\lambda_H\,\Delta_{HH}^{(\sigma^*)}\big(S_H^{(r)},S_H^{(s)}\big)\big)\right],
$$
where $\sigma^*$ is the chosen admissible H-alignment (typically selected by minimum discrepancy $\Delta_{HH}$ across $\mathcal{A}_{HH}$).

### 3.2 Dynamical stability ($D_c$)

Dynamical coherence uses **distributional distance** rather than structural discrepancy. Let $p_D^{(t)}$ and $p_D^{(t+1)}$ be successive feature distributions extracted from $S_D^{(t)}$ and $S_D^{(t+1)}$. The stability is based on the **Wasserstein‑1 distance** ($W_1$):
$$
D_c\ :=\ \exp\!\big(-\mu\, W_1(p_D^{(t)},p_D^{(t+1)})\big).
$$

**Rationale:** Process evolution is captured by how probability mass moves across feature space, not by pairwise metric preservation. This reflects the temporal flow of dynamical systems.

### 3.3 Cross‑aspect coherence ($V_c$) and aggregate
The geometric mean of the three ensemble pairwise coherences:
$$
V_c\ :=\ \big(\ \overline{\mathrm{Coh}}_{HV}\ \cdot\ \overline{\mathrm{Coh}}_{VD}\ \cdot\ \overline{\mathrm{Coh}}_{DH}\ \big)^{1/3}.
$$

The **aggregate triadic coherence** is
$$
C_\Sigma\ :=\ \big(H_c\cdot V_c\cdot D_c\big)^{1/3}\in[0,1].
$$

A verification *passes* if **CI_lo($C_\Sigma$) $\ge \Theta$** and all declared stability floors (variance bounds) are satisfied.

---

## 4 · Aspectual Coalgebra Semantics (Fixed‑Point Stability)

**Theorem (self-application convergence).** The triadic articulation functor 
$$
F: (\mathcal{A}, \mathbf{d}) \to (\mathcal{A}, \mathbf{d})
$$
defined by repeated application of $\mathrm{Summary} \circ A_X$ (articulation followed by summarization) is a **contraction** on the product metric space of aspect summaries, ensuring a unique fixed-point under iterated self-observation.

**Formal statement.** There exists $k \in (0,1)$ such that for any two summary triples $\mathbf{S}_1=(S_H^{(1)}, S_V^{(1)}, S_D^{(1)})$ and $\mathbf{S}_2=(S_H^{(2)}, S_V^{(2)}, S_D^{(2)})$:
$$
\mathbf{d}(F(\mathbf{S}_1), F(\mathbf{S}_2)) \le k \cdot \mathbf{d}(\mathbf{S}_1, \mathbf{S}_2),
$$
where $\mathbf{d}$ is the product metric $\mathbf{d}(\mathbf{S}_1, \mathbf{S}_2) = \sum_{X \in \mathcal{A}} \Delta_{XX}(S_X^{(1)}, S_X^{(2)})$.

**Proof.** Deferred to technical appendix. The contraction property follows from: (1) bounded Lipschitz constants of summary operators, (2) exponential decay in $\mathrm{Coh}$ predicate, and (3) geometric mean aggregation dampening maximal discrepancies. $\square$

**Corollary (Axiom A4).** This establishes self-articulation stability: **iterated self-observation** of any coherent phenomenon (including TSC as phenomenon) converges to a stable coherence class. Specifically, $\lim_{n\to\infty} F^n(\mathbf{S}_0)$ exists and is independent of initial summary $\mathbf{S}_0$ (up to declared tolerance).

**Operational consequence.** Reflexive self-application (§12 in Operational) will exhibit stable $C_\Sigma$ across iterations, validating the framework's internal consistency.

---

## 5 · Verification Interface (Abstract)

A verification instance $\mathcal{V}$ consists of:

**Required components:**
- **Contexts:** $\{\Omega_X\}_{X \in \mathcal{A}}$ (observation spaces with declared structure)
- **Operators:** $\{A_X\}_{X \in \mathcal{A}}$ (articulation maps: phenomenon → observations)
- **Summaries:** $\{\mathrm{Summary}_X\}$ (structure extractors: observations → $(d_X, p_X, H_X, \mathcal{I}_X)$)
- **Alignments:** $\{\mathcal{A}_{XY}\}$ (ensemble per aspect pair, $|\mathcal{A}_{XY}| \ge 3$)
- **Parameters:** $\alpha \in [0,1]$, $\lambda, \lambda_H, \mu > 0$, $\Theta \in (0,1]$, tolerance bounds $\tau, \varepsilon, \delta \ge 0$
- **Seeds:** All randomness sources (for alignment sampling, bootstrap resampling)

**Output specification:**
$$
\mathcal{V}(\equiv) = (H_c, V_c, D_c, C_\Sigma, \{\mathrm{Var}_{XY}\}, [\text{CI}_{\text{lo}}, \text{CI}_{\text{hi}}], \text{provenance})
$$

**Normative constraints:**
1. All components **must** be fixed and recorded *before* $A_X$ is applied to phenomenon $\equiv$
2. Provenance record **must** include: version, timestamp, parameter values, seed values, alignment ensemble specifications
3. If any $\mathrm{Var}_{XY}$ exceeds declared stability floor, verification **must** be marked **degenerate**
4. CI bounds **must** be reported; pass criterion applies to **CI_lo($C_\Sigma$)**, not point estimate

---

## 6 · Composition

Given two phenomena $\equiv_1, \equiv_2$ with observations $O_X^{(1)}, O_X^{(2)}$, define the **aligned product**:
$$
O_X^{(1)} \otimes O_X^{(2)} := \{(o_i^{(1)}, o_j^{(2)}) : (i,j) \in \text{declared alignment}\}.
$$

The alignment may be induced by shared context (e.g., temporal co-occurrence, spatial proximity, shared causal structure).

**Property (log-convexity of coherence under composition).** Under appropriate alignment that preserves structure across both phenomena, the aggregate coherence satisfies:
$$
\ln C_\Sigma(O_X^{(1)} \otimes O_X^{(2)}) \ge \frac{1}{2}\big(\ln C_\Sigma(O_X^{(1)}) + \ln C_\Sigma(O_X^{(2)})\big) - \epsilon_{\text{comp}},
$$
where $\epsilon_{\text{comp}} \ge 0$ is a composition penalty bounded by the discrepancy of the declared alignment between $O_X^{(1)}$ and $O_X^{(2)}$. Specifically: $\epsilon_{\text{comp}} \le C \cdot \Delta_{\text{align}}$ for some constant $C$ and alignment discrepancy $\Delta_{\text{align}}$.

**Interpretation:** Modular composition cannot decrease coherence faster than linear interpolation in log-space. This ensures stability under hierarchical construction: coherent sub-phenomena compose into coherent larger phenomena.

**Proof sketch.** Follows from subadditivity of KL divergence and log-concavity of geometric mean. Full proof in technical appendix. $\square$

---

## 7 · Integrity and Provenance

**Normative requirements for reproducibility:**

1. **Pre-commitment.** All parameters ($\alpha, \lambda, \lambda_H, \mu, \Theta$), contexts ($\Omega_X$), operators ($A_X$), summaries ($\mathrm{Summary}_X$), and alignment ensembles ($\mathcal{A}_{XY}$) **must** be fixed and recorded *before* observation.

2. **Seed control.** Any stochastic process (alignment sampling, bootstrap resampling) **must** use declared seeds. Seeds **must** be recorded in provenance.

3. **Version pinning.** Implementations **must** record: TSC Core version, Summary implementation version, Alignment method version.

4. **Audit trail.** Each verification **must** produce a provenance record containing:
   - Timestamp (ISO 8601)
   - All parameter values
   - All seed values  
   - Alignment ensemble specification
   - Summary method specification
   - OOD status (if applicable)
   - Full $(H_c, V_c, D_c, C_\Sigma, \text{CI})$ with variance diagnostics

5. **Falsifiability.** Given identical provenance record, verification **must** be reproducible (up to declared numerical tolerance).

---

## 8 · Dimensional Leverage (Diagnostics)

Define the **dimensional leverage** for each aspect $X \in \{H, V, D\}$:
$$
\lambda_X := -\ln(X_c) \in [0, \infty),
$$
and the **aggregate leverage**:
$$
\lambda_\Sigma := \frac{1}{3}(\lambda_H + \lambda_V + \lambda_D) = -\ln(C_\Sigma).
$$

**For weighted aggregation** (if using non-uniform weights $w_H, w_V, w_D$ where $\sum w = 3$ and weights are **$S_3$-covariant** under role relabeling):
$$
\lambda_\Sigma = \frac{1}{\sum w}\sum_{X} w_X \lambda_X.
$$

**Interpretation:**
- $\lambda_X$ quantifies "where coherence is lost" in dimension $X$
- Higher $\lambda_X$ indicates lower coherence contribution from aspect $X$
- Additive form enables diagnostic: "expand recognition scope in dimension with highest $\lambda_X$"

**Operational use:** Dimensional leverage guides recognition policies ($\Phi, R_C$) in Operational specification (§12). When external error signal triggers scope expansion, allocate effort proportional to $\lambda_X / \sum \lambda$.

### 8.1 Relation to Operational Specification

This Core defines **what** to compute (metrics, axioms, theorems).

**Operational (§12)** specifies **how** to apply these constructs reflexively to TSC itself, including:
- Witness sets for H/V/D dimensions
- Release gating on CI_lo($C_\Sigma$) $\ge \Theta$
- C_r policies ($\Phi$/V_EI/R_C) using dimensional leverage

**Separation of concerns:** Core remains algorithm-agnostic; Operational adds policy without redefining coherence.

---

**End — TSC Core v2.2.0 (self‑contained).**
```