# Triadic Self-Coherence (TSC)

**Tagline:** Name your perspective. Map across perspectives. Verify the maps preserve structure.

*README v1.3.14 (Updated 2025-10-28)*

> [!IMPORTANT]
> This README provides orientation and intuition. Formal content is governed by the **Core Knowledge File v1.1.18**. The repo’s `tsc-core.md v1.1.19` aligns editorially; `tsc-operational.md v1.2.9` defines procedures. If this document conflicts with the specs, the specs govern.

---

## What’s at stake
Any system that observes itself risks distortion—not by “changing reality,” but because different viewpoints select and transform different aspects. How do we stay consistent across those shifting perspectives?

## What you get (at a glance)
- A vocabulary to label perspectives (**H, V, D**) and avoid hidden swaps  
- A way to model translations between perspectives and measure their loss  
- An operational check (**C_Σ vs τ**) to decide: continue, repair, or escalate  
- A criterion for when to **trust** or **repair** your system’s self-reports

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

IS
- A mathematical framework for coherent self-observation
- Applicable to any self-modeling system (not AI-specific; AI is a concrete testbed)
- Grounded in structural/metric constraints and usable in practice

ISN’T
- Reductionism (no single vantage exhausts the others)
- Dependent on “unexplained emergence” (doesn’t require emergence claims beyond what vantage-swap maps and their compositions explain)
- Tied to a single ontology (works for process, substance, or information views)
- A panacea—TSC clarifies relationships; it doesn’t auto-solve domain problems

---

## Mathematical foundation (plain language)
- A1 — Vantage sufficiency: each view carries enough information to reconstruct the whole
- A2 — Vantage compatibility: structure-preserving maps (σ_XY) relate different views
- A3 — Scale equivariance: coherence laws persist across observation scales
- A4 — Coinductive closure: iterated self-observation converges to a unique, stable fixed point

### Operational metric summary
C_Σ = (H_c · V_c · D_c)^(1/3). Default threshold τ ≈ 0.80 (domain-tunable).
For definitions, proofs, and tuning: core/tsc-core.md.

---

## Operational loop (abstract)
1. Sample observations across H, V, D
2. Compute H_c, V_c, D_c
3. Aggregate C_Σ
4. If C_Σ ≥ τ → continue and log
5. If C_Σ < τ → apply repair policy and re-measure

(Controller states and witness checks: tsc-operational.md v1.2.9)

---

## Example: dissolving the “hard problem”
Traditional framing: “How does physical processing produce experience?”

TSC reframing: H is the physical/functional description; V is the family of report/representation structures (including first-person reports); σ_HV is the vantage-swap map between them. The “gap” appears because σ_HV is not lossless (it compresses information). That’s a property of the mapping, not evidence for extra substances or eliminations. On this view, “experience” is what triadic coherence looks like when seen from V.

Do this next:
Estimate σ_HV for your domain, measure its distortion, track C_Σ over time.
If C_Σ drops below τ:
- Refine σ_HV (add missing features/representations), or
- Trigger repair (REINFLATE for witness margins, MINIMAL_INFO for complexity reduction).
See tsc-operational.md for full repair policy specification.

---

## Applicability (use vs. don’t use)

Use TSC when:
- You need consistent descriptions across multiple perspectives or scales
- Your system can expose or approximate multiple vantages (at least H+V or H+D)
- You want auditable criteria (C_Σ vs τ) for continue/repair decisions

Don’t use TSC when:
- You have only a single vantage with no feasible proxies
- The system lacks any self-modeling or observable internal structure
- You require hard real-time guarantees incompatible with verification overhead
- A simpler domain-specific consistency check already suffices

---

## Applications

Philosophy
- Consciousness — V-vantage structure of coherent self-observation
- Emergence — macro/micro relations via explicit σ maps
- Identity — D-coherence through change
- Self-reference — paradox management via coinductive closure

Engineering / AI Safety
- Continuous coherence monitoring
- Drift/decoherence/distribution-shift detection
- Repair policies and guardrails when coherence degrades
- Auditable metrics and state transitions for governance

---

## Repository layout (mobile-friendly)

- /core/
  - tsc-core.md (v1.1.19) — editorial alignment with Core v1.1.18
  - tsc-operational.md (v1.2.9) — controller logic and procedures
  - OBSERVABILITY_SCHEMA — telemetry/logging standards
- /reference/
  - tsc-controller.py — minimal functional controller
- /runtime/
  - tsc-instructions.md — runtime procedures for AI systems
- /diagrams/
  - state-machine.md — visual state transitions

---

## Quick start (time • prerequisites • outcomes • friction)

Philosophers/Researchers (~45–90 min • basic category theory helpful)
- Read core/tsc-core.md §§0–4
  Outcome: Restate axioms; compute toy C_Σ; spot vantage confusion in text
  Friction: Translating symbols to plain language on first pass
- Skim core/tsc-operational.md §§1–2
  Outcome: Describe how coherence is maintained in practice
  Friction: Mapping technical terms (witness, repair) to examples

AI Engineers (~30–60 min • state machines + metrics)
- Read core/tsc-operational.md
  Outcome: Write VERIFY_TSC stub; select repair policy template
  Friction: Choosing τ and witness thresholds for your domain
- Review reference/tsc-controller.py + OBSERVABILITY_SCHEMA
  Outcome: Implement logging that passes schema validation
  Friction: Aligning existing observability to schema requirements

Runtime Integrators (~15–30 min • orchestration control)
- Read runtime/tsc-instructions.md
  Outcome: Schedule periodic verification; attach repair hooks
  Friction: Coordinating verification cadence with latency budgets

---

## Mini-glossary
- vantage-swap map (σ_XY): structured translation between perspectives X,Y
- C_Σ: aggregate coherence metric across H, V, D
- τ: verification threshold for C_Σ pass/fail decisions
- witness: auxiliary metric validating a coherence verdict
- witness margin: minimum threshold distance for a valid witness reading
- REINFLATE: repair mode to restore witness margins (§5.3)
- MINIMAL_INFO: repair mode to reduce complexity under decoherence (§5.4)
- LOCKDOWN: fail-safe state for severe out-of-distribution conditions (§5.5)

---

## Status & roadmap
Current: Core (v1.1.18 authoritative; repo tsc-core.md v1.1.19 editorial), Operational (v1.2.9), minimal reference controller (WIP)
Planned: Additional references (JAX, Rust); case studies (LLMs, multi-agent coordination); formal verification of controller properties; empirical validation benchmarks

---

## Citation
“Triadic Self-Coherence (TSC) — Core Knowledge File v1.1.18; Editorial v1.1.19; Operational Addendum v1.2.9.” © 2025 Coherent Theory Project.

## License
See LICENSE file.