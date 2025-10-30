# Consciousness — a TSC (Triadic Self‑Coherence) exemplar
*Version:* examples v2.1.0 • aligns with **spec/tsc-core.md v2.0.0** and **spec/tsc-operational.md v2.0.0**

> **What this file is.** A **didactic, philosophy‑first** demonstration that treats a conscious event as one phenomenon ≡ articulated triadically as **H (pattern)**, **V (relation)**, **D (process)** and then asks a single question: *do these three articulations describe one coherent event?*  
> **What this file is not.** Not a theory that “explains consciousness,” not a replacement for empirical science, not a commitment to internal representations. It is a **consistency check** across three inseparable dimensions of one event.

---

## 0) Coherence‑first stance (recognition, not assumption)

- **Given:** There is cohering (≡). Any event we care about already articulates as **H/V/D**.  
- **Task:** Recognize that triadic articulation and **measure** whether the articulations **cohere** (no privileged dimension; full S₃ role symmetry).  
- **Outcome:** A single score **C_Σ ∈ [0,1]** summarizing dimensional consistency, plus diagnostics showing where and why coherence is lost.

---

## 1) Phenomenon and articulation

**Phenomenon:** brief masked letter perception with report (toy paradigm). Each *trial* is a conscious event candidate.

- **H (pattern / cohered):** compact neural features per trial (stable pattern in measurement space).  
- **V (relation / coherer):** phenomenal distinctions per trial (clarity, location, confidence) as *relational structure* among trials (similar/different).  
- **D (process / cohering):** the task protocol as unfolding process (masking, SOA, prompt, report), including dispositions to act (button press, reaction time).

> **S₃ note.** We pick this articulation for pedagogy. Any **permutation of {H,V,D}** is an *equally valid* articulation of the same event; **C_Σ** must be invariant to relabeling (§4).

---

## 2) TSC block (YAML) — toy observations, ensemble, expectations

```yaml
tsc:
  version: "2.0.0"
  phenomenon: "Masked letter perception with report (toy)"
  identity: "consciousness/toy/masked-letter-v1"
  articulation:
    H:
      description: "Neural-pattern summary per trial (unitless, normalized)"
      features: ["feat1", "feat2", "feat3"]  # placeholders for e.g., bandpower, late positivity, synchrony
      metric: "cosine"                       # intra-H comparisons
    V:
      description: "Phenomenal distinctions per trial (reportable structure)"
      features: ["clarity", "locationL", "confidence"]  # minimal, extensible
      metric: "euclidean"                    # intra-V comparisons
    D:
      description: "Process features per trial (protocol & dispositions)"
      features: ["mask", "soa_ms", "rt_ms", "reported"] # mask∈{0,1}; reported∈{0,1}
      metric: "scaled-euclidean"
  observations:
    # 12 toy trials with gentle structure: clearer → stronger pattern → more reports, faster RTs
    O_H:
      - {id: t01, feat1: 0.78, feat2: 0.64, feat3: 0.70}
      - {id: t02, feat1: 0.12, feat2: 0.18, feat3: 0.20}
      - {id: t03, feat1: 0.81, feat2: 0.66, feat3: 0.73}
      - {id: t04, feat1: 0.32, feat2: 0.28, feat3: 0.30}
      - {id: t05, feat1: 0.75, feat2: 0.61, feat3: 0.68}
      - {id: t06, feat1: 0.15, feat2: 0.22, feat3: 0.21}
      - {id: t07, feat1: 0.70, feat2: 0.58, feat3: 0.63}
      - {id: t08, feat1: 0.18, feat2: 0.20, feat3: 0.19}
      - {id: t09, feat1: 0.73, feat2: 0.59, feat3: 0.66}
      - {id: t10, feat1: 0.28, feat2: 0.25, feat3: 0.27}
      - {id: t11, feat1: 0.69, feat2: 0.55, feat3: 0.61}
      - {id: t12, feat1: 0.24, feat2: 0.23, feat3: 0.25}
    O_V:
      - {id: t01, clarity: 0.84, locationL: 0.0, confidence: 0.82}
      - {id: t02, clarity: 0.18, locationL: 0.0, confidence: 0.22}
      - {id: t03, clarity: 0.86, locationL: 0.0, confidence: 0.85}
      - {id: t04, clarity: 0.32, locationL: 0.0, confidence: 0.35}
      - {id: t05, clarity: 0.80, locationL: 0.0, confidence: 0.78}
      - {id: t06, clarity: 0.22, locationL: 0.0, confidence: 0.24}
      - {id: t07, clarity: 0.76, locationL: 0.0, confidence: 0.74}
      - {id: t08, clarity: 0.20, locationL: 0.0, confidence: 0.21}
      - {id: t09, clarity: 0.79, locationL: 0.0, confidence: 0.77}
      - {id: t10, clarity: 0.28, locationL: 0.0, confidence: 0.29}
      - {id: t11, clarity: 0.72, locationL: 0.0, confidence: 0.70}
      - {id: t12, clarity: 0.26, locationL: 0.0, confidence: 0.27}
    O_D:
      - {id: t01, mask: 0, soa_ms: 80,  rt_ms: 410, reported: 1}
      - {id: t02, mask: 1, soa_ms: 20,  rt_ms: 720, reported: 0}
      - {id: t03, mask: 0, soa_ms: 80,  rt_ms: 395, reported: 1}
      - {id: t04, mask: 1, soa_ms: 30,  rt_ms: 640, reported: 0}
      - {id: t05, mask: 0, soa_ms: 70,  rt_ms: 420, reported: 1}
      - {id: t06, mask: 1, soa_ms: 20,  rt_ms: 690, reported: 0}
      - {id: t07, mask: 0, soa_ms: 60,  rt_ms: 455, reported: 1}
      - {id: t08, mask: 1, soa_ms: 20,  rt_ms: 710, reported: 0}
      - {id: t09, mask: 0, soa_ms: 60,  rt_ms: 430, reported: 1}
      - {id: t10, mask: 1, soa_ms: 30,  rt_ms: 620, reported: 0}
      - {id: t11, mask: 0, soa_ms: 60,  rt_ms: 470, reported: 1}
      - {id: t12, mask: 1, soa_ms: 25,  rt_ms: 650, reported: 0}
  summaries:
    H: ["pairwise-distance-matrix", "stability-index"]   # any stable, S₃-neutral summaries
    V: ["pairwise-distance-matrix"]
    D: ["transition-coherence", "rt-distribution"]
  aligners:
    HV:
      family: "entropic-ot"
      epsilon: [0.01, 0.05, 0.10]
      costs: ["cosine", "euclidean"]
      seeds: [0, 1, 2]
    HD:
      family: "entropic-ot"
      epsilon: [0.05]
      costs: ["cosine"]
      seeds: [0, 1]
    VD:
      family: "entropic-ot"
      epsilon: [0.05]
      costs: ["euclidean"]
      seeds: [0, 1]
  thresholds:
    floors: {nu_min: 1.0e-3, H_min: 0.10, L_min: 1.0e-3, nu_min_D: 1.0e-4, H_min_D: 0.05}
    Theta: 0.80
  expectation:
    # Indicative values for this toy (band ±0.02)
    H_c: 0.92
    V_c: 0.91
    D_c: 0.94
    C_sigma: 0.923
  diagnostics:
    permutation_invariance: true     # C_Σ invariant under {H,V,D} relabeling
    scale_sweep: "stable"            # coarse/fine-graining within band
    witness_swap: "stable"           # alternate summaries preserve verdict
