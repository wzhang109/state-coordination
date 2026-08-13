# Research Log — State Coordination / China WTO Project

Weekly entries. Format: what was done / what was found or decided / what's next.
Work is AI-assisted (passage location, drafting, code); all coding judgments
and final content are human-reviewed before acceptance.

---

## Week of July 19–25, 2026

**Focus:** From single-sector demo to first cross-sector real data

**Done:**
- Wrote `researchstrategy_ChinaWTO.md`: reframed the empirical design around
  WTO accession (2001) as a staggered liberalization shock, replacing the
  single-date Korea 1987 design. Key consequence: the 2004 auto policy batch
  is reclassified as post-treatment material; treatment evidence must predate
  Dec 2001.
- Located and coded the 1994 Automotive Industry Policy from the Sina archive
  (12 pp., verified by direct reading): 14 records. Found three provisions
  (Arts. 29, 32, 36) reappearing near-verbatim in the 2004 policy — direct
  documentary evidence for the persistence dimension.
- Added the textile sector as the contrast case: Guofa [1998] No.2
  (spindle-compression notice) + Ninth Five-Year Plan (1996), 10 records.
  The 1998 notice is highly specific but compressive — same state-coordination
  instruments as autos (entry freeze, targeted quotas), opposite direction.
- Wrote and ran `scripts/03_summarize_real_batches.py`. First real cross-sector
  table: autos > textiles on allocation (2.00 vs 1.75) and specificity
  (2.00 vs 1.67), consistent with the design's premise. Sample far too small
  to interpret beyond direction.

**Found/decided:**
- Running the pipeline exposed broken CSV quoting in two earlier files
  (unquoted commas in notes fields) — invisible until code actually consumed
  the data. Exactly why the validation plan insists on a reproducible pipeline
  rather than hand-inspected spreadsheets. Fixed and re-committed.
- Coding intensity is not symmetric across sectors yet (more auto records than
  textile); record counts partly reflect coder attention. Flagged in the
  summary script's caveats.

**Next:**
- Exhaust remaining codable passages in the 1998 textile notice and the
  Ninth Five-Year Plan textile section.
- Begin outcome-data reconnaissance: China Industrial Enterprise Database
  access options, CNIPA patent counts by sector.

  ---

## Week of August 12, 2026

**Focus:** Index construction fix + allocation direction field

**Done:**
- Found a degenerate case in `scripts/01_construct_index.py`'s cross-sector
z-standardization: with n=2 sectors, the population SD is |a-b|/2, so the
z-score reduces to sign(a-b) regardless of the size of the underlying gap.
Verified numerically across several (a,b) pairs — e.g. 2.0 vs 1.9 and 2.0 vs
0.1 produced identical standardized scores. The index was behaving as a vote
over which sector scored higher on each dimension, discarding all magnitude
information. Gated standardization on a minimum sector count (8); below that,
the script now falls back to raw 0-2 dimension means and prints which scale
it used. Documented in `README.md`'s "What is auditable" section.
- Added a `direction` field (protective / compressive / neutral) to the
allocation dimension across all four real coded-passage batches (1994, 1996,
2004 autos; 1998/1996 textiles). The original rubric scored both the 1994
auto entry-freeze (protective — restricts entry to preserve incumbents) and
the 1998 textile spindle-freeze (compressive — restricts capacity to force
contraction) as allocation=2, even though they predict opposite outcomes.
Recorded direction as a separate field rather than folding it into the score,
so the index can be computed with or without the distinction.

**Found/decided:**
- If autos (protective) and textiles (compressive) move in opposite
directions post-transition, an event-study coefficient that pools them would
be diluted toward zero — not because there's no effect, but because the
index summed two opposite mechanisms into one number. This was invisible
until the two sectors' rubric notes were placed side by side.
- Rubric revision is logged with date and reason in `docs/coding_rubric.md`,
per the reliability-tracking convention in `docs/validation_plan.md`: a
rubric that changes on contact with real data and says so is more credible
than one that claims to have been right from the start.

**Next:**
[fill in once you decide — candidates: finish validation_plan sections 6-8,
build the 1996 source log, or start the recall-worksheet answers while the
allocation rows are fresh]

---

## Week of August 13, 2026

**Focus:** Outcome-data reconnaissance (firm entry, patenting)

**Done:**
- Surveyed access routes for the two outcome variables the panel still needs. Full
findings in `docs/outcome_data_reconnaissance.md`.
- Firm entry: the standard source (China Industrial Enterprise Database) is realistically
gated behind a university library subscription I don't have; market-resold copies carry a
documented authenticity risk (Nie, Jiang & Yang 2012 and others flag this directly).
Identified a public proxy instead — business-registration data via the National Enterprise
Credit Information Publicity System, accessible in bulk through third-party aggregators
(启信宝 and similar) without institutional affiliation.
- Patenting: CNIPA's own published statistics are too aggregated to map onto this
project's sector definitions. Google Patents Public Data on BigQuery is free, covers
China, and is queryable by IPC classification — the standard approach in the literature
for constructing sector-level patent counts via an IPC-to-industry crosswalk.

**Found/decided:**
- The "gold standard" firm-entry dataset is not currently reachable without either a
university affiliation or a collaborator who has one. Rather than block on that, the
registration-date proxy is the working near-term plan — logged explicitly as a proxy, not
equivalent to above-scale industrial firm entry, so it doesn't get quietly treated as the
same variable later.
- Patents have a clear, free, realistic path (BigQuery); firm entry does not yet, and costs
money either way (aggregator query fees).

**Next:**
- Draft the IPC-to-industry crosswalk for automobiles and textiles; run a test BigQuery
query and sanity-check against CNIPA's published aggregates.
- Price out one registration-data aggregator and check whether its industry classification
maps cleanly onto the two coded sectors.
