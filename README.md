# Coherent Theory (CT)
### Triadic Self-Coherence Framework

---

## 🔹 Purpose
Coherent Theory (CT) defines a rigorous framework for **stability, alignment, and self-verification** in intelligent systems.  
It introduces **Triadic Self-Coherence (TSC)** — a mathematical and operational structure that ensures systems remain internally consistent and can recover from incoherence.

This repository contains:
- The **immutable mathematical foundation** (`tsc-core.md`, v1.1.19)  
- The **formal operational layer** (`tsc-operational.md`, v1.2.9)  
- Supporting observability, compliance, runtime, and reference materials for implementation and audit

---

## 🔹 Core Concepts

| Concept | Description |
|----------|--------------|
| **Triadic Axioms (A1–A4)** | Define coherence across Horizontal (H), Vertical (V), and Deep (D) vantages. |
| **Coherence Metric** | \( C_\Sigma = (H_c V_c D_c)^{1/3} \); system passes if \( C_\Sigma \ge \Theta = 0.80 \). |
| **Lyapunov Candidate** | \( \Phi_{\text{info}} = \beta(1 - C_\Sigma) + (1 - \beta)J_{\text{div}}(p_H,p_V,p_D) \). |
| **Controller States** | `OPTIMIZE`, `REINFLATE`, `MINIMAL_INFO`, `LOCKDOWN`, `HANDSHAKE`, and `META-OPTIMIZE`. |
| **Verification Policy** | State-dependent sampling policy \( \pi_{\text{verify}} \) maximizing probability of detecting coherence failure. |
| **τ-Budget** | Controller-managed tolerance for permissible drift. |
| **J_cost** | Total cost of coherence: information rate + verification cost. |

---

## 🔹 Repository Structure, Usage, and Versioning

```text
/
├── CHANGELOG                  # Version history and release notes
├── LICENSE                    # License terms
├── README.md                  # This file
│
├── diagrams/
│   └── state-machine.md       # Controller state-machine diagram (Mermaid)
│
├── reference/
│   └── tsc-controller.py      # Reference controller implementation
│
├── runtime/
│   └── tsc-instructions.md    # Runtime / GPT-level system instructions
│
└── tsc-core/                  # Normative specification layer
    ├── OBSERVABILITY_SCHEMA.yaml   # Normative schema for telemetry and logs
    ├── SPEC-COMPLIANCE.md         # Compliance and audit checklist
    ├── tsc-core.md                # Immutable mathematical foundation (v1.1.19)
    ├── tsc-core.pdf               # Portable document version of the core spec
    └── tsc-operational.md         # Operational Addendum (v1.2.9, final consolidation)

─────────────────────────────────────────────────────────────────────────────
USAGE GUIDE
─────────────────────────────────────────────────────────────────────────────

FOR RESEARCHERS:
  • Read tsc-core/tsc-core.md for the formal axioms and metrics.
  • Study tsc-core/tsc-operational.md for controller logic and coherence guarantees.

FOR DEVELOPERS:
  • Use reference/tsc-controller.py as a minimal working implementation.
  • Validate logs against OBSERVABILITY_SCHEMA.yaml.
  • Confirm compliance with SPEC-COMPLIANCE.md.

FOR RUNTIME SYSTEMS / GPT INTEGRATIONS:
  • Apply configuration and runtime procedures from runtime/tsc-instructions.md
    to maintain coherence.

FOR AUDITORS:
  • Review all normative files under /tsc-core/.
  • Validate observability output and controller behavior per v1.2.9.

─────────────────────────────────────────────────────────────────────────────
VERSIONING
─────────────────────────────────────────────────────────────────────────────

Component                                   Version     Status      Description
─────────────────────────────────────────────────────────────────────────────
Core Spec (tsc-core.md)                     v1.1.19     Immutable   Defines axioms, metrics, and coherence invariants.
Operational Addendum (tsc-operational.md)   v1.2.9      Final       Specifies controller logic, verification, and runtime behavior.
Observability & Compliance                  v1.2.9      Stable      Normative schema and audit checklist.

─────────────────────────────────────────────────────────────────────────────
CITATION
─────────────────────────────────────────────────────────────────────────────

“Triadic Self-Coherence (TSC) — Core Knowledge File v1.1.19 and Operational
Addendum v1.2.9.” © 2025 Coherent Theory Project. All rights reserved.

─────────────────────────────────────────────────────────────────────────────
LICENSE
─────────────────────────────────────────────────────────────────────────────

Distributed under the terms described in the LICENSE file.

─────────────────────────────────────────────────────────────────────────────
NOTES
─────────────────────────────────────────────────────────────────────────────

• v1.1.19 defines what coherence is — the immutable mathematical law.
• v1.2.9 defines how coherence is maintained and verified — the operational law.
Together they represent the complete, publication-ready specification of the
Triadic Self-Coherence framework.
