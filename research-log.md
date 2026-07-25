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
