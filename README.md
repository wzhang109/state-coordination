# State Coordination

**Which forms of earlier state support leave capabilities that new entrants and downstream firms can use, and which mainly preserve advantages for established firms?**

I approach this question through development economics and public policy, with an interest in how institutions shape people's opportunities over time. This project uses historical policy documents to measure what governments supported, how support was allocated, and who could use the resulting resources.

The question grew out of a broader hypothesis about state building, democratization, and long-run prosperity. The current research separates **state capacity**, **industrial-policy support**, and **political regime**. It does not assume that authoritarian rule is necessary for development, or that a higher support score measures more effective government.

## Preliminary findings — September 2026

A first exploratory analysis combines public state-capacity, democratization, and GDP data. Higher capacity before a qualifying democratic transition is positively associated with growth over the following twenty years in a common sample covered by World Bank and Maddison data. Ten-year estimates are less precise. These are adjusted associations, not estimates of the causal effects of authoritarianism or institutional sequencing.

**[Read the findings, methods, and limitations](research/2026-09-20/README.md)** · **[中文说明](research/2026-09-20/findings.zh-CN.md)**

The analysis includes sample lists, all specifications, source checks, and scripts. It provides context for the narrower policy question; it does not test the sector-level mechanisms below.

## Current research question

The active setting is **China around WTO accession in 2001**. The proposed comparison distinguishes provisions that may create capabilities accessible beyond their original recipients from provisions that restrict access to selected firms.

Evidence to investigate includes shared training, supplier development, technical infrastructure, financing eligibility, production approvals, and joint-venture restrictions. A policy can contain both broadly accessible support and selective privileges. Intent in a policy document is not evidence of implementation or impact.

The next empirical question is whether the benefits of earlier support extended to **new entrants and downstream firms**, or remained concentrated among **pre-existing recipients**, as market conditions changed. Industry patent totals alone cannot distinguish these mechanisms.

See the [revised research design](researchstrategy_ChinaWTO.md) and [measurement priorities](docs/current_research_question.md).

## What exists, and what remains untested

| Material | Current status | What it supports |
|---|---|---|
| Cross-country analysis, September 2026 | Real public data; exploratory regressions and source diagnostics | Associations between pre-transition capacity and later growth |
| Chinese policy passages | Four batches covering automobiles and textiles | Source-traceable measurement and policy continuity |
| Saved sector patent counts, 1990–2010 | Files exist; original query and industry mapping need a complete audit | Internal descriptive checks, not a verified policy effect |
| Event-study scripts and plots in the outputs folder | Synthetic demonstration | Illustration of a workflow, not empirical findings |
| Capabilities versus incumbent advantages | Revised research question | Hypotheses awaiting measurement, independent review, and suitable outcomes |

The saved patent files already show different growth patterns between automobiles and textiles before 2001. With only two sectors, the project does not support a credible causal event study or reliable sector-clustered inference.

## Policy-text coverage

| Sector | Year | Document | Coded passages | Role |
|---|---|---|---:|---|
| Automobiles | 1994 | 汽车工业产业政策 | 13 | Pre-accession support |
| Automobiles | 1996 | Ninth Five-Year Plan, automotive section | 3 | Pre-accession support |
| Automobiles | 2004 | 汽车产业发展政策 | 9 | Post-accession policy continuity |
| Textiles | 1998 | 国发〔1998〕2号 | 8 | Pre-accession support |

The 2004 document is not used to define pre-accession support. Source strength and coding history are documented in [data/README.md](data/README.md). The rubric records persistence, specificity, network breadth, allocation, and an allocation-direction field. **A high allocation score can denote selective privilege; it is not a measure of beneficial capacity.**

The original South Korea 1987 design remains a historical design note. Required outcome coverage has not been secured for this project. Related public research and replication resources exist, so the earlier blanket description of Korean data as classified was too strong. Coverage for the proposed post-1987 analysis still needs checking.

## Research practice

- Keep documentary evidence, constructed measures, and outcome interpretation separate.
- Record policy dates and beneficiaries; do not infer capacity from later economic success.
- Preserve existing coded batches. New mechanism fields require a revised rubric and independent review.
- Disclose that outcome patterns have already been examined. New coding changes are exploratory, not retrospectively preregistered or fully blinded.
- Report null and conflicting results. A non-significant pre-trend test does not establish parallel trends.

The research motivation and question are mine. Coding, data preparation, and analysis use substantial AI assistance. I am still developing the technical methods; the new analysis has not undergone independent methodological review.

## Reproduce

The [analysis folder](research/2026-09-20/README.md#reproduce) contains requirements, a source manifest, download script, and instructions. Source files are obtained from their original publishers; the exact public World Bank extract is preserved because its live API can change.

The older synthetic demo remains in the scripts folder. Its output status is described in [outputs/README.md](outputs/README.md).

## Related project

[Accountability Continuity](https://github.com/wzhang109/Accountability_Continuity) examines human review, judgment, and responsibility in AI-assisted work. The projects share an interest in how institutional arrangements affect people's capabilities. They have different data and research designs; evidence from one does not validate the other.
