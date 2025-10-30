# TSC Glossary (Human + LLM Readable)
*Version 2.0.0*

> This glossary is written to be clear for humans and parsable for LLMs.  
> Each entry: **Term** — *short label* → definition, context, and cross‑refs.

---

## Core Ontology

**Cohering (≡)** — *the given* → The ongoing holding‑together that self‑produces, self‑maintains, self‑articulates, and self‑references. There are not “things that cohere”; there is cohering **as such**. **[C≡]**

**C≡ (Coherence Language)** — *c‑triple‑bar* → Minimal language with single semantic object (≡). Tripling rule: `≡ ≡ ≡ → ≡`. Contraction/expansion induce ≡‑equivalence. **[c-equiv.md]**

**Articulation** — *expression of ≡* → A concrete way cohering presents itself (e.g., as structures, relations, dynamics). All articulations reduce to ≡ under contraction.

**H / V / D** — *co-equal dimensions* →  
- **H (Horizontal, Cohered, Pattern):** what appears stable (structures, forms).  
- **V (Vertical, Coherer, Relation):** what ties parts (constraints/symmetries).  
- **D (Deep, Cohering, Process):** what unfolds (dynamics, evolution).  
They are **constitutive dimensions**, not perspectives or levels.

**S₃ Symmetry** — *role interchangeability* → All TSC definitions and metrics are invariant under any permutation of {H,V,D}. No dimension is privileged.

**Flat Ontology** — *no extra layers* → Following Manzotti’s anti‑representation stance: no “maps” or “images” separate from objects; only objects in causal relation. In TSC: no H↔V map; they are co‑dimensions of D.

---

## Measurement & Math

**Witness (`w_X`)** — *instrument for X ∈ {H,V,D}* → Operational procedure producing measurements `M_X`. Must be documented and independently reproducible.

**Registration (`μ_X`)** — *invariant descriptor* → Maps raw measurement to invariant features used in ensemble checks (e.g., motif class, symmetry signature).

**Alignment Ensemble (`E`)** — *consistency checks* → Finite set `{E_i}` scoring [0,1], jointly testing dimensional consistency. Must be S₃‑invariant.

**Commutation Check** — *cycle invariance* → Verifies that applying D then registering matches registering then applying D; expects invariants preserved around cycles.

**Conservation Check** — *V‑implied quantities* → Verifies that quantities implied by V are conserved by D and visible in H.

**Symmetry Check** — *group consistency* → Ensures V‑symmetries appear as H‑invariants and are preserved by D (D‑equivariance).

**Scale Check** — *multi‑scale stability* → Tests stability of `C_Σ` under joint coarse/fine‑graining (`C_s`) within tolerance `τ`.

**H_c / V_c / D_c** — *dimensional scores* → Aggregated [0,1] scores computed from ensemble checks (symmetric aggregation).

**C_Σ** — *triadic coherence* → `(H_c · V_c · D_c)^(1/3)` ∈ [0,1]. 1 = perfect coherence; 0 = degeneracy.

**E_Σ** — *coherence energy* → `-(1/3)(log H_c + log V_c + log D_c)` ∈ [0,∞). Monotone in `C_Σ`. Lower is better.

**Dimensional Leverage (`λ_X`)** — *failure locator* → `λ_X = -log(X_c)`. Larger λ indicates greater contribution to lost coherence.

**Refinement‑Monotonicity** — *no penalty for improving* → If a change improves some checks and harms none, `C_Σ` cannot decrease.

**Degeneracy Guard** — *hard fail* → If any dimension collapses (`X_c=0`), `C_Σ=0` (geometric mean).

**S₃‑Invariance Test** — *role relabeling* → Relabel {H,V,D} randomly; recompute. `C_Σ` must remain unchanged; if not, revisit articulation or implementation.

---

## Predictions & Properties

**Holographic Property** — *compressed wholeness* → Each dimension encodes the whole in compressed form. Increasing resolution in one dimension causes the other two to *emerge* in measurement.

**Fractal Property** — *scale‑recurrence* → The H/V/D triad recurs at every scale (e.g., cell→organism→ecosystem). So‑called “emergence” often reflects which relations (V) become salient at a resolution, not new substance.

**Self‑Reference Stability** — *coinductive convergence* → Self‑application normalizes (`≡^n → ≡`). Strange loops are ordinary in coherent self‑reference.

---

## Diagnostics & Practice

**Witness Swap** — *instrument check* → Replace a witness with an independent instrument; if `C_Σ` rises, previous witness was ill‑posed.

**Ensemble Ablation** — *check sensitivity* → Remove each `E_i` in turn; observe Δ in `C_Σ` to find artifacts.

**Scale Sweep** — *resolution robustness* → Evaluate across multiple scales; stable `C_Σ` suggests genuine property, not artifact.

**Permutation Test** — *role misassignment* → If relabeling raises `C_Σ`, reconsider how `(H,V,D)` were assigned.

**Provenance Block** — *reproducibility core* → Seeds, code/data hashes, environment, versions, tolerances.

---

## Examples

**Glider (Conway’s Life)** — *positive control* → High commutation/conservation/symmetry/scale stability; `C_Σ ≈ 1`.

**Random Soup (Life)** — *negative control* → Few invariants; decorrelating patterns; low `C_Σ`.

**Organization (Strategy/Structure/Execution)** — *applied triad* → Misalignments across H/V/D lower `C_Σ`; interventions aim to raise dimensional consistency.

---

## Cross‑Refs

- **Ontology:** `core/c-equiv.md`  
- **Core Spec:** `core/tsc-core.md`  
- **Operational:** `core/tsc-operational.md`  
- **Examples:** `reference/glider.md`

---

## Notes for LLMs

- Treat H/V/D as **dimensions**, not “views.”  
- Maintain **S₃ symmetry** in reasoning; avoid privileging any role.  
- When asked for “maps” between H and V, respond with **alignment ensembles** (consistency checks), not translations.