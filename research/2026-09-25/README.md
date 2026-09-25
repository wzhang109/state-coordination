# From testing infrastructure to shared authorization

**Exploratory documentary pilot · 25 September 2026**

The new finding is a documented administrative arrangement: a January 2005 notice lists **12 testing institutions against four named venues, yielding 23 institution–venue links**. Ten institutions list the same Ministry of Transport venue. This establishes overlap in formally listed testing sites for one scope of work. It does not establish actual tests performed, access by new manufacturers, or a development effect.

[中文说明](findings.zh-CN.md) · [Official notice](https://www.mee.gov.cn/gkml/zj/bgt/200910/t20091022_173901.htm) · [Source records](sources.md)

## Why investigate this?

The existing automotive policy row `SRC_AUTO_1994_006` concerns national research, testing and inspection institutions. The September 20 audit already identified a problem: policy support for such institutions is not evidence of broad access. This update follows that specific lead into institutional history and an administrative decision. It adds evidence, rather than changing the original support score.

The immediate question is now: **What evidence distinguishes the existence of state-supported automotive testing infrastructure from a formal arrangement in which several testing institutions can use the same venue? What further evidence would establish access by manufacturers?**

This is a measurement pilot selected because it follows an existing coded passage. It is not a representative sample of policies, a preregistered test, or evidence that political sequencing is necessary for prosperity.

## What was done

1. Separated physical construction, institutional creation, accreditation, listed testing venues, and manufacturer use. These are different observations.
2. Read the 1994 testing-institution rules, the Tianjin center's qualification history, and a retrospective account of the Ministry of Transport's Tongzhou ground. Source quality and chronology are recorded in [sources.md](sources.md) and [timeline.csv](timeline.csv).
3. Extracted only the institution, testing scope and venue fields from the 2005 regulator's table. The notice concerns additional qualifications under **GB1495-2002, stage II, vehicle exterior acceleration noise**. Personal contact fields were excluded.
4. Split venue lists using the source's enumeration separator, preserved original names, and reproduced the counts with [analyze.py](analyze.py). No statistical model was fitted.

## Results

| Venue name as printed | Institutions listing it | Denominator |
|---|---:|---:|
| 交通部公路交通实验场 | 10 | 12 institutions in this notice |
| 东风汽车实验场（襄樊） | 6 | 12 |
| 海南汽车试验研究所 | 5 | 12 |
| 长春农安汽车试验场 | 2 | 12 |

Six institutions list one venue, one lists two, and five list three: **6 × 1 + 1 × 2 + 5 × 3 = 23 links**. Counts overlap, so column totals need not equal 12. These are named venues, not a census of separate physical facilities or all testing institutions in China. Ten out of twelve is a share within this notice, not a share of national tests or market activity.

For example, source row 4 lists Tianjin's testing center against three venues. A testing institution and the location where a test can take place are therefore not interchangeable units. Counting each listed institution as a separate new facility would misread this record.

Historical records also complicate a simple policy-to-construction story. Tianjin's institutional preparation and the Tongzhou ground's early development began before the 1994 industrial policy. Accreditation or completion after 1994 cannot alone show that this policy created the resource. The detailed dates are a retrospective source account; original approval and acceptance documents have not been inspected.

## What has, and has not, been traced

| Evidence layer | Observation | Remaining gap |
|---|---|---|
| Policy intent | 1994 policy provision supports national testing institutions | No identified project funding decision tied to this provision |
| Organizational and physical history | Earlier preparation; later accreditation and construction milestones | Original project records; capacity at each date |
| Formal service governance | 1994 rules distinguish national and group-level institutions, publication of capabilities, reporting and charges | Actual fee schedules, implementation and applicant treatment |
| Specific administrative arrangement | 2005 notice lists multiple institutions against shared venue names | Contracts, bookings, transactions and use intensity |
| Manufacturer access and benefits | Not observed in the new data | Firm identities, eligibility, fees, waiting times, refusals and outcomes |

The 1994 rules and 2005 notice come from different regulatory contexts. Their relevance to a common measurement problem does not establish a legal or causal chain from industrial-policy Article 18. The notice itself cites a 2000 environmental-regulator qualification circular. This study has not traced that circular's full implementation history.

Multiple institutions listing a venue is consistent with resource sharing. It may also reflect regulatory requirements, specialized equipment, administrative concentration or ownership relationships. The table cannot distinguish these explanations. Missing client records are **unknown**, not zero use or proof of exclusion.

**Temporal limit:** this notice is dated **2005-01-26**, despite its `200910` hosting path. It is after China's WTO accession. It cannot define pre-2001 exposure, demonstrate that the arrangement existed before accession, or serve as an exogenous treatment measure.

## Next evidence decision

Focus the next search on one institution–venue pair, beginning with Tianjin and the Ministry of Transport venue. Seek a dated test report or client register connecting a named manufacturer and model to the institution **and** venue. An institution's name on a report without a site is insufficient to establish that link.

Then seek contemporaneous eligibility rules, fee schedules, booking records and rejected applications. Code a manufacturer's entrant/incumbent status using a stated date and definition, not its later success. Annual activity reports are a lead because Article 14 of the 1994 rules called for task and revenue reporting; this does not mean those reports are publicly available.

If only permission records are obtainable, retain a descriptive study of administrative arrangements. Do not relabel it an access or impact study. Before any causal analysis, assess firm coverage, timing, competing changes and a defensible comparison.

## Files and reproduction

- `authorizations.csv`: 12 institution rows; original Chinese text with formatting whitespace removed.
- `institution_venue_links.csv`: 23 links; `source_row` joins to the first file.
- `summary.json`: exact counts and interpretation limits.
- `timeline.csv`: selected historical milestones, source IDs, date precision and evidence type; not an exhaustive institutional history.
- `sources.md`: source URLs, locators, provenance and download fingerprint.
- `validation.json`: source-field comparison, reproduction and invalid-input checks; not independent human review.
- `analyze.py`: extraction, structural validation and deterministic calculation; Python standard library only.

From the repository root:

```bash
python3 research/2026-09-25/analyze.py --check
python3 research/2026-09-25/analyze.py --download --check
# Or use an independently saved copy of the official HTML:
python3 research/2026-09-25/analyze.py --html /path/to/notice.html --check
```

The first command checks calculations from the included transcription; it does not check the source. The other commands re-extract the official table and compare all three output files. The page can change or become unavailable. The source fingerprint records the version retrieved, while the minimal extracted fields remain included for offline reproduction.

Research questions and motivation are the author's. Source search, extraction, calculation and drafting used substantial AI assistance. Reproduction and source checks are not independent methodological review. The findings remain a bounded, exploratory record of formal authorization.
