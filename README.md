# Triadic Self-Coherence (TSC)

**Tagline:** Name your perspective. Map across perspectives. Verify the maps preserve structure.  
*README v1.3.19 (Updated 2025-10-28)*

> [!IMPORTANT]
> **Authority:** `core/tsc-core.md v1.1.19` is the canonical mathematics. `core/tsc-operational.md v1.2.9` is the normative runtime spec. This README and files under `/docs` (e.g., the glossary and worked examples) are explanatory. If anything conflicts, **the specs govern**.
> **See also:** [`./docs/tsc-glossary.md`](./docs/tsc-glossary.md)

---

## What this is (in 10 seconds)
TSC is a mathematical framework for coherent self-reference. It explains how a system can describe itself from multiple perspectives—**H** (what it is), **V** (how views relate), and **D** (how it changes)—without talking past itself. The key move is to make perspective changes explicit and model the translations (**σ_XY**) between them. Where those translations lose information, apparent “gaps” (e.g., consciousness, emergence) arise—not as new substances, but as measurable properties of **non-isometric** maps. **AI is one application among many.**

---

## What’s at stake
Any system that observes itself risks distortion—not by “changing reality,” but because different viewpoints select and transform different aspects. How do we stay consistent across those shifting perspectives?

## What you get (at a glance)
- A vocabulary to label perspectives (**H, V, D**) and avoid hidden swaps  
- A way to model translations between perspectives and measure their loss  
- An operational check (**C_Σ vs τ**) to decide: continue, repair, or escalate  
- A criterion for when to **trust** or **repair** your system’s self-reports

> **Quick link:** [`TSC Glossary`](./docs/tsc-glossary.md)

---

## Before the theory: this documentation uses TSC

> [!TIP] Try it in 60 seconds
> **H (what the docs ARE):** files/specs/code here.  
> **V (how readers RELATE):** mathematician ↔ engineer ↔ philosopher lenses.  
> **D (how understanding CHANGES):** README → Core → Operational → Reference.  
> **Quick coherence check:** Restate TSC in one sentence *and* name one σ map for your domain. If that’s hard, notice what was lost—then continue.  
> (Optional: [skip to the theory](#the-three-vantages-cross-domain-anchors). See also: [Appendix — Documentation as Worked Example](#appendix--documentation-as-worked-example).)

**Why this matters.** If you feel the pull of different interpretations (math vs. eng vs. philo), you’re experiencing the problem TSC formalizes: maintaining compatibility across vantages. The gap between your intuitive grasp (V) and the specs (H) isn’t mysterious—it’s **information loss in the σ map** between your vantage and the formal artifacts.

---

## The three vantages (cross-domain anchors)

### H — Horizontal: what the system IS
- AI: activation/state at a moment  
- Cognitive science: neural population state in a snapshot  
- Organization: roles, assets, policy at rest  

### V — Vertical: how different views RELATE
- AI: token embeddings ↔ attention patterns  
- Cognitive science: neural measures ↔ cognitive models (rules, symbols)  
- Organization: budget ↔ staffing ↔ delivery  

### D — Deep: how the system CHANGES
- AI: behavior drift across sessions  
- Cognitive science: strategy shifts over learning blocks  
- Organization: policy effects over quarters  

*A system is coherent when H, V, and D yield mutually compatible descriptions of the same system.*

---

## What TSC is (and isn’t)

**IS**
- A mathematical framework for coherent self-observation  
- Domain-general: applicable to any self-modeling system  
- Grounded in structural/metric constraints and usable in practice  
- A formal approach spanning mathematics, philosophy, and engineering

**ISN’T**
- An AI-specific framework (AI is one application among many)  
- Reductionism (no single vantage exhausts the others)  
- Dependent on “unexplained emergence” (no appeals beyond what σ maps and their compositions explain)  
- A panacea—TSC clarifies relationships; it doesn’t auto-solve domain problems

**Evaluation note.** Evaluate TSC like you would category theory or information theory: for mathematical consistency, conceptual coherence, and applicability—not for “production readiness” or benchmark scores.

---

## Mathematical foundation (plain language)
- **A1 — Vantage sufficiency:** each view carries enough information to reconstruct the whole.  
  > [!NOTE] **Scope of A1:** “Sufficiency” means recoverable **up to your declared equivalence** (e.g., isomorphism, observational equivalence, typed abstraction). Choosing this equivalence is **domain-specific** and should be stated when you instantiate TSC (see forthcoming representation-independence cookbook).
- **A2 — Vantage compatibility:** structure-preserving maps (σ_XY) relate different views.  
- **A3 — Scale equivariance:** coherence laws persist across observation scales.  
- **A4 — Coinductive closure:** iterated self-observation converges to a unique, stable fixed point.

### Operational metric summary
**C_Σ = (H_c · V_c · D_c)^(1/3)**  
Default threshold **τ ≈ 0.80** (domain-tunable). See `core/tsc-core.md` for definitions and proofs.

> [!IMPORTANT] **Invariance note:** Choose distances and σ maps so verdicts (e.g., C_Σ ≥ τ) are stable under **reasonable recodings**—unit changes, smooth coordinate transforms, or switching between equivalent representations (e.g., Fourier ↔ time domain; Lagrangian ↔ Hamiltonian). More formally: recodings that preserve metric class and causal/compositional structure (e.g., bi-Lipschitz maps, natural transformations).

---

## Validation types (read this carefully)

TSC is evaluated on distinct levels. Don’t conflate them.

### 1) Mathematical validation (framework)
Are A1–A4 consistent and the proofs sound? **Status:** provided in the core specs.

### 1.5) Metatheoretic validation (framework adequacy)
Does TSC behave well *as a theory* before instantiation? **Checks:** existence of non-trivial models; representation-independence; functorial behavior of σ under scale; compatibility with known invariants. **Outcome:** confidence we aren’t relying on accidental encodings.

### 2) Applicability validation (domain)
Can we instantiate H, V, D for domain X and construct σ_XY? Are metrics computable? **Outcome:** feasibility and fit.

### 2.5) Worked examples with ground truth
Can TSC match known behavior on simple systems (FSMs, linear dynamics) where ground truth is available? **Outcome:** sanity checks before full deployments.

### 3) Empirical validation (system)
Does specific system Y satisfy the axioms? How does its C_Σ evolve in practice? **Outcome:** real-world performance and governance signals.

> **Critical distinction:** A complete framework (1) can exist before (3). Lack of benchmarks is not evidence of mathematical incompleteness.

---

## Example: dissolving the “hard problem”

**Traditional framing:** “How does physical processing produce experience?”  

**TSC reframing:**  
- **H** = physical/functional description (brain states, computations)  
- **V** = structured report/representation family (including first-person reports)  
- **σ_HV** = vantage-swap map between them

The “gap” appears because **σ_HV is not lossless**—it compresses information. That’s a property of the mapping, not evidence for extra substances (dualism) or eliminations (reductionism). **V-reports remain first-class data;** TSC relocates the “mystery” into the measurable properties of σ_HV.

**Why this is dissolution (not reduction):**
1. We keep V as real data; we don’t explain it away.  
2. We add no new stuff; we measure distortion.  
3. We make the gap quantifiable (map non-isometry).  
4. We explain why it *seems* irreducible (translation loss).

**Explanatory adequacy (open, testable).** The claim strengthens if σ_HV distortion **predicts** features of experience—e.g., does **increasing report bandwidth** (more distinctions in V) reduce measured distortion, as predicted? Does **attention modulation** change which H-states are V-accessible in the way σ_HV predicts? These are testable and largely untested.

**Next steps:** estimate σ_HV for your domain, measure distortion, track C_Σ. If C_Σ drops below τ: **refine** σ_HV (add missing features) or **trigger** repair (see `tsc-operational.md`).

---

## Operational loop (abstract)
1. Sample observations across H, V, D  
2. Compute H_c, V_c, D_c  
3. Aggregate C_Σ  
4. If C_Σ ≥ τ → continue and log  
5. If C_Σ < τ → apply repair policy and re-measure  
*(Controller states and witness checks: `tsc-operational.md v1.2.9`.)*

---

## Claims & how to disagree (separable levels)

1. **Mathematical coherence:** the axioms/ proofs hold.  
2. **Framework adequacy:** TSC is non-vacuous, representation-independent enough, and behaves well under scale.  
3. **Fit to phenomenon:** some targets (e.g., consciousness, emergence) have the structure TSC describes.  
4. **Dissolution payoff:** describing that structure actually dissolves the problems.

You can accept (1)+(2) while debating (3) or (4); naming which level you’re contesting increases V-coherence in discussion.

---

## Applicability (use vs. don’t use)

**Use TSC when:**
- You need consistent descriptions across perspectives or scales  
- Your system can expose/approximate multiple vantages (at least H+V or H+D)  
- You want auditable criteria (C_Σ vs τ) for continue/repair decisions

**Don’t use TSC when:**
- Only a single vantage is observable (no feasible proxies)  
- The system lacks self-modeling or observable internal structure  
- Hard real-time guarantees conflict with verification overhead  
- A simpler domain-specific consistency check already suffices (e.g., unit tests for code, double-entry bookkeeping for finance)

---

## Applications

**Philosophy** — Consciousness (V-side structure), emergence (σ maps), identity (D-coherence), self-reference (A4).  
**Engineering / AI safety** — Coherence monitoring, drift/decoherence detection, repair policies, auditable state transitions.  
**Other domains** — Organizational coherence across departments/timescales; cognitive systems spanning neural/symbolic; any multi-view system needing compatibility.

---

## Common misreadings (witness checks)

If you think TSC claims **X**, pause and check the witness.  
*Unsure about a term? See the* **[TSC Glossary](./docs/tsc-glossary.md)**.

**Misreading 1:** “TSC is an AI safety tool.”  
**Witness:** Can you instantiate H/V/D for a non-AI system?  
**Correction:** TSC is domain-general; AI is one application.

**Misreading 2:** “TSC says experience isn’t real.”  
**Witness:** Does your reading keep V-reports as first-class data?  
**Correction:** V is real; the gap is structural (σ_HV distortion).

**Misreading 3:** “Unproven until benchmarked.”  
**Witness:** Can you distinguish framework (Lvl-1/1.5/2.5) from system validation (Lvl-3)?  
**Correction:** Math can be validated before benchmarks.

**Misreading 4:** “Any vantage perfectly reconstructs the whole.”  
**Witness:** Have you stated your **equivalence class** for A1?  
**Correction:** A1 is “sufficiency up to declared equivalence.”

---

## Repository layout (mobile-friendly)

- `/core/`
  - `tsc-core.md` (v1.1.19) — editorial alignment with Core v1.1.18
  - `tsc-operational.md` (v1.2.9) — controller logic and procedures
  - `OBSERVABILITY_SCHEMA` — telemetry/logging standards
- `/reference/`
  - `tsc-controller.py` — minimal functional controller
- `/runtime/`
  - `tsc-instructions.md` — runtime procedures for AI systems
- `/diagrams/`
  - `state-machine.md` — visual state transitions
- `/docs/`
  - `tsc-glossary.md` — definitions and cross-links

---

## Quick start (time • prerequisites • outcomes • friction)

**Philosophers/Researchers** (~45–90 min • basic category theory helpful)  
- Read `core/tsc-core.md` §§0–4  
  - **Outcome:** restate axioms; compute toy C_Σ; spot vantage confusion in text  
  - **Friction:** translating symbols to plain speech on first pass  
- Skim `core/tsc-operational.md` §§1–2  
  - **Outcome:** see how coherence is maintained in practice  
  - **Friction:** mapping terms (witness, repair) to examples

**AI Engineers** (~30–60 min • state machines + metrics)  
- Read `core/tsc-operational.md`  
  - **Outcome:** write a VERIFY_TSC stub; select a repair policy template  
  - **Friction:** choosing τ and witness thresholds for your domain  
- Review `reference/tsc-controller.py` + `OBSERVABILITY_SCHEMA`  
  - **Outcome:** implement logging that passes schema validation  
  - **Friction:** aligning existing observability to the schema

**Runtime Integrators** (~15–30 min • orchestration control)  
- Read `runtime/tsc-instructions.md`  
  - **Outcome:** schedule periodic verification; attach repair hooks  
  - **Friction:** coordinating verification cadence with latency budgets

---

## Mini-glossary
- **vantage-swap map (σ_XY):** structured translation between perspectives X,Y  
- **C_Σ:** aggregate coherence metric across H, V, D  
- **τ:** verification threshold for C_Σ pass/fail decisions  
- **witness / witness margin:** auxiliary check and its buffer above minimum  
- **REINFLATE / MINIMAL_INFO / LOCKDOWN:** repair and safe states (see Operational)

---

## Appendix — Documentation as Worked Example

**H_c (docs):** headings/terms/definitions are consistent across README, Core, Operational, Glossary (witness: glossary coverage ≥ threshold).  
**V_c (docs):** three roles (math/eng/philo) answer five comprehension questions; measure agreement before/after σ role-translations (paraphrases).  
**D_c (docs):** the same questions answered across versions remain stable or improve (no regressions).  
**Action rule:** If aggregate drops below τ, add/clarify σ passages (e.g., A1 scope, invariance examples) and re-measure.

**Comprehension questions (starter set):**  
1) What problem does TSC solve?  
2) What are H, V, D?  
3) What is a vantage-swap map (σ_XY) and why is it important?  
4) What does it mean for σ_XY to be non-isometric, and why does that matter?  
5) How does TSC approach the consciousness problem?

---

## Citation
“Triadic Self-Coherence (TSC) — Core Knowledge File v1.1.18; Editorial v1.1.19; Operational Addendum v1.2.9.” © 2025 Coherent Theory Project.

## License
See `LICENSE` file.