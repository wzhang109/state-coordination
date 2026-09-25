# State Coordination

**How do inherited state institutions and policy support shape later development, and who can use the capabilities they leave behind?**

I began this independent project in **late March 2026**, when I formed an initial hypothesis and put forward a research proposal about state building, democratization, and long-run prosperity. This origin date is a retrospective account recorded in September. The archived Korea note is dated April 2026; the GitHub history begins on 19 July. These dates refer to different stages of the work.

My background is in development economics and public policy. I am interested in how institutional conditions influence people's opportunities over time. The project began with a conjecture about Asian development experiences; it does not assume that authoritarian rule or a particular political sequence is necessary for prosperity.

**Start here:** [Project history and date evidence](docs/project_history.md) · [为什么研究、做了什么、得到什么、还不知道什么](docs/research_story.zh-CN.md) · [一步一步理解研究](docs/study_guide.zh-CN.md)

## The questions and their relationship

| Level | Question | Status |
|---|---|---|
| Broad motivation | How do institutions create conditions for lasting development? | Organizing concern |
| Original hypothesis | Does capacity accumulated before democratization help explain later prosperity, and is that sequence necessary? | Associations explored; necessity and causal sequencing not established |
| Mechanism, already in the note dated April | Does earlier support leave usable capabilities beyond original recipients, or preserve incumbent advantages? | Competing explanations requiring direct evidence |
| China WTO pilot | What do policy documents specify about resources, beneficiaries, and access around trade opening? | Early coding exists; implementation and beneficiary outcomes remain incomplete |
| September cross-country analysis | Among qualifying democratic transitions, how does prior capacity relate to later GDP growth? | Exploratory evidence at a different level of analysis |

The move from South Korea's democratization to China's WTO accession changed the setting and event. The mechanism question continued, but trade opening is not a substitute for democratization. The cross-country regressions neither validate the policy index nor establish the sector mechanisms. See the [current question map](docs/current_research_question.md).

## What I have done and found so far

The repository contains an early methodological proposal, policy passages coded against a rubric, source records, saved sector patent counts, a synthetic workflow demonstration, and a September analysis using real public country data. Coding, data preparation and writing use substantial AI assistance. There is no formal research supervisor at present; independent methodological and coding review remain incomplete.

The original ten-year DDCG estimate is positive but imprecise. Selected twenty-year specifications using World Bank and Maddison data show a positive adjusted association. A subsequent comparison on identical countries does not establish that the twenty-year coefficient is larger than the ten-year coefficient. These are associations, not effects of authoritarianism, political order, or a specific policy.

**[Results, methods and limits](research/2026-09-20/README.md)** · **[中文结果](research/2026-09-20/findings.zh-CN.md)**

Two other lessons matter for the pilot. First, a high support score may represent selective privileges, so it cannot be read as better government or greater productive capacity. Second, existing industry patent totals do not identify who benefited, and the two industries were already growing differently before 2001.

## Latest evidence update — 25 September 2026

A documentary pilot follows automotive testing infrastructure into a concrete administrative record. A 2005 regulator notice lists **12 testing institutions, four venue names and 23 institution–venue links** for one testing standard. Ten institutions list the same venue. This is evidence of overlap in formally listed sites, not observed use by manufacturers or a causal effect of earlier policy.

[New findings and reproducible data](research/2026-09-25/README.md) · [中文：这次到底推进了什么](research/2026-09-25/findings.zh-CN.md)

Historical source accounts distinguish preparation, construction and accreditation. Some groundwork predates the 1994 policy; later completion cannot alone be attributed to it. The new 2005 record is post-WTO and cannot define pre-2001 exposure. Original coding scores and cross-country estimates are unchanged.

## What the materials can support

| Material | Current status | What it supports |
|---|---|---|
| Cross-country data and regressions | Real public data; exploratory source and specification checks | Conditional associations within defined samples |
| Four Chinese policy batch files | 35 coding rows; uneven source strength and incomplete independent validation | Reviewable interpretations of formal policy provisions |
| Patent counts, 1990–2010 | Internally recomputed; original query and industry mapping still need audit | Checks on saved series, not a verified policy effect |
| Event-study demonstration in outputs | Synthetic data | Illustration of calculations |
| Automotive testing notice, 2005 | 12 source-traceable institution rows; descriptive venue mapping | Scope-specific formal authorization, not manufacturer access or transactions |
| Broader access versus incumbent advantages | An early mechanism question with revised measurement requirements | Hypotheses, not established findings |

There are only two sectors in the current pilot. That is insufficient for a credible causal event study or reliable sector-clustered inference. Existing review labels in coding files do not establish independent validation of every score or interpretation.

## Policy-text coverage

| Sector | Year | Document | Coding rows | Role |
|---|---|---|---:|---|
| Automobiles | 1994 | 汽车工业产业政策 | 14 | Pre-accession provisions |
| Automobiles | 1996 | Ninth Five-Year Plan, automotive section | 3 | Pre-accession provisions |
| Automobiles | 2004 | 汽车产业发展政策 | 9 | Later continuity evidence |
| Textiles | 1998 | 国发〔1998〕2号 | 8 | Pre-accession provisions |
| Textiles | 1996 | Ninth Five-Year Plan, textile section | 1 | Pre-accession provisions; in the same textile file |

These are coding rows, not independent policies, firms, or implementation observations. A passage can appear under more than one dimension. The earlier homepage understated the 1994 count and omitted the 1996 textile row; this update corrects the inventory without changing any scores.

The 2004 document cannot define pre-2001 exposure. Recurrence of wording after 2001 can document continuity but cannot by itself establish what researchers would have known beforehand or how a policy operated. [Data notes](data/README.md) record source and interpretation limits.

## Next evidence task

The [September 25 pilot](research/2026-09-25/README.md) reaches the formal authorization layer. Next, trace one listed institution–venue pair to a dated manufacturer test report, and seek contemporary eligibility, fees and service records. If these are unavailable, keep the result descriptive rather than treating authorization as actual access. Find that evidence before expanding a support index or promising a causal estimate.

The [China WTO design](researchstrategy_ChinaWTO.md) remains a candidate mechanism study. Continuing the institutional-sequencing question or pursuing this pilot requires an explicit choice based on substantive interest, the literature, and feasible evidence. The current regressions do not decide between those routes.

## Reproduce and review

The [September analysis folder](research/2026-09-20/README.md#reproduce) contains source versions, download instructions, model tables and code. Later diagnostics are labeled as post-result additions. Code and source checks help detect mistakes; they do not validate causal assumptions.

The [research log](research_log.md) preserves earlier entries, with dated clarifications where interpretations have changed. The [history page](docs/project_history.md) links the archived Korea note and distinguishes its printed April date from its misleading filename and July upload date.

## Related work

[Accountability Continuity](https://github.com/wzhang109/Accountability_Continuity) examines human review, judgment and responsibility in AI-assisted work. It shares an interest in institutional conditions and capabilities, but has different data and questions.
