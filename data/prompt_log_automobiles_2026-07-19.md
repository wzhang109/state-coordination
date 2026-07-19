# Prompt / Output Log — Automobile Sector Real Pilot Batch

| Field | Value |
|---|---|
| run_id | AUTO-2004-001 |
| date | 2026-07-19 |
| model | Claude (AI research assistant) |
| prompt_version | v1 — manual passage identification + rubric mapping discussion |
| rubric_version | docs/coding_rubric.md (current) |
| source_batch | Automotive Industry Development Policy (汽车产业发展政策), State Council/NDRC Order No. 8, 2004 |
| input_fields | Full official gazette text (gov.cn), coding_rubric.md dimension definitions |
| output_schema | source_id, sector, year, dimension, score, passage_excerpt, coder_id, confidence, review_status, notes |
| reviewer | Wenwen Zhang |
| benchmark_sample | None yet — this is the first real (non-synthetic) batch; no hand-coded benchmark exists yet for cross-validation |
| known_issues | (1) Only one source document coded so far — persistence dimension is weakly identified with a single document; (2) 1994 original policy text not yet digitized/verified, so historical continuity is inferred from the 2004 document's own preamble reference rather than direct comparison of both texts; (3) treatment-year framing (1987 in the synthetic demo vs. 1994/2004 in real data) not yet reconciled — pending research design decision. |
| decision | Accepted, pending reviewer's independent re-check against rubric before treating as final |
