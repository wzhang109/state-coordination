# Data folder

This folder contains two types of files: synthetic demo data used to illustrate the workflow, and a small real pilot batch coded from an actual public policy document.

## Synthetic demo data (`demo_*`)

- `demo_coded_passages.csv`: synthetic passage-level scores for four dimensions of pre-transition state support.
- `demo_sector_year.csv`: synthetic sector-year outcomes before and after 1987.
- `demo_support_index.csv`: generated sector-level support index.

These files are for workflow demonstration only and should not be interpreted substantively.

## Real pilot batch (`real_*`)

- `real_source_log_automobiles.csv`: source metadata for passages hand-coded from the official 2004 State Council/NDRC Order No. 8, "Automotive Industry Development Policy" (汽车产业发展政策), verified against the official gazette text at gov.cn.
- `real_coded_passages_automobiles.csv`: rubric-based scores (persistence, specificity, network breadth, allocation) for 9 real passages from that document, coded with AI-assisted first-pass drafting and human review (see `docs/prompt_log_automobiles_2026-07-19.md` for the full run log).

This is the first real (non-synthetic) data added to this repository, covering a single sector and a single source document. It is a pilot batch, not a completed empirical analysis.

For a real project, raw archival materials should be stored separately if copyright or access restrictions apply. Public repositories should include metadata, codebooks, and replication-safe extracts rather than sensitive or non-public source text. 

More on the go
