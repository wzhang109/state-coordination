# State Coordination Reproducibility Demo

A small public demo for source-traceable policy-text measurement and event-study workflow. This repository uses **synthetic data only**. It is designed to demonstrate workflow habits rather than present final empirical results.

## Why this repo exists

My research asks whether inherited state coordination structures shape post-transition outcomes such as firm entry, patenting, and concentration. The main empirical challenge is measurement: how to turn policy texts, laws, industrial plans, R&D mandates, and archival passages into auditable sector-level metrics.

This demo shows a minimal version of the workflow:

1. maintain document-level source logs;
2. code archival passages using a fixed rubric;
3. validate machine-assisted scores against hand-coded benchmarks;
4. construct a sector-level support index;
5. merge the index into a sector-year panel;
6. estimate a simple event-study specification on synthetic data.

The goal is not to automate substantive judgment away. The goal is to make measurement more scalable while keeping each score traceable to documentary evidence and human review.

## Status

This repository currently combines a synthetic demo (illustrating the full workflow end-to-end) with a first real pilot batch: 9 passages hand-coded from the official 2004 "Automotive Industry Development Policy" (汽车产业发展政策), State Council/NDRC Order No. 8. The pilot batch covers a single sector and a single source document; it is not yet a completed empirical analysis. See `data/README.md` for which files are synthetic and which are real, and `docs/prompt_log_automobiles_2026-07-19.md` for the coding run log.

## Repository structure

```text
state-coordination-repro-demo/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   ├── demo_coded_passages.csv       # created by script 00
│   ├── demo_sector_year.csv          # created by script 00
│   └── demo_support_index.csv        # created by script 01
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
    ├── event_study_coefficients.csv  # created by script 02
    └── event_study_plot.png          # created by script 02
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

## What is auditable

- `docs/coding_rubric.md` defines coding dimensions and score meanings before analysis.
- `docs/source_log_template.csv` shows the metadata needed to trace a coded passage back to a source.
- `docs/prompt_log_template.md` gives a structured way to log AI-assisted coding runs.
- `docs/validation_plan.md` outlines benchmark construction, error analysis, and human review routing.
- `scripts/01_construct_index.py` makes the weighting and standardization choices explicit.

## Limitations

This repository uses synthetic data. Coefficients, plots, and output tables should not be interpreted substantively. The repository is intended to demonstrate reproducible project structure, transparent documentation, and a workflow for scaling measurement while preserving human oversight.

The event-study coefficients and plots in outputs/ are still generated from synthetic data only; the real pilot batch in data/real_* has not yet been run through the quantitative pipeline.
