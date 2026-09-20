# Earlier State Support and Access to Capabilities After Trade Opening

Wenwen (Celine) Zhang · Revised research design · 20 September 2026

This design develops a mechanism question already present in the Korea note dated April 2026. The project began in late March according to the author's retrospective account; the China WTO setting entered the repository in July. September revisions clarify measurement and identification requirements. They do not mark the origin of the mechanism question. [Project history](docs/project_history.md) records the supporting dates.

This is a candidate empirical route, not a causal design already supported by the available data. Changing from democratization to trade opening preserves part of the substantive question but changes the event and counterfactual. Further commitment to this route depends on finding suitable evidence of beneficiaries and actual access.

## Research question

**Around China's WTO accession, which forms of earlier state support left capabilities that new entrants and downstream firms could use, and which mainly preserved advantages for established firms?**

The object of study is access to resources created or allocated by policy. Trade opening is not a substitute for democratization. The accompanying [cross-country exploration](research/2026-09-20/README.md) is background evidence at a different level of analysis.

## Competing mechanisms

| Candidate mechanism | Documentary evidence to code | Outcome evidence needed | Alternative explanations |
|---|---|---|---|
| Capabilities accessible beyond original recipients | Shared training, supplier development, technical resources, open eligibility, infrastructure access | Gains among new entrants or downstream firms; persistence after preferences end | Demand, imported technology, other reforms, selection of promising industries |
| Advantages concentrated among existing recipients | Restricted approvals, named beneficiaries, exclusive financing eligibility, continuing entry barriers | Benefits concentrated among earlier recipients; limited access by others | Efficient scale, different risk or productivity, industry composition |
| Both mechanisms operate | Broad support and selective privileges in the same policy | Wider capabilities coexist with concentrated access | Measurement error and aggregation hiding distinct groups |

The capacity-building versus incumbent-entrenchment distinction is documented in the early Korea note; the access fields below make it more operational. These are hypotheses, not findings. More patents, more concentration, or growth among incumbents alone cannot distinguish them. Text describes formal arrangements; actual implementation and use require separate evidence.

## Measurement

Retain the existing State Support Index and source links as an earlier measurement layer. Its dimensions are persistence, specificity, network breadth, and allocation. The direction field distinguishes protective, compressive, and neutral allocation provisions.

The index is **not** a direct measure of state capacity or policy quality. Allocation=2 includes targeted privileges. A single combined score can conceal opposing mechanisms.

The next coding revision should separately record:

1. the instrument and resource involved;
2. eligible beneficiaries and entry conditions;
3. whether new entrants, suppliers, or downstream users can obtain access;
4. any exclusivity, expiry, or withdrawal condition;
5. whether evidence concerns intent, a formal rule, implementation, or an observed result;
6. source passage, date, uncertainty, and review status.

These fields have not been applied or validated. Existing rows must not be silently relabeled. Some sector outcomes have already been inspected, so the revision is exploratory. Independent coding and outcome-masked review of new material would improve credibility but cannot make prior work retrospectively blinded.

The 1994 and 1996 automobile and 1998 textile batches are pre-accession evidence. The 2004 automobile batch documents later arrangements and cannot define earlier exposure. The 1994 batch still needs a stronger official source.

## Empirical scope and timing

The current two-sector sample supports documentary comparison and descriptive checks. It is insufficient for a credible causal event study or sector-clustered inference.

Before selecting an estimator, define a consistent event and comparison:

- A **common accession-date comparison** asks whether sectors with different earlier support changed differently around 2001. It requires a defensible counterfactual trend and attention to anticipation, other reforms, and demand.
- A **policy-specific timing comparison** uses independently documented tariff, quota, or entry-rule changes. These need not begin together or constitute comparable treatments. Timing and intensity may themselves be selected.

These designs are not interchangeable. Relative-time interactions alone do not implement a modern group-time treatment estimator or solve treatment heterogeneity. The earlier proposal's estimator claim is withdrawn pending a clear estimand, treatment definition, comparison group, and sufficient data.

Pre-period patterns are diagnostics. Failure to reject a pre-trend does not establish parallel trends, and choosing a favorable window after seeing outcomes does not restore identification. See [Roth (2022)](https://www.aeaweb.org/articles?id=10.1257/aeri.20210236).

## Existing outcome files

Two patent-count variants for automobiles and textiles, 1990–2010, are saved in the data folder. The September analysis recomputed those counts but did not rerun their extraction. The log refers to a query and industry crosswalk absent from the inspected 0346cc0 snapshot. Recovering and auditing that provenance is the immediate data task.

In the saved main file, 1990–2000 compound annual patent growth was approximately 16.63% for automobiles and 12.75% for textiles. Their count ratio rose from 1.36 to 1.90 before accession. Post-2001 divergence cannot simply be attributed to earlier support. Industry totals do not distinguish new entrants from incumbents or identify who used a capability.

## Next steps and decision points

1. Recover the query, industry mapping, population definition, and deduplication rules; audit a sample against source records. Until provenance is established, keep the files descriptive and unverified upstream.
2. Pilot the proposed mechanism fields, record disagreements, and seek independent review. If coders cannot distinguish access from selective privilege, revise the measure before expanding it.
3. Evaluate outcome data for new entrants, original recipients, and downstream users. Add comparable sectors where source coverage permits; more sectors alone do not solve identification.
4. Retain a historical or descriptive comparison if causal requirements cannot be met. A causal design is conditional on evidence, not a promised result.

The intended contribution is a source-traceable account of **what earlier support made possible, for whom, and under what access conditions**. It does not require finding state intervention uniformly beneficial or harmful.
