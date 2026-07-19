# Measuring the Legacies of State Coordination

## Trade Liberalization, Sectoral Support Structures, and Heterogeneous Adjustment in China's WTO Accession

**Wenwen (Celine) Zhang**
Initial methodological note for discussion
July 2026 — companion design to the South Korea (1987) note, April 2026

---

## 1. Research question

This project asks why some sectors broadened firm entry, patenting, and competitive diffusion after China's accession to the WTO (December 11, 2001), while others became more concentrated among pre-existing incumbents. I use WTO accession — and the associated tariff reductions, quota removals, and market-access commitments — as a common trade-liberalization shock, and ask whether post-accession sectoral outcomes depended on the organizational support structures that sectors had already accumulated under pre-accession industrial policy.

This is the same sequencing question as the companion Korea note, applied to a different kind of political-economic opening: not democratization, but external trade liberalization under a binding multilateral commitment. Liberalization does not act on a blank institutional slate. It interacts with pre-existing state capacity, financing relationships, and sector-coordination mechanisms built up in the pre-accession period. The empirical challenge, as before, is to measure those inherited structures directly rather than through expenditure proxies.

## 2. Competing mechanisms

**Capacity-building mechanism.** Pre-accession industrial policy may have created durable coordination infrastructure — joint-venture technology-transfer channels, financing relationships with state banks, R&D mandates, supplier networks. Under this mechanism, WTO-driven exposure to international competition activates these structures: firms use inherited coordination advantages to adapt, upgrade, and diffuse innovation, and entry broadens as the sector professionalizes under competitive pressure.

**Incumbent-entrenchment mechanism.** Alternatively, pre-accession support may have created narrow, firm-specific advantages — approved-producer status, joint-venture quotas, preferential credit, investment-approval privileges. Under this mechanism, liberalization does not level the field. Firms holding these pre-existing privileges use them to consolidate as tariff walls fall, converting formal trade protection into informal regulatory protection (investment-approval barriers, JV-partner gatekeeping) that keeps new entry and innovation concentrated among the same incumbents.

As with the Korea design, the goal is not to ask whether WTO accession raised entry or innovation on average, but whether inherited state support changed the *distribution* of post-accession adjustment across sectors and firms.

## 3. Measurement: State Support Index

The treatment variable is unchanged in form from the Korea design: a sector-level, source-traceable **State Support Index** built from archival policy materials — industrial plans, ministry orders, five-year-plan sectoral chapters, and investment-approval regulations — coded along four dimensions: **persistence, specificity, network breadth, allocation**.

$$\bar{C}_{sd} = \frac{1}{|\mathcal{T}_0|}\sum_{t \in \mathcal{T}_0} C_{std}, \qquad \mathcal{T}_0 = \{t : t < 2001\}$$

$$S_s = \sum_{d \in D} w_d \, \tilde{C}_{sd}, \qquad \tilde{C}_{sd} = \frac{\bar{C}_{sd} - \mu_d}{\sigma_d}$$

**Critical constraint carried over from the pilot coding done to date:** every passage used to construct $\bar{C}_{sd}$ must predate WTO accession (December 11, 2001). The automobile-sector passages coded on 2026-07-19 from the 2004 *Automotive Industry Development Policy* (State Council/NDRC Order No. 8) **cannot serve as treatment-period evidence** — that document postdates accession and is better treated as a *post-treatment policy response* (see Section 6). The correct pre-treatment source for the automobile sector is the original 1994 *Automotive Industry Policy* (国务院关于印发汽车工业产业政策的通知, State Planning Commission, July 1994), which needs to be located and coded from scratch. Other sectors' pre-2001 sources — Eighth Five-Year Plan (1991–1995) and Ninth Five-Year Plan (1996–2000) sectoral chapters, ministry-level industrial catalogs — should be prioritized for the same reason.

$w_d$ should be fixed **before** any outcome data is examined, and that fact should be recorded explicitly (date and version) in the source log, to preempt any concern about post-hoc weight selection.

**Coder-blinding protocol (new addition, applies to both this note and the Korea note):** passages are coded for $\mathcal{T}_0$ using only the archival text and the fixed rubric, without reference to any post-accession outcome data for that sector. This should be stated explicitly in `docs/validation_plan.md` and logged per-run in the prompt log.

## 4. Empirical design

Unlike Korea's single-date political transition, WTO accession created a **staggered, sector-specific liberalization schedule**: tariff bindings, quota removals, and market-access commitments phased in on different timelines by product category (e.g., automobiles had a multi-year tariff phase-down through 2006 and a longer path to JV-restriction relaxation; textiles and apparel saw the most consequential shock at the 2005 phase-out of the Multi-Fibre Arrangement quota system; telecom and financial services followed separate, longer schedules). This is a genuinely staggered-adoption design, not a single common shock — structurally the same estimation problem as the Compute Gatekeeping project's multi-date tier changes, and the same problem Callaway & Sant'Anna (2021) and Sun & Abraham (2021) were built to solve.

**Baseline specification (single accession date, for direct comparability with the Korea design):**

$$Y_{ust} = \alpha_u + \lambda_t + \sum_{k \neq -1} \beta_k \left(D_t^k \times \tilde{S}_s\right) + Z_{s0}'\delta_t + \varepsilon_{ust}, \qquad T^* = 2001$$

**Preferred specification (sector-specific liberalization timing):** define $T^*_s$ as the year the sector's principal WTO-related liberalization commitment took effect (first major tariff cut, quota removal, or JV-restriction easing for that product category), and estimate group-time average treatment effects $ATT(g, t)$ by liberalization-timing cohort $g$ (Callaway & Sant'Anna 2021), aggregated into an event-study-style path (Sun & Abraham 2021) interacted with $\tilde{S}_s$:

$$Y_{ust} = \alpha_u + \lambda_t + \sum_{k \neq -1} \beta_k \left(D_t^k \times \tilde{S}_s\right) + Z_{s0}'\delta_t + \varepsilon_{ust}, \qquad D_t^k = \mathbf{1}\{t - T^*_s = k\}$$

This avoids the negative-weighting bias that naive two-way fixed effects produces when already-liberalized sectors act as comparisons for later-liberalized sectors — the identical concern flagged in the Compute Gatekeeping log (Week 2), carried over here for consistency across the author's projects.

A compact post-period summary, analogous to the Korea note's Section 4:

$$Y_{ust} = \alpha_u + \lambda_t + \theta\left(\text{Post}_{st} \times \tilde{S}_s\right) + Z_{s0}'\delta_t + \varepsilon_{ust}$$

where $\text{Post}_{st} = \mathbf{1}\{t \geq T^*_s\}$ is now sector-specific rather than common across sectors.

**Anticipation.** Unlike Korea's 1987 transition, WTO accession was negotiated over roughly 1999–2001 and was broadly anticipated; firms in some sectors may have begun adjusting before the formal accession date. This should be treated as a distinct, named identification threat (Section 6), not folded silently into the pre-trend check.

## 5. Mechanism interpretation

Under the **capacity-building mechanism**, higher pre-accession support should predict broader post-accession entry and innovation diffusion:
$$\beta_k^{\text{entry}} > 0, \quad \beta_k^{\text{new-firm patents}} > 0, \quad \beta_k^{\text{HHI}} < 0 \quad (k \geq 0)$$

Under the **incumbent-entrenchment mechanism**, higher pre-accession support should predict persistent concentration and incumbent-favored innovation:
$$\beta_k^{\text{entry}} \leq 0, \quad \beta_k^{\text{incumbent patents}} > 0, \quad \beta_k^{\text{HHI}} > 0 \quad (k \geq 0)$$

Dimension-specific specifications (replacing $\tilde{S}_s$ with $\tilde{C}_{sd}$ for each $d \in D$) test which form of pre-accession support — persistence, specificity, network breadth, or allocation — is doing the work. The **allocation** dimension is likely to be especially informative here: the 2004 policy's dual-track investment-approval system (簡易备案 for incumbents expanding capacity vs. strict 核准 for new entrants) is a clean example of a mechanism that could convert formal trade opening into continued informal protection for the same firms already holding approval status — this is exactly the kind of post-treatment institutional response that motivates treating the 2004 document as an outcome rather than a treatment source (Section 3).

## 6. Identification concerns and robustness

The central selection concern — that pre-accession support reflects the state's prior bet on already-promising sectors rather than the creation of reusable coordination capacity — carries over from the Korea design and should be addressed the same four ways: (i) pre-2001 event-study coefficients as a pre-trend diagnostic; (ii) baseline sector characteristics ($Z_{s0}$: capital intensity, pre-accession export exposure, pre-accession concentration) interacted with year effects; (iii) sensitivity checks against global demand shocks unrelated to accession; (iv) comparison of the archival index against simpler proxies (state-owned share, subsidy levels).

Three threats are distinctive to this design and were not present in the Korea note:

**Anticipation.** WTO accession was announced and negotiated well before December 2001. Robustness checks should test alternative $T^*$ definitions (e.g., 1999 bilateral agreement date vs. 2001 formal accession) and inspect whether adjustment visibly begins before the formal date.

**Staggered, unequal phase-in intensity.** Because different product categories liberalized on different schedules and by different amounts, $T^*_s$ and treatment intensity are themselves policy choices correlated with sector characteristics — this should be treated as a second selection margin, separate from the selection concern about $S_s$ itself, and addressed by including the pre-announced phase-in schedule (from the accession protocol's tariff-binding tables) as a control, not only as the timing variable.

**Treating the 2004 policy as outcome, not treatment.** Using a post-accession document (2004) as descriptive evidence of *how* pre-existing incumbents adapted their regulatory tools after liberalization is legitimate and useful — but only as an outcome-side qualitative narrative, clearly separated from the quantitative $S_s$ construction. The data folder and any future write-up must keep these two roles visually and structurally distinct (see `data/README.md`'s existing real/demo separation, which should be extended to a treatment-period/outcome-period separation once 1994-era sources are added).

Standard errors clustered at the sector level; given a likely small number of sectors, wild-cluster bootstrap or randomization inference should be planned for from the start rather than added late.

## 7. AI-assisted measurement workflow

Unchanged in structure from the Korea note and the existing `docs/` templates in this repository: fixed rubric, structured output schema, source-level metadata, prompt/output logging, benchmark validation against hand-coded samples, and human review routing for ambiguous cases. The coder-blinding protocol described in Section 3 should be added explicitly to `docs/validation_plan.md` as a named requirement, not left implicit.

**Near-term outputs:** (i) locate and digitize the 1994 *Automotive Industry Policy* and at least one additional pre-2001 sector source (Eighth or Ninth Five-Year Plan sectoral chapter); (ii) recode a real pre-treatment batch from these sources, replacing the 2004-sourced batch's role as "treatment evidence"; (iii) build the WTO accession protocol's sector-level tariff-binding schedule as the phase-in timing variable; (iv) identify and test access to outcome data sources — China Industrial Enterprise Database (NBS, firm entry and characteristics), SIPO/CNIPA patent records, sector-level concentration constructed from the Enterprise Database itself; (v) a short validation memo once a pre-2001 benchmark sample exists.

## 8. Expected contribution

Substantively, this note extends the Korea design's underlying question — whether liberalization interacts with, rather than replaces, inherited state coordination — to a trade-opening rather than political-opening shock, and to a staggered rather than single-date treatment. Methodologically, it reuses the same source-traceable coding infrastructure and the same staggered-adoption estimator choice as the author's other applied work, making the three projects (Korea; China/WTO; Compute Gatekeeping) a consistent methodological program applied to three distinct institutional settings, rather than three unrelated exercises.

## 9. Immediate next step

Recode the automobile sector's pre-treatment State Support Index entries from the **1994** original policy text (not the 2004 revision already coded). Until this is done, `data/real_coded_passages_automobiles.csv` should be understood as *post-treatment descriptive material*, not as input to $S_s$.
