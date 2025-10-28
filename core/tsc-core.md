# Triadic Self-Coherence (TSC) — Core Knowledge File
**Version:** v1.1.19 — Stable Mathematical Core (Revised)  
**Status:** Stable mathematical foundation (updates are rare, versioned, and backwards‑compatible)  
**Use:** Canonical reference for axioms, objects, metrics, and theorems of TSC.  
*(Operational choices — thresholds, tolerances, cadence, gauges, repair policies — are out of scope and belong to the operational addendum.)*

---

## 0 · Purpose and Scope
This document specifies the **mathematical core** of Triadic Self‑Coherence (TSC). It defines the coherence object, triadic axioms, metric–topological semantics, bisimulation, dimensional coherence metrics, and key theorems (including final‑coalgebra uniqueness and compositional stability).

**Revision note (v1.1.19):**
- Removes the “immutability” clause of prior editions; the core is **stable** rather than immutable. Revisions are **rare**, **versioned**, and designed for **backwards compatibility**.
- Eliminates **hard‑coded constants** (e.g., numeric pass thresholds). Such choices are modeled as **symbols/parameters** in this core and must be **instantiated** by the operational layer.

---

## 1 · Triadic Axioms (Structural Invariants)
Let \(C\) denote the **coherence object**. For each vantage \(X \in \{H,V,D\}\) (Horizontal, Vertical, Deep):

- **Lens:** \(L_X : C \to R_X\) and **Reconstructor:** \(\varepsilon_X : R_X \to C\) with
\[
\varepsilon_X \circ L_X \;=\; \mathrm{id}_C \qquad \text{(A1: Vantage Sufficiency)}.
\]

**A2: Vantage‑Swap Compatibility.**  
There exist bijections \(\sigma_{XY} : R_X \leftrightarrow R_Y\) with inverses \(\sigma_{YX}=\sigma_{XY}^{-1}\) such that
\[
L_X \;=\; \sigma_{YX} \circ L_Y, \qquad
\varepsilon_X \;=\; \varepsilon_Y \circ \sigma_{XY},
\]
and each \(\sigma_{XY}\) is **1‑Lipschitz (non‑expansive)**; isometries are the ideal case.

**A3: Scale Equivariance (Fractal–Holographic Law).**  
For any scale morphism \(s: C \to C\) there exist \(\phi_X : R_X \to R_X\) with
\[
L_X \circ s \;=\; \phi_X \circ L_X, \qquad
\varepsilon_X \circ \phi_X \;=\; s \circ \varepsilon_X.
\]

**A4: Coinductive Closure (Finality).**  
Let \(\Delta : C \to R_H \times R_V \times R_D\) be \(\Delta(c)=(L_H(c),L_V(c),L_D(c))\).  
\((C,\Delta)\) is **final** in its coalgebra class: every other triadic observation factors uniquely (up to a \(\tau\)-isometry) through \(C\).

---

## 2 · Metric–Topological Semantics
Work in \(\mathfrak{Met}_\tau\), the category of metric‑tolerant spaces with 1‑Lipschitz morphisms.

- Each \(R_X\) carries a metric \(d_X\).  
- **Semantic equivalence:** \(a \approx b \iff d_X(a,b) \le \tau_X\).  
- A change of vantage \(\sigma_{XY}\) is TSC‑valid if
\[
\big|\, d_X(a,b) - d_Y(\sigma_{XY}(a), \sigma_{XY}(b)) \,\big| \le \tau.
\]
- **Parameters (symbolic):** scale factors \(\lambda,\mu>0\), transport regularizer \(\varepsilon\ge 0\). The core **does not** assign numeric values; instantiation is operational.
- Expectations \(\mathbb{E}[\cdot]\) are over an explicit index set \(I\); the operational layer **must report \(I\)** when publishing metrics.
- **Dynamics carrier:** Fix a measurable space \(M\) and a Markov kernel \(S_t : M \to \mathcal{D}(M)\) (time‑indexed). How \(M\) and \(S_t\) are constructed (e.g., via a chosen vantage \(X^\star\) and its \(R_{X^\star}\)) is an **operational** declaration.

Define the clamping map \(\rho(x) = \max(0,\min(1,x))\).

---

## 3 · Bisimulation (Behavioral Equivalence)
Let \(\mathcal{S}_X : M_X \to \mathcal{D}(M_X)\) be a vantage‑specific transition operator; endow \(\mathcal{D}(M_X)\) with \(W_1\) (Wasserstein‑1).

A relation \(R \subseteq M_X \times M_X\) is a **bisimulation** iff for all \((a,b)\in R\):
1) \(d_X(a,b) \le \tau_X\), and  
2) \(W_1(\mathcal{S}_X(a), \mathcal{S}_X(b)) \le \tau_X\).

Triadic bisimilarity requires the condition hold under all three vantages.

---

## 4 · Dimensional Coherence Metrics
With \(\lambda,\mu>0\) and time‑indexed sequences or samples from \(I\):

\[
\begin{aligned}
H_c &= \mathbb{E}_{(i,j)\in I}\!\left[\exp\!\big(-\lambda \cdot d_H(R_H^i, R_H^j)\big)\right],\\[4pt]
V_c &= \rho\!\left( 1 - \tfrac{1}{3}\!\sum_{X\neq Y}\mathbb{E}_{(a,b)\in I}\!\Big[ \big|\, d_X(a,b) - d_Y(\sigma_{XY}(a),\sigma_{XY}(b)) \,\big| \Big] \right),\\[4pt]
D_c &= \exp\!\big(-\mu \cdot W_1(S_t, S_{t+1})\big),\\[6pt]
C_\Sigma &= \big(H_c \cdot V_c \cdot D_c\big)^{1/3}.
\end{aligned}
\]

> **Thresholds.** The core **does not** prescribe a numeric pass threshold for \(C_\Sigma\).  
> An operational symbol \(\Theta\in(0,1]\) may be introduced for policy (e.g., “PASS iff \(C_\Sigma \ge \Theta\)” or CI‑based criteria). Selection, estimation, and auditing of \(\Theta\) are **operational** concerns.

---

## 5 · Verification Routine (Abstract)
This core specifies an **abstract** verification that returns metrics and constraint checks. Any **pass/fail** decision (thresholding, CI bounds, OOD handling, sampling policy) is delegated to the operational layer.

**procedure \(\mathrm{VERIFY\_TSC}(C)\):**  
1. Compute \(R_X \leftarrow L_X(C)\) for \(X\in\{H,V,D\}\).  
2. Check A1–A3 symbolically (up to \(\tau\)): \(\varepsilon_X\!\circ\!L_X \approx \mathrm{id}_C\); \(\sigma,\phi\) respect \(d_X\).  
3. Compute \(H_c,V_c,D_c,C_\Sigma\) (using declared \(I\)).  
4. Return \(\{H_c,V_c,D_c,C_\Sigma\}\) and diagnostics; **do not** decide policy.

---

## 6 · Controller (Existence & Properties)
Let \(\mathcal{R}\) denote a controller acting on representations/parameters to improve coherence.

- **Contraction (abstract):** There exists a metric on controller state such that repeated application of \(\mathcal{R}\) is contractive toward a \(\tau\)‑coherent fixed point.  
- **Functoriality:** \(\mathcal{R}\) preserves TSC‑valid morphisms.  
- **Budgeting symbols:** \(\{\tau_X\}\) and a global \(\tau_{\max}\) may be tracked in proofs; no numeric values are assigned here.  
- Concrete state machines, repair policies, gauges, cadence, OOD behavior, and sampling are **operational**.

---

## 7 · Compositional Corollaries
1) **Composition:** Non‑expansive pipelines preserve coherence (with bounded tolerance accumulation).  
2) **Products:** For components \(i\) with weights \(\alpha_i>0\),
\[
H_{c,\Pi}=\prod_i H_{c,i}^{\alpha_i},\quad
V_{c,\Pi}=\prod_i V_{c,i}^{\alpha_i},\quad
D_{c,\Pi}=\prod_i D_{c,i}^{\alpha_i},\quad
C_{\Sigma,\Pi}=\Big(\prod_i C_{\Sigma,i}^{\alpha_i}\Big)^{1/(\sum_i \alpha_i)}.
\]

---

## 8 · Final‑Coalgebra Uniqueness (Sketch)
If A1–A4 hold in \(\mathfrak{Met}_\tau\) with 1‑Lipschitz morphisms, then \((C,\Delta)\) is final up to \(\tau\)‑isometry: for any \(F\)‑coalgebra \((Z,\Delta_Z)\) there exists a unique (up to \(\tau\)‑isometry) morphism
\[
u_Z : (Z,\Delta_Z) \to (C,\Delta)
\]
such that \(\Delta \circ u_Z \approx F(u_Z)\circ \Delta_Z\). Uniqueness follows from bisimilarity (A4) and the contraction of \(\mathcal{R}\).

---

## 9 · Stability Under Composition and Products
All corollaries from §7 apply; the product metric is non‑expansive, hence coherence is preserved under bounded accumulation of tolerances. (No numeric bounds are fixed by the core.)

---

## 10 · Parameter Symbols and Normalization
- \(\lambda,\mu>0\) tune similarity/transport scales; \(\varepsilon\ge 0\) regularizes \(W_1\) when needed.  
- The operational layer may optionally apply monotone **gauge** maps \(g_X\) to raw distances; such choices are **out of scope** here and must be declared operationally.

---

## 11 · Integrity and Versioning
- This file is the **canonical mathematical definition** of TSC.  
- It is **stable** (not immutable): revisions are **rare**, **versioned**, and aim for **backwards compatibility**.  
- Later layers (operational specs, instructions, implementations) **must not redefine the axioms or metrics** specified here.  
- All **operational constants** (e.g., pass thresholds \(\Theta\), CI levels \(\delta\), bootstrap sizes \(B\), cadence bounds, gauge parameters) are **out of scope** and must be declared/audited by the operational layer.

---

*(End of File — TSC Core v1.1.19, Stable Mathematical Core)*
