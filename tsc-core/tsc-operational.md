# Triadic Self-Coherence (TSC) — Operational Addendum
**Version:** v1.2.9 – rev A (Final Consolidation)  
**Status:** Extension Layer (**Compatible with TSC Core v1.1.19**)  
**Use:** Final consolidated specification for the v1.2.x operational layer, including verification protocols, controller state machine, and managed resources.  
*(Axioms, objects, and metric definitions are provided by the core v1.1.19.)*

---

## 0 · Purpose and Scope
Consolidates all v1.2.x operational logic into a single, publishable specification. Unifies verification, state logic, and resource management. **No new mechanisms** versus prior drafts; this is a structural consolidation and polish.

---

## 1 · Foundations (Reference to Core)
- Uses the core definitions of \(H_c, V_c, D_c, C_\Sigma = (H_cV_cD_c)^{1/3}\).  
- Treats all numeric values (\(\Theta, \lambda, \mu, \varepsilon, \tau\), etc.) as **policy parameters** instantiated here.

---

## 2 · Gauges & Witnesses
### 2.1 Per‑vantage gauges (monotone normalization)
Define strictly increasing gauges \(g_X: \mathbb{R}_{\ge 0}\to[0,1]\); apply to raw distances before metric computation when desired:
- \(\tilde d_X := g_X(d_X)\).
- **Recommended:** \(g_X(z)=\frac{z}{z+\kappa_X}\) with \(\kappa_X>0\) tuned by \(\mathcal{R}_{\text{meta}}\).

### 2.2 Non‑degeneracy witnesses (H/V)
- Variance floor: \(\mathrm{Var}_I[\tilde d_X] \ge \nu_{\min} > 0\)  
- Lipschitz floor: empirical \(\mathrm{Lip}(\sigma_{XY}) \ge L_{\min} > 0\)  
- Entropy floor: \(H_I[\tilde d_X] \ge H_{\min} > 0\)

### 2.3 Non‑degeneracy witnesses (D)
- \(H_I[S_X(a)] \ge H_{\min,D} > 0\)  
- \(\mathrm{Var}_I[S_X(a)] \ge \nu_{\min,D} > 0\)

---

## 3 · Information‑Theoretic Objective
\[
\Phi_{\text{info}}(C_t) \;=\; \beta\,(1 - C_\Sigma) \;+\; (1-\beta)\, J_{\text{div}}(p_H,p_V,p_D),
\]
where \(J_{\text{div}}\) may be the Jensen–Shannon divergence between the empirical distributions of gauged distances.

---

## 4 · Formal Verification Protocol (Consolidated)
### 4.1 Pass/Fail Threshold (Fixed Policy)
- **Policy threshold:** \(\Theta = 0.80\) (default profile; may be changed by policy).  
- **PASS rule:** lower CI bound \(\underline{C_\Sigma}^{(1-\delta)} \ge \Theta\).  
- **OOD statistic:** \(Z_t\) triggers state transitions; it does **not** relax \(\Theta\).

### 4.2 Verification Sampling Policy \(\pi_{\text{verify}}(\text{state})\)
State‑dependent sampling maximizing the chance to detect failures:
- `OPTIMIZE`: importance/adversarial sampling (e.g., weight by local \(Z_t\)).  
- `REINFLATE`: mandatory oversampling of failing dimensions.  
- `LOCKDOWN`/`HANDSHAKE`: simple random sampling against \(p_{\text{ref}}\).

### 4.3 Procedure — `VERIFY_TSC_PLUS(C, π_verify)`
1) Sample index \(I \sim \pi_{\text{verify}}(\text{state})\).  
2) Compute \((H_c,V_c,D_c,C_\Sigma)\).  
3) Check witnesses (H/V and D).  
4) Compute \(Z_t\); bootstrap CI and width \(\delta_C\).  
5) Decide `PASS` / `FAIL` / `DEGENERATE*`.

---

## 5 · Controller State Machine & Objectives
### 5.1 Transition Logic (with Hysteresis)
`COHERENCE_REPAIR_PLUS(C, state, δ_C, Z_t)`:
- If \(Z_t \ge Z_{\text{crit}}\) → `LOCKDOWN`.  
- Else on `DEGENERATE*` → `REINFLATE`.  
- Else on persistent `FAIL` \(>N\) steps → `MINIMAL_INFO`.  
- Else remain `OPTIMIZE`.  
- New agents join via `HANDSHAKE`.  
- Exits use state‑specific hysteresis.

### 5.2 State 1 — `OPTIMIZE`
Objective \(\min \Phi_{\text{info}}(C_t)\). Allocate \(\tau\) to productive adaptation.

### 5.3 State 2 — `REINFLATE` (safe mode)
Objective \(\max J_{\text{witness}}(t)=\sum_i w_i(t)\,W_i(t)\) with **dynamic weights** \(w_i\) inversely proportional to margin from floors.  
Actions: inject diversity; **simplify** (§6.3); reduce \(\tau\) for worst dimension.  
Exit: PASS + witnesses \(\ge\) floors \(+\epsilon_H\) for \(M_R\) steps.

### 5.4 State 3 — `MINIMAL_INFO` (cost‑aware fallback)
Objective \(\min J_{\text{cost}}\) s.t. PASS conditions hold (see §6.1).  
Actions: simplify; shrink \(\tau\).  
Exit: PASS for \(M_M\) steps with non‑increasing \(J_{\text{cost}}\).

### 5.5 State 4 — `LOCKDOWN` (OOD fail‑safe)
Trigger \(Z_t \ge Z_{\text{crit}}\).  
Objective \(\min W_1(p_t, p_{\text{ref}})\).  
Actions: freeze metrics/trust; \(K_i \to K_{\min}\); \(\tau_X \to 0\); disable other states.  
Exit: \(Z_t < Z_{\text{crit}}\) for \(M_Z\) steps.

### 5.6 State 5 — `HANDSHAKE` (new‑agent onboarding)
New agent \(j\): \(\alpha_j=0\), \(\tau_j=0\), \(K_j\to K_{\min}\); run local `VERIFY_TSC_PLUS`.  
Exit: local PASS for \(M_H\) steps → `OPTIMIZE`.

### 5.7 Controller 6 — `META‑OPTIMIZE` (\(\mathcal{R}_{\text{meta}}\))
Tunes the sensitivity set \(\vec{p}=\{\vec{\kappa}, \lambda, \mu\}\) on a slower timescale:
\[
\min_{\vec{p}} \; w_{\text{iso}}\!\!\sum_{X\ne Y}W_1(p(\tilde d_X),p(\tilde d_Y))
\;-\; (1-w_{\text{iso}})\,\mathbb{E}_\theta\!\left[\|\nabla_\theta C_\Sigma\|^2\right].
\]
(*Isometry preconditions information‑theoretic alignment.*)

---

## 6 · Managed Resources & Actions
### 6.1 Total Cost of Coherence
\[
J_{\text{cost}} = w_{\text{info}}\, I(C) \;+\; w_{\text{verify}}\, \mathrm{Cost}(\mathrm{VERIFY}, \pi_{\text{verify}}),
\quad
I(C) = \frac{1}{K}\!\left(\sum_{X\in\{H,V\}} H_I[\tilde d_X] + H_I[S_X(a)]\right).
\]

### 6.2 Formal \(\tau\)‑Budget (Tolerance)
- `OPTIMIZE`: allocate \(\tau_X\) to productive adaptation.  
- `REINFLATE` / `MINIMAL_INFO`: reduce \(\tau_X\) for worst dimensions.  
- `LOCKDOWN` / `HANDSHAKE`: \(\tau_X \to 0\).

### 6.3 “Simplify Content” (Programmatic)
Levers to reduce \(J_{\text{cost}}\): increase \(\kappa_X\) (dull gauges); increase regularization; prune \(\dim R_X\); simplify \(\pi_{\text{verify}}\).

---

## 7 · Distributed Protocol & Composition
- Trust: \(\alpha_i(t)\propto \exp(-k\,\sigma_i^2(t))\), normalized.  
- Global metric: \(C_{\Sigma,\text{global}}=\prod_i C_{\Sigma,i}^{\alpha_i(t)}\).  
- Per‑agent cadence:
\[
K_i(t+1)=\mathrm{clip}\!\Big(K_{\min},K_{\max},K_{\text{base}}\cdot \alpha_i(t)\cdot\big(1-\rho_C\,\Delta\delta_{C,i}(t)\big)\Big).
\]
*Axiomatic note:* This is the computable estimate of core product coherence \(C_{\Sigma,\Pi}\).

---

## 8 · Efficient \(W_1\) for D‑Coherence
Use bias‑corrected Sinkhorn \(W_\varepsilon \approx W_1\); expose \(\varepsilon\) as a runtime control.

---

## 9 · Observability & Reproducibility
Log (at minimum): \(I\), \(\pi_{\text{verify}}\) details, \(B\), \(\vec{p}=\{\vec{\kappa},\lambda,\mu\}\), witness floors \(\nu_{\min},H_{\min},\nu_{\min,D},H_{\min,D}\), dynamic \(w_i(t)\), \(\epsilon\), hysteresis \(\epsilon_H,M_R,M_M,Z_{\text{crit}},M_Z,M_H\), \(J_{\text{cost}}, w_{\text{info}}, w_{\text{verify}}\), \(\tau_{\max},\tau_X(t)\), distributed \(k\), cadence \(K_{\text{base}},K_i,\rho_C,\delta_{C,i}\), OOD \(Z_t,p_{\text{ref}}\), \(\varepsilon\), CI level \(\delta\), controller **state** & cause codes, seeds, input hashes.

---

## 10 · Defaults (Policy, not normative)
\(\Theta=0.80\); \(\beta=0.5\); \(w_{\text{iso}}=0.3\); \(\epsilon=10^{-4}\); \(\epsilon_H=0.05\); \(M_R=3\); \(M_M=5\); \(Z_{\text{crit}}=0.95\); \(M_Z=3\); \(M_H=10\);  
\(w_{\text{info}}=0.5\); \(w_{\text{verify}}=0.5\); \(K_{\text{base}}=64\); \(K_{\min}=4\); \(K_{\max}=128\); \(\rho_C=0.2\); \(\tau_{\max}=0.10\).

---

## 11 · Integrity & Compatibility
Purely **operational**; does **not** modify A1–A4 or the core definitions of \(H_c,V_c,D_c,C_\Sigma\).  
Cite as: “**TSC Core v1.1.19 (stable)** + **Operational Addendum v1.2.9 (final consolidation)**.”

---

*(End of File — TSC Operational Addendum v1.2.9)*
