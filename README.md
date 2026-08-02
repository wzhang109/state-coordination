# State Coordination — Policy-Text Measurement and Event-Study Workflow

Source-traceable measurement of state industrial-policy support, built to turn policy
texts into auditable sector-level metrics that can be tested with event-study panel
designs.

The repository contains a synthetic demo illustrating the full pipeline end-to-end, and a
growing set of real coded passages from primary policy documents. **Estimates currently in
`outputs/` run on synthetic data only and should not be interpreted substantively.**

## Why this repo exists

The research question is whether inherited state coordination structures shape
post-transition outcomes such as firm entry, patenting, and concentration. Two hypotheses
are in play and both are plausible: those structures may persist as genuine organizational
capital that helps new entrants, or they may persist as barriers that entrench incumbents.

The binding constraint on answering this is measurement. "State support for sector X in
1994" is not a number anyone publishes. It exists as laws, five-year plans, ministry
directives, and R&D mandates. So most of the work here is turning that text into a number
that survives scrutiny:

1. maintain document-level source logs;
2. code passages against a rubric fixed before outcomes are examined;
3. validate machine-assisted scores against hand-coded benchmarks;
4. construct a sector-level support index;
5. merge the index into a sector-year panel;
6. estimate an event-study specification.

The goal is not to automate substantive judgment away. It is to make measurement scalable
while keeping every score traceable to documentary evidence and human review.

## Empirical settings

The measurement approach is being developed for two independent settings.

**Setting 1 — South Korea, 1987 democratization.** *Currently paused.* The sector-year
outcome data required for the panel is classified and not accessible. The synthetic demo
in this repository is built around this setting, which is why event time is indexed to
1987. May resume if data access changes.

**Setting 2 — China, 2001 WTO accession.** *Active.* All real coded data comes from this
setting.

Both settings share a design feature worth naming precisely: a **common event date**, with
sectors differing in **exposure intensity** (their pre-transition support score). This is a
differential-exposure event study, not a staggered-adoption design — the distinction
matters for which estimators are appropriate.

## Data status

| Sector | Year | Document | Passages | Relative to 2001 accession |
|---|---|---|---|---|
| Automobiles | 1994 | 汽车工业产业政策 | 13 | Pre |
| Automobiles | 1996 | 九五纲要, automotive section | 3 | Pre |
| Automobiles | 2004 | 汽车产业发展政策 (State Council/NDRC Order No. 8) | 9 | Post |
| Textiles | 1998 | 国发〔1998〕2号 | 8 | Pre |

The pre-transition batches (1994, 1996, 1998) are the inputs to the support index. See
`data/README.md` for file-by-file provenance and source strength.

### The 2004 batch has a different role

The 2004 automotive policy is **not** used to construct the pre-transition index. It
documents institutional continuity across the transition. Three provisions coded in the
1994 policy reappear in the 2004 policy in near-identical or verbatim form, despite WTO
accession in 2001:

- ceiling of two joint ventures per foreign firm per vehicle category (1994 Art. 29 → 2004 Art. 48)
- 50% minimum Chinese equity share in vehicle and engine JVs (1994 Art. 32 → 2004 Art. 48)
- the designated list of vehicle import ports (1994 Art. 36 → 2004 Art. 58), unchanged

Whether that continuity is capacity-building or incumbent-entrenching is the empirical
question the index is built to address.

## Current scale and what it supports

Real coded data currently covers **2 sectors**. This has two consequences that are stated
here rather than left for a reader to discover:

**Clustered inference is not yet available.** The event-study specification in
`scripts/02_` clusters standard errors at the sector level. Clustered standard errors
require many more clusters to be valid; with two, the reported inference would be
meaningless. The script is retained as a demonstration of the intended workflow, not as an
estimation of the current sample.

**Cross-sector standardization is disabled below a threshold.** With only two sectors,
z-standardizing a dimension across sectors returns exactly ±1 regardless of the underlying
gap, discarding all magnitude information. `scripts/01_` therefore falls back to raw 0–2
dimension means until sector coverage is sufficient, and prints which scale it used.

At present the repository supports descriptive measurement and documentation of
institutional continuity, not causal estimation. The next step is horizontal expansion —
one core pre-transition document per additional sector — rather than deeper coverage of
sectors already included.

## Event-study demo output

![Event-study demo output](outputs/event_study_plot.png)

*Synthetic data only.* The plot shows interactions between event-time indicators and the
pre-transition State Support Index, with sector and year fixed effects and k = −1 omitted
as the reference period. Coefficients are not substantive results; the figure illustrates
the output format of the workflow.

**Pre-period coefficients — left of the dashed line — are where the identifying assumption
is tested, not decoration.** The design identifies effects only if, absent the transition,
sectors with different support scores would have followed parallel paths. If pre-period
coefficients are jointly indistinguishable from zero, that assumption is supported. If they
trend, the design does not identify a causal effect and results are reported as descriptive.

## Repository structure

```text
state-coordination/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   ├── demo_coded_passages.csv                    # created by script 00
│   ├── demo_sector_year.csv                       # created by script 00
│   ├── demo_support_index.csv                     # created by script 01
│   ├── prompt_log_automobiles_2026-07-19.md       # AI-assisted coding run log
│   ├── real_coded_passages_automobiles_1994.csv
│   ├── real_coded_passages_automobiles_1996.csv
│   ├── real_coded_passages_automobiles_2004.csv
│   ├── real_coded_passages_textiles.csv
│   ├── real_source_log_automobiles.csv            # 2004 sources
│   ├── real_source_log_automobiles_1994.csv
│   └── real_source_log_textiles.csv
├── docs/
│   ├── coding_rubric.md
│   ├── validation_plan.md
│   ├── prompt_log_template.md
│   └── source_log_template.csv
├── scripts/
│   ├── 00_generate_demo_data.py
│   ├── 01_construct_index.py
│   └── 02_event_study_demo.py
└── outputs/
    ├── README.md
    ├── event_study_coefficients.csv               # created by script 02
    └── event_study_plot.png                       # created by script 02
```

## How to run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python scripts/00_generate_demo_data.py
python scripts/01_construct_index.py
python scripts/02_event_study_demo.py
```

Scripts must run in order; each depends on the previous one's output.

## What is auditable

- `docs/coding_rubric.md` defines coding dimensions and score meanings before analysis.
- `docs/source_log_template.csv` shows the metadata needed to trace a coded passage back to its source.
- `docs/prompt_log_template.md` gives a structured way to log AI-assisted coding runs; `data/prompt_log_automobiles_2026-07-19.md` is a completed instance.
- `docs/validation_plan.md` covers benchmark construction, weighting sensitivity, reliability, and human review routing.
- `scripts/01_construct_index.py` makes weighting and standardization choices explicit and reports which scale was used.

Every real coded passage carries `passage_excerpt`, `coder_id`, `confidence`, and
`review_status`, so any individual score can be contested on the evidence rather than in
the abstract.

## Limitations

- Coefficients, plots, and output tables in `outputs/` are generated from synthetic data and carry no substantive interpretation.
- Real coded data has not yet been run through the quantitative pipeline; outcome variables (sector-year firm entry, patenting, concentration) are not yet assembled.
- Single coder to date. Reliability evidence and the plan for addressing this are in `docs/validation_plan.md`.
- Source strength is uneven across batches. The 2004 document is verified against the official State Council gazette; the 1994 document is currently verified against an archived press reprint plus researcher screenshots. Replacing the 1994 source with an official one is an open task.
- Sector coverage is imbalanced (automobiles: 3 documents; textiles: 1). A post-accession textile document is missing and would mirror the 2004 automotive batch.

## Related work

This repository is the methodological ancestor of a parallel project applying the same
measurement approach to a different domain:

**[Accountability Continuity Research](https://github.com/wzhang109/Accountability_Continuity_Research)**
— an institutional framework for human-agentic task allocation. It asks which decisions
require a continuous, accountable human as AI systems become more capable, and builds an
Accountability Continuity Index using the same measurement design pattern used here:
dimensions fixed before outcomes are examined, every score traceable to primary evidence,
and ambiguous cases routed to human review rather than machine finalization.

The rubric schema is deliberately shared across both projects (`coder_id`, `confidence`,
`review_status`) so that measurement decisions remain auditable in the same way regardless
of subject matter.

The identification strategies differ and should not be conflated. This project uses a
common event date with sectors differing in exposure intensity. The accountability project
faces staggered adoption timing with an ordinal treatment, which calls for a different
estimator family.
