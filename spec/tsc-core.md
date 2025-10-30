# Triadic Self‑Coherence (TSC) — Core
**Version:** v2.0.0 (C≡‑native, self‑contained)

**Scope.** This document is normative and self‑contained. It defines the primitives, axioms, constructions, metrics, and semantics of Triadic Self‑Coherence. It depends on no other file.

---

## −1 · Ontological Bedrock (C≡)

**Primitive.** `≡` denotes a phenomenon understood as a *self‑labeling relation*.

**Aspectual articulation.** Every phenomenon articulates as three co‑constitutive aspects:
- **H** — structural/causal articulation (what holds together),
- **V** — relational/phenomenal articulation (how parts stand together),
- **D** — dynamical/functional articulation (how change/agency unfolds).

**Relational priority.** Relation is primary; relata crystallize within ongoing cohering. The three aspects are *co‑labels* of one phenomenon and admit role‑exchange across scales.

> The remainder of this file specifies how to measure whether the three articulations of the *same* phenomenon cohere.

---

## 0 · Objects and Notation

- **Aspects.** \( \mathcal{A}=\{H,V,D\} \).

- **Observation context.** For each \(X\in\mathcal{A}\), fix a set (or measurable/metric space) \( \Omega_X \) within which aspect \(X\) is observable.

- **Articulation operator.** For each \(X\), an operator
  \[
  A_X:\ \text{Phenomena}\ \rightsquigarrow\ \mathcal{P}(\Omega_X)
  \]
  returns a finite observation set \( O_X := A_X(\equiv) \subseteq \Omega_X \).

- **Structural summary.** Each observation set \( O_X \) admits a *summary*
  \[
  S_X = \mathrm{Summary}(O_X) = \big(d_X,\ p_X,\ H_X,\ \mathcal{I}_X\big),
  \]
  where:
  - \(d_X:\, O_X\times O_X\to \mathbb{R}_{\ge 0}\) is a metric (pairwise structure),
  - \(p_X\) is a probability mass function over declared features of \(O_X\) (distributional profile),
  - \(H_X := -\sum_i p_X(i)\log p_X(i)\) (entropy),
  - \(\mathcal{I}_X\) is an optional set of declared invariants (e.g., spectra, motif counts).

- **Parameters.** Coherence parameters \( \alpha\in[0,1] \), \( \lambda>0 \). Tolerances \( \tau,\varepsilon,\delta\ge 0 \). A pass threshold \( \Theta\in(0,1] \).

---

## 1 · Axioms (Aspectual)

**A1 · Aspect completeness (verification sufficiency).**  
For each \(X\in\mathcal{A}\) there exist admissible contexts \( \Omega_X \) and operators \(A_X\) such that \(O_X=A_X(\equiv)\) carries sufficient structure for non‑trivial cross‑aspect coherence evaluation with any \(Y\in\mathcal{A}\).

**A2 · Cross‑aspect commensurability.**  
For any \(X,Y\in\mathcal{A}\) there exists a *coherence predicate*
\[
\mathrm{Coh}_{XY}:\ \mathcal{P}(\Omega_X)\times\mathcal{P}(\Omega_Y)\to [0,1],
\]
satisfying: **symmetry** \( \mathrm{Coh}_{XY}(O_X,O_Y)=\mathrm{Coh}_{YX}(O_Y,O_X) \),  
**reflexivity** \( \mathrm{Coh}_{XX}(O_X,O_X)=1 \),  
**weak transitivity:** if \( \mathrm{Coh}_{XY}\ge \tau \) and \( \mathrm{Coh}_{YZ}\ge \tau \), then \( \mathrm{Coh}_{XZ}\ge \tau-\varepsilon \).

**A3 · Scale‑equivariance.**  
For declared scale morphisms \( \phi_X:\Omega_X\to\Omega_X \),
\[
\mathrm{Coh}_{XY}(\phi_X(O_X),\,\phi_Y(O_Y))=\mathrm{Coh}_{XY}(O_X,O_Y)\ \pm\ \delta(\phi_X,\phi_Y),
\]
with bounded drift \( \delta \).

**A4 · Self‑articulation stability.**  
Iterated self‑observation (articulating the articulation, etc.) converges to a stable class: there exists a unique (up to tolerance) fixed point of the triadic self‑application (see §4).

---

## 2 · Coherence Construction

### 2.1 Summaries (constructive)
Given \(O_X\), compute \(S_X=(d_X,p_X,H_X,\mathcal{I}_X)\) as in §0.  
The map \(\mathrm{Summary}\) is fixed *before* verification and may be domain‑specific.

### 2.2 Alignments (correspondence for comparison)
An **alignment** between \(O_X\) and \(O_Y\) is any weighted correspondence (e.g., a transport plan) \(\sigma_{XY}\) satisfying declared *structure‑preserving* constraints, such as:
- **Order preservation (tolerant).** If \( d_X(o_i,o_j) < d_X(o_k,o_\ell) \), then typically \( d_Y(\sigma o_i,\sigma o_j) \le d_Y(\sigma o_k,\sigma o_\ell) \) within a declared slack.
- **Bounded distortion.** \( d_Y(\sigma o_i,\sigma o_j) \le C\cdot d_X(o_i,o_j) \) for some \(C\ge 1\).
- **Flexible cardinality.** Partial and many‑to‑one correspondences are admissible.

An **alignment ensemble** \( \mathcal{A}_{XY} \) is any finite family of admissible alignments, fixed in advance.

### 2.3 Discrepancy and predicate
Define the discrepancy between summaries via alignment \(\sigma\):
\[
\Delta_{XY}^{(\sigma)}(S_X,S_Y)
:= \alpha\,\mathbb{E}_{(i,j)}\big|\,d_X(o_i,o_j)-d_Y(\sigma o_i,\sigma o_j)\,\big|
\ +\ (1-\alpha)\,\mathrm{JSD}(p_X\Vert p_Y),
\]
where \(\mathrm{JSD}\) is the Jensen–Shannon divergence:
\[
\mathrm{JSD}(p\Vert q)=\tfrac12\,\mathrm{KL}\!\big(p\Vert \tfrac12(p+q)\big)\ +\ \tfrac12\,\mathrm{KL}\!\big(q\Vert \tfrac12(p+q)\big),
\quad
\mathrm{KL}(a\Vert b)=\sum_i a_i\log\frac{a_i}{b_i}.
\]

The **pairwise coherence** for a chosen \(\sigma\) is
\[
\mathrm{Coh}^{(\sigma)}_{XY}(O_X,O_Y) = \exp\!\big(-\lambda\,\Delta_{XY}^{(\sigma)}(S_X,S_Y)\big).
\]

The **ensemble coherence** and **stability** are
\[
\overline{\mathrm{Coh}}_{XY} := \mathbb{E}_{\sigma\in \mathcal{A}_{XY}}\big[\mathrm{Coh}^{(\sigma)}_{XY}\big],
\qquad
\mathrm{Var}_{XY} := \mathrm{Var}_{\sigma\in \mathcal{A}_{XY}}\big[\mathrm{Coh}^{(\sigma)}_{XY}\big].
\]

A declared **stability floor** requires \( \mathrm{Var}_{XY} \) to remain below a fixed bound; otherwise the comparison is considered **degenerate**.

---

## 3 · Metrics

- **Within‑aspect stability (H\_c).** A scalar in \([0,1]\) derived from dispersion of repeated H‑articulations (e.g., exponential of a summary‑drift measure). One constructive choice is
  \[
  H_c := \exp\!\big(-\gamma_H\,\mathrm{Std}[p_H]\big)
  \]
  for a fixed \( \gamma_H>0 \).

- **Dynamical stability (D\_c).** A scalar in \([0,1]\) derived from temporal dispersion in D‑articulations. One constructive choice is
  \[
  D_c := \exp\!\big(-\mu\,\mathrm{Std}[p_D]\big)
  \]
  for a fixed \( \mu>0 \).

- **Cross‑aspect fit (V\_c).** Geometric mean of the three pairwise coherences:
  \[
  V_c := \big(\overline{\mathrm{Coh}}_{HV}\cdot \overline{\mathrm{Coh}}_{VD}\cdot \overline{\mathrm{Coh}}_{DH}\big)^{1/3}.
  \]

- **Aggregate coherence.**
  \[
  C_{\Sigma} := (H_c\,V_c\,D_c)^{1/3}.
  \]

A verification *passes* if \( C_{\Sigma} \ge \Theta \) and all declared stability floors are satisfied.

---

## 4 · Aspectual Coalgebra Semantics (self‑contained)

Let \( \mathcal{O} := \mathcal{P}(\Omega_H)\times \mathcal{P}(\Omega_V)\times \mathcal{P}(\Omega_D) \).  
Define the *articulation functor*
\[
F(\equiv) := \big(A_H(\equiv),\,A_V(\equiv),\,A_D(\equiv)\big) \in \mathcal{O}.
\]

A **coalgebra** is a pair \( (E,\delta) \) with \( \delta:E\to F(E) \).  
A morphism \(h:(E,\delta)\to(E',\delta')\) satisfies \( F(h)\circ \delta = \delta'\circ h \).

Equip \(\mathcal{O}\) with a metric \( \mathbf{d} \) induced by §2.3 (e.g., max of componentwise summary distances). Assume:
- **Lipschitz articulations.** Each \(A_X\) is Lipschitz into its summary metric.
- **Non‑expansive discrepancy.** The induced discrepancy under admissible alignments is non‑expansive in summaries.
- **Bounded scale drift.** Declared scale morphisms yield uniformly bounded \( \delta \) as in A3.

**Theorem (tolerant finality).** Under the above conditions, there exists a coalgebra \( (\mathbb{E},\Delta) \) such that for any \( (E,\delta) \) there is a unique \( h:E\to \mathbb{E} \) with
\[
\mathbf{d}\big(F(h)\circ \delta,\ \Delta\circ h\big) \le \tau,
\]
for a fixed tolerance \( \tau \). (Sketch: construct the terminal chain in \( (\mathcal{O},\mathbf{d}) \); completeness and non‑expansivity yield a Cauchy limit; approximate uniqueness follows from a tolerant fixed‑point argument.)

---

## 5 · Verification Interface (mathematical contract)

A *verification* is specified by:
1. Declared contexts \( \Omega_H,\Omega_V,\Omega_D \) and admissible summaries,
2. Articulation operators \( A_H,A_V,A_D \),
3. Alignment ensembles \( \mathcal{A}_{HV},\mathcal{A}_{VD},\mathcal{A}_{DH} \),
4. Parameters \( \alpha,\lambda,\Theta \) and stability floors.

**Procedure.**
- Produce \( O_X=A_X(\equiv) \) and \( S_X=\mathrm{Summary}(O_X) \),
- Compute \( \overline{\mathrm{Coh}}_{XY} \) and \( \mathrm{Var}_{XY} \) for all pairs,
- Compute \( H_c,D_c,V_c,C_{\Sigma} \) and verify stability floors,
- Return \( (H_c,V_c,D_c,C_{\Sigma}) \) and the pairwise coherence/stability diagnostics.

---

## 6 · Composition

For two phenomena with articulations \( O_X \) and \( O'_X \), define the **aligned product**
\[
O_X \otimes O'_X := \text{disjoint union with declared cross‑weights},
\]
and extend summaries and alignments block‑wise. With the constructions of §2–§3, the aggregate coherence satisfies a *log‑convexity* property under this product, ensuring modular verification.

---

## 7 · Parameters and Domains

- \( \alpha \in [0,1] \), \( \lambda>0 \), \( \Theta\in(0,1] \), tolerances \( \tau,\varepsilon,\delta\ge 0 \).
- All randomization, if any, must be declared with seeds; all summaries and ensembles must be fixed *before* observation.
- Every numeric choice must be recorded alongside the verification result to enable reproducibility.

---

## 8 · Symbols (quick reference)

- `≡` — phenomenon (self‑labeling relation).  
- \( \Omega_X \) — observation context for aspect \(X\).  
- \( A_X \) — articulation operator; \( O_X=A_X(\equiv) \).  
- \( S_X=(d_X,p_X,H_X,\mathcal{I}_X) \) — structural summary.  
- \( \sigma_{XY} \) — alignment (weighted correspondence).  
- \( \mathcal{A}_{XY} \) — alignment ensemble.  
- \( \Delta_{XY} \) — discrepancy; \( \mathrm{Coh}_{XY}=\exp(-\lambda \Delta_{XY}) \).  
- \( H_c, D_c, V_c, C_{\Sigma} \) — metrics and aggregate verdict.  
- \( \alpha,\lambda,\Theta,\tau,\varepsilon,\delta \) — parameters and tolerances.  
- \( F \), \( (E,\delta) \), \( (\mathbb{E},\Delta) \) — coalgebraic semantics.

---

**End — TSC Core (self‑contained).**