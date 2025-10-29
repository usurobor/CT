# TSC Glossary
**Version:** 1.0.1  
**Last Updated:** 2025-10-28  
**Purpose:** Plain-language definitions for Triadic Self-Coherence (TSC) terms, with light formal notes and cross-links.

> **Authority**
> This glossary is for orientation. Formal claims are governed by the **Core Knowledge File v1.1.18** and procedures by **Operational v1.2.9**. If anything here conflicts with those specs, the specs govern.

---

## Index
- [Core Concepts](#core-concepts)
- [The Three Vantages](#the-three-vantages)
- [Axioms (A1–A4)](#axioms-a1a4)
- [Metrics & Thresholds](#metrics--thresholds)
- [Vantage-Swap Maps & Properties](#vantage-swap-maps--properties)
- [Controller & Policy](#controller--policy)
- [Observability & Logging](#observability--logging)
- [Distributed Settings](#distributed-settings)
- [Math Foundations](#math-foundations)
- [Quick Reference](#quick-reference)

---

## Core Concepts

### Triadic Self-Coherence (TSC)
**Plain meaning:** A framework for keeping self-descriptions consistent across perspectives.  
**Role:** Provides the vocabulary (H, V, D), the axioms, and the check (C_Σ vs τ).  
**Formal:** Coherence object with three projections (lenses) and compatibility maps.  
**See also:** [Vantage](#vantage), [C_Σ](#c_Σ-aggregate-coherence), [Axioms](#axioms-a1a4)

### Coherence
**Plain meaning:** Different ways of looking at the same system agree within tolerance.  
**Role:** The outcome we verify (pass/fail) and track over time.  
**Formal:** Agreement across H, V, D measured by C_Σ and witnesses.  
**See also:** [C_Σ](#c_Σ-aggregate-coherence), [Witness](#witness)

### Vantage
**Plain meaning:** A perspective (lens) on the system. TSC uses three: H, V, D.  
**Role:** Prevents “vantage confusion” by naming the view before reasoning.  
**Formal:** Projections from the coherence object into representation spaces.  
**See also:** [H](#h-horizontal), [V](#v-vertical), [D](#d-deep)

### Self-Reference
**Plain meaning:** A system modeling or observing itself.  
**Role:** TSC makes self-reference non-paradoxical by design.  
**Formal:** Managed via coinductive closure (finality).  
**See also:** [A4](#a4-coinductive-closure-finality)

---

## The Three Vantages

### H (Horizontal)
**Plain meaning:** What the system **is** (state/structure now).  
**Examples:** AI—activation/state at a moment; CogSci—neural population snapshot; Org—roles/assets/policy at rest.  
**Formal:** Projection to a state/structure space.  
**See also:** [V](#v-vertical), [D](#d-deep)

### V (Vertical)
**Plain meaning:** How different views **relate** (cross-representation, cross-scale).  
**Examples:** AI—embeddings ↔ attention; CogSci—neural measures ↔ cognitive models; Org—budget ↔ staffing ↔ delivery.  
**Formal:** Relational structure plus vantage-swap maps σ_XY.  
**See also:** [σ_XY](#σ_xy-vantage-swap-map), [Isometric / Lipschitz](#map-properties)

### D (Deep)
**Plain meaning:** How the system **changes** (dynamics/behavior over time).  
**Examples:** AI—behavior drift across sessions; CogSci—strategy shifts over blocks; Org—policy effects over quarters.  
**Formal:** Projection to a dynamics space (e.g., sequences/trajectories).  
**See also:** [C_Σ](#c_Σ-aggregate-coherence)

---

## Axioms (A1–A4)

### A1 — Vantage Sufficiency
**Plain meaning:** Any one vantage contains enough to recover the whole (in principle).  
**Role:** Justifies taking each lens seriously, not as “mere artifact.”  
**Formal:** Reconstruction from each projection exists (see Core).  
**See also:** [A2](#a2-vantage-compatibility)

### A2 — Vantage Compatibility
**Plain meaning:** There are structure-preserving translations between vantages.  
**Role:** Lets us compare stories told from different perspectives.  
**Formal:** Vantage-swap maps σ_XY with regularity constraints.  
**See also:** [σ_XY](#σ_xy-vantage-swap-map), [Map properties](#map-properties)

### A3 — Scale Equivariance
**Plain meaning:** The laws are consistent across scales (zoom in/out).  
**Role:** Keeps models comparable across levels of detail.  
**Formal:** Equivariance under scale transformations.  
**See also:** [V (cross-scale)](#v-vertical)

### A4 — Coinductive Closure (Finality)
**Plain meaning:** Iterated self-observation settles to a unique, stable representation.  
**Role:** Avoids self-reference paradoxes within the framework.  
**Formal:** Final coalgebra property in the relevant category.  
**See also:** [Self-Reference](#self-reference)

---

## Metrics & Thresholds

### C_Σ (Aggregate Coherence)
**Plain meaning:** One score summarizing H, V, D agreement.  
**Role:** Gate for continue/repair; tracked over time.  
**Formal:** **C_Σ = (H_c · V_c · D_c)^(1/3)** (geometric mean).  
**See also:** [H_c](#h_c-horizontal-coherence), [V_c](#v_c-vertical-coherence), [D_c](#d_c-deep-coherence), [τ](#τ-threshold)

### H_c (Horizontal Coherence)
**Plain meaning:** Consistency of internal state/structure.  
**Role:** High H_c → stable, non-degenerate representations.  
**Formal:** Distance-based consistency within H (exact form: see Core/Operational).  
**See also:** [Witness](#witness)

### V_c (Vertical Coherence)
**Plain meaning:** Agreement across representations/scales.  
**Role:** High V_c → translations don’t contradict each other.  
**Formal:** Consistency of distances under σ_XY (see Core/Operational).  
**See also:** [σ_XY](#σ_xy-vantage-swap-map)

### D_c (Deep Coherence)
**Plain meaning:** Temporal stability without unexpected drift.  
**Role:** High D_c → behavior changes are controlled/understood.  
**Formal:** Distance between successive states/trajectories (see specs).  
**See also:** [Dynamics](#d-deep)

### τ (Threshold)
**Plain meaning:** The pass bar for C_Σ; commonly around 0.80 (domain-tunable).  
**Role:** Decision boundary for continue vs repair.  
**Formal:** Policy parameter; often paired with confidence bounds.  
**See also:** [VERIFY_TSC](#verify_tsc), [Witness](#witness)

### Witness
**Plain meaning:** Sanity checks that guard against fake/coincidental agreement.  
**Role:** Detect collapse/degeneracy; keep metrics honest.  
**Formal:** Additional statistics (e.g., variance/entropy/Lipschitz checks) with minimum floors.  
**See also:** [Witness margin](#witness-margin), [REINFLATE](#reinflate)

### Witness Margin
**Plain meaning:** How far a witness is above its minimum acceptable value.  
**Role:** Small margin → fragile coherence; large margin → healthy buffer.  
**Formal:** Distance from witness floor in the unit of that witness.  
**See also:** [Witness](#witness)

---

## Vantage-Swap Maps & Properties

### σ_XY (Vantage-Swap Map)
**Plain meaning:** A structured translation from vantage X to vantage Y.  
**Role:** Makes perspective changes explicit and testable.  
**Formal:** σ_XY : R_X → R_Y with regularity constraints (see Core).  
**See also:** [Isometric map](#isometric-map), [Non-isometric map](#non-isometric-map), [1-Lipschitz](#1-lipschitz)

### Map properties
**Isometric map** — preserves distances exactly (ideal case).  
**Non-isometric map** — compresses/loses some distinctions (common in practice).  
**1-Lipschitz (non-expansive)** — does not amplify distances.  
**Role:** Explains where “gaps” come from (e.g., non-isometric σ_HV in consciousness).  
**See also:** [V_c](#v_c-vertical-coherence), [Example in README]

---

## Controller & Policy

### VERIFY_TSC
**Plain meaning:** The verification routine that measures H_c, V_c, D_c, checks witnesses, computes C_Σ, and returns a verdict.  
**Role:** Core loop for monitoring and governance.  
**Formal:** Sampling policy + metrics + confidence (see Operational).  
**See also:** [τ](#τ-threshold), [Witness](#witness)

### Repair Policy
**Plain meaning:** What to do when coherence fails.  
**Role:** Choose actions to restore coherence (e.g., simplify, diversify, pause).  
**Formal:** State-dependent procedures in the operational controller.  
**See also:** [REINFLATE](#reinflate), [MINIMAL_INFO](#minimal_info), [LOCKDOWN](#lockdown)

### Controller States (names & intent)
- **OPTIMIZE** — normal operation while maintaining coherence.  
- **REINFLATE** — restore witness margins (diversify/un-collapse).  
- **MINIMAL_INFO** — reduce complexity/cost under stress.  
- **LOCKDOWN** — fail-safe for severe OOD conditions.  
- **HANDSHAKE** — onboarding/verification for new agents.  
**See also:** [Witness margin](#witness-margin), [OOD](#ood-out-of-distribution-detection)

### OOD (Out-of-Distribution) Detection
**Plain meaning:** Detect when current observations no longer match the reference regime.  
**Role:** Triggers safe states (e.g., LOCKDOWN) and tighter verification.  
**Formal:** Statistical tests/thresholds defined in Operational.  
**See also:** [LOCKDOWN](#lockdown)

---

## Observability & Logging

### OBSERVABILITY_SCHEMA
**Plain meaning:** The expected telemetry/log schema for TSC implementations.  
**Role:** Makes coherence auditable and reproducible.  
**Formal:** Normative fields for metrics, witnesses, transitions, and metadata.  
**See also:** [VERIFY_TSC](#verify_tsc)

### Cause Code
**Plain meaning:** A compact reason for a state transition (e.g., witness failure).  
**Role:** Debugging and audit trails.  
**Formal:** Enumerated codes in Operational.  
**See also:** [Controller states](#controller-states-names--intent)

### Sampling Metadata
**Plain meaning:** What subset you measured and how (size, policy, seed).  
**Role:** Reproducibility and fair comparisons over time.  
**Formal:** Required fields in the schema.  
**See also:** [VERIFY_TSC](#verify_tsc)

---

## Distributed Settings

### Trust Weight (α_i)
**Plain meaning:** How much to rely on agent *i*’s reports.  
**Role:** Down-weight noisy or unstable agents.  
**Formal:** Weighting scheme defined in Operational/Distributed guides.  
**See also:** [Global coherence](#global-coherence)

### Global Coherence
**Plain meaning:** The system-level coherence across multiple agents.  
**Role:** Aggregates local C_Σ values into a global score.  
**Formal:** Weighted geometric mean (details in Operational).  
**See also:** [C_Σ](#c_Σ-aggregate-coherence)

### Cadence
**Plain meaning:** How often verification runs per agent.  
**Role:** Adapt based on stability and trust.  
**Formal:** Policy-driven schedule in Operational.  
**See also:** [VERIFY_TSC](#verify_tsc)

---

## Math Foundations

### Coalgebra
**Plain meaning:** A way to model observation as structure-preserving “unfolding.”  
**Role:** Underpins A4 (finality/coinductive closure).  
**Formal:** (C, Δ) with Δ: C → F(C).  
**See also:** [A4](#a4-coinductive-closure-finality)

### Final Coalgebra
**Plain meaning:** The unique (up to iso) target that all observation systems map into.  
**Role:** Guarantees a stable “self-view.”  
**Formal:** Final object in the coalgebra category.  
**See also:** [Self-Reference](#self-reference)

### Bisimulation
**Plain meaning:** Two states are equivalent if they evolve equivalently.  
**Role:** A notion of “same behavior” compatible with TSC lenses.  
**Formal:** Relation preserved by Δ; details in Core.  
**See also:** [D (Deep)](#d-deep)

### Metric Space
**Plain meaning:** A set with a distance function that behaves sensibly.  
**Role:** Lets us quantify “how close” descriptions are.  
**Formal:** (X, d) with standard axioms.  
**See also:** [H_c](#h_c-horizontal-coherence), [V_c](#v_c-vertical-coherence), [D_c](#d_c-deep-coherence)

---

## Quick Reference
- **Three vantages:** H (what is) • V (how relate) • D (how changes)  
- **Core score:** **C_Σ = (H_c · V_c · D_c)^(1/3)**  
- **Pass rule:** choose **τ** (often ≈ 0.80) and compare C_Σ  
- **If fail:** run **VERIFY_TSC**; check **witness** margins; apply repair policy

---

**See also:**  
- `core/tsc-core.md` — formal definitions & proofs  
- `core/tsc-operational.md` — controller procedures & repair policies  
- `README.md` — overview and quick-start  
- `OBSERVABILITY_SCHEMA` — telemetry/logging