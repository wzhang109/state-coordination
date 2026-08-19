# Outcome Data Reconnaissance

Status: desk research completed 2026-08-13. No data has been acquired yet — this is a
survey of access routes and their realistic feasibility, per `README.md`'s "Limitations"
section: outcome variables (sector-year firm entry, patenting, concentration) are not yet
assembled.

Two outcome variables are needed for the sector-year panel: **firm entry/exit** and
**patenting**. Findings below for each, ranked by realistic feasibility for an independent
researcher without a current university library affiliation.

## Firm entry/exit

### Option A: China Industrial Enterprise Database (中国工业企业数据库) — not currently accessible

This is the dataset the literature actually uses for this kind of question: NBS
firm-level data on "above-scale" industrial enterprises (annual sales above 5 million RMB,
lowered to 2 million RMB from 2011), commonly cited coverage 1998–2015, though data
quality is generally considered strongest through the mid-2000s and more debated in later
years ([Nie, Jiang & Yang 2012](https://mpra.ub.uni-muenchen.de/50945/1/MPRA_paper_50945.pdf)
is the standard methodological caution paper — flags firm-ID matching problems across
years, measurement errors, outliers, and definitional ambiguity, and is worth citing
directly if this dataset is used later).

Access is realistically gated behind a university library subscription (confirmed at
Peking University, Renmin University, and others) or the NBS-linked "中国微观经济数据查询系统."
Neither is available without an institutional affiliation. Market-resold versions exist but
several independent sources flag authenticity risk — altered or fabricated copies
circulating for sale — which makes this route unsuitable without a way to verify
provenance.

**Status: blocked without a university affiliation or a collaborator who has one.** Worth
revisiting if such a collaboration becomes available (e.g., through the outreach already
underway on the Accountability Continuity project — a different literature, but the kind of
academic contact that could plausibly also unlock a data-access route).

### Option B: National Enterprise Credit Information Publicity System (国家企业信用信息公示系统) — realistic near-term proxy

Public system (国家市场监督管理总局) covering business registration records: establishment
date, industry classification, registered capital, status, for essentially all registered
entities, not just above-scale industrial firms. The official portal doesn't support bulk
export, but third-party aggregators built on the same underlying data (启信宝/Qixin,
similarly 企查查/Qichacha, 天眼查/Tianyancha) offer batch queries with exportable fields
including establishment date and industry classification — usable to construct a sector ×
year new-registration count as an entry proxy.

This is not the same variable as the literature's usual "firm entry" (which is typically
scoped to above-scale industrial firms specifically), and registration date is not identical
to operational entry — both caveats belong in the eventual outcomes README if this is used.
But it is a real, independently constructible proxy, accessible without institutional
affiliation, at the cost of a paid batch-query service.

**Status: realistic. Next step is pricing and coverage-checking one of these services** —
not yet done.

## Patenting

### Option A: CNIPA official statistics — too aggregated

CNIPA publishes periodic statistical reports (e.g., annual "patent-intensive industries"
monitoring reports) with industry-level aggregates, but the industry categories used
(ICT manufacturing, new materials, pharmaceuticals, etc.) don't cleanly map onto
automobiles/textiles as defined in this project, and the reports are national aggregates,
not a sector × year panel matched to this project's document-based sector definitions.

**Status: not usable directly as a panel input, but useful as an external sanity check
once a sector-level series is constructed some other way.**

### Option B: Google Patents Public Data (BigQuery) — realistic, free

Free dataset (Creative Commons Attribution 4.0), covers 100+ countries including China,
includes IPC and CPC classification codes, updated quarterly, queryable via BigQuery SQL
([google/patents-public-data on GitHub](https://github.com/google/patents-public-data)).
The standard approach in the patent-economics literature is to build an IPC-to-industry
crosswalk (e.g., specific IPC classes for motor vehicles vs. textile machinery) and filter
by applicant country/location to construct a sector × year patent-count series. This
requires SQL and a crosswalk decision, both within scope of this project's existing
methodology (comparable in spirit to the coding rubric — a fixed mapping decided before
outcomes are examined, not adjusted after seeing results).

**Status: realistic, free, and the recommended near-term path.** Next step is drafting the
IPC-to-industry crosswalk for automobiles and textiles specifically, then a test query.

### Option C: Commercial patent platforms (IncoPat, PatSnap) — fallback

Better sector tagging out of the box, but paid. Worth keeping as a fallback if the
BigQuery route's IPC crosswalk proves too noisy on inspection.

## Recommended near-term path

1. Patents: draft the IPC-to-industry crosswalk for automobiles and textiles, run a test
   BigQuery query, sanity-check counts against CNIPA's published aggregates.
2. Firm entry: price out one bulk-query aggregator (启信宝 or similar), check whether
   industry classification in that data can be mapped to the two sectors already coded.
3. Keep the China Industrial Enterprise Database as the aspirational source, not the
   working plan, unless an institutional route opens up.

## Open questions

- Whether a registration-date proxy (Option B under firm entry) is a defensible enough
  outcome variable to report, or whether it needs to be framed explicitly as a robustness
  check rather than the primary specification once real above-scale firm data is
  unavailable.
- Whether the IPC-to-industry crosswalk should be built from scratch or adapted from an
  existing published crosswalk (searching for one is the literal next task, not yet done).

## Results: first real patent pull (2026-08-14/15)

Test query run in BigQuery against `patents-public-data.patents.publications`, using the
crosswalk in `docs/ipc_industry_crosswalk.md` (B60#+B62D for automobiles; D01–D06 textile
machinery, excluding paper/printing, for textiles). Two variants run, 1990–2010:

- **Variant A — assignee country = China** (`assignee_harmonized.country_code = 'CN'`)
- **Variant B — filing office = China** (`country_code = 'CN'`)

Raw exports: `data/outcome_patents_automobiles_textiles.csv` (Variant B, adopted as the
working series) and `data/outcome_patents_automobiles_textiles_assignee_variant.csv`
(Variant A, kept for provenance/comparison, not used directly).

### Variant A has a tail-year data-quality problem

Variant A grows steadily through 2008 (automobiles: 843 → 9,103) and then drops sharply —
2009: 1,942; 2010: 638. That is almost certainly a processing artifact, not an economic
collapse: Google's `assignee_harmonized` field depends on name-disambiguation work that
lags the raw publication data, so the most recent 1–2 years are systematically
undercounted. Variant B shows no such drop (2009: 22,237; 2010: 26,855 — continued growth).
**Decision: Variant B (filing office) adopted as the working patent series.** Variant A's
tail-year figures should not be used or reported as-is.

Variant B is not a perfect substitute — "filed at the Chinese patent office" includes
foreign multinationals filing locally, not only domestic Chinese firms, which is a scope
question worth revisiting once this feeds into an actual specification (the state-support
mechanism this project is testing is about domestic firms specifically).

### Both sectors show large nationwide growth — expected, and not yet informative on its own

Automobile filings grew roughly 29x and textile filings roughly 18x from 1990 to 2010
(Variant B). This tracks with China's well-documented nationwide patent-filing boom over
this period (1992/2000/2008 patent law revisions; the 2008 National IP Strategy), which
affected essentially every sector — this is a common trend, not sector-specific signal.
The event-study specification's year fixed effects (`C(year)` in `scripts/02_`) are exactly
what absorb a shared national trend like this, so it is not disqualifying, but the raw
counts above should not be read as sector-specific evidence on their own.

### A real pre-trend concern, not yet resolved

Auto/textile filing ratio: 1.36 (1990) → 1.90 (2000, the year *before* accession) → 1.82
(2001) → ~2.2 (2004 onward, roughly stable after). The ratio was already rising sharply
*before* 2001, not flat — automobile filings grew 38.7% year-over-year in 2000 alone.
CAGR comparison: automobiles grew 16.6%/year 1990–2000 vs. 19.8%/year 2001–2010 (modest
acceleration); textiles grew 12.75%/year 1990–2000 vs. 17.1%/year 2001–2010 (textiles
accelerated by *more*, in relative terms, than automobiles did).

Two things follow from this, both flagged rather than resolved:

1. **This is exactly the kind of pre-trend `validation_plan.md` Section 8's joint test
   exists to catch.** Growth was already elevated and rising before the 2001 event date —
   the formal joint pre-period test (already coded into `scripts/02_event_study_demo.py`)
   needs to be run for real once this series is merged into the actual panel, not assumed
   to pass because the story sounds right.
2. **Textiles accelerating relatively more than automobiles post-2001 does not obviously
   match a simple "protective sectors benefit more from WTO-era continuity" story** — eyeballed
   levels are not a substitute for the actual regression. Worth holding this loosely until
   the real specification is run, not fitting a narrative to two ratios.

**Next:** merge this series into a sector-year panel structure (matching
`demo_sector_year.csv`'s shape), decide how to handle the domestic-vs-foreign-filer scope
question in Variant B, and run the actual pre-trend joint test once the State Support Index
is on the same panel.
