# Coding Rubric: State Support Index

The State Support Index is intended to measure **pre-transition organizational support**, not state capacity itself. Each score must be traceable to a source passage.

## Unit of coding

- The stored coding row links one source passage to one dimension; a passage can support several rows.
- Sector-year-dimension cells are aggregation targets, not independent observations of policy implementation.
- Supporting evidence: archival passage, law, industrial plan, policy directive, R&D mandate, or sectoral development document

## Dimensions

### 1. Persistence

How durable and repeated was state support for a sector before the transition?

- `0`: no clear recurring support
- `1`: occasional or short-lived support
- `2`: repeated or institutionalized support across multiple years or documents

### 2. Specificity

How targeted was the policy support?

- `0`: broad macro or economy-wide language only
- `1`: sector-relevant but not highly specific
- `2`: sector-specific policy, target, mandate, or implementation instrument

### 3. Network breadth

How many types of organizations were connected by the policy framework?

- `0`: no clear organizational network
- `1`: one or two organization types, such as ministry-firm or ministry-bank
- `2`: broader network involving ministries, firms, banks, research institutes, technology agencies, or industry associations

### 4. Allocation

Did support appear broadly capacity-building or incumbent-directed?

- `0`: no allocation mechanism identified
- `1`: broad support or general sectoral capacity-building
- `2`: targeted allocation to selected firms, incumbents, or privileged organizations

## Direction (allocation only)

Added 2026-08-12, after the first real coded batches revealed that the allocation
dimension was collapsing two opposite mechanisms into one score.

State control over entry can be **protective** (restricting entry to preserve
selected incumbents, as in the 1994 automotive policy's suspension of new
passenger-vehicle approvals) or **compressive** (restricting capacity to force
contraction, as in the 1998 textile spindle-reduction program). Both score 2 on
allocation under the original rubric. Their intended directions differ, but the signs and distribution of actual effects are empirical questions; they need not be opposite.

`direction` is recorded separately rather than folded into the score, so the index
can be computed with or without the distinction and the two can be compared.

Values: `protective` | `compressive` | `neutral` (blank for non-allocation rows)

## Required evidence fields

Each coded passage should include:

- `source_id`
- `sector`
- `year`
- `dimension`
- `score`
- `passage_excerpt`
- `coder_id`
- `confidence`
- `review_status`
- `notes`
- `direction` (allocation rows only; see above)

## Ambiguous cases

Ambiguous or low-confidence cases should be routed to human review. Scores should not be finalized only from machine-generated outputs.

## Interpretation note — 20 September 2026

This is the existing rubric version. Scores and coded batches are preserved. Allocation=2 can denote selective privilege, so a higher aggregate support score is not necessarily greater productive capacity. The [narrowed question](current_research_question.md) proposes separate beneficiary and access fields; they are not yet coded or validated. Do not infer policy quality from later outcomes.


## Evidence note — follow-up review, 20 September 2026

A network-breadth score does not establish open eligibility or actual use. For example, SRC_AUTO_1994_006 proposes research/testing institutions; its existing note interprets these as shared, but the excerpt does not document access by new firms. Similarly, a formal approval restriction can identify a rule without estimating incumbent gains. Original scores and notes are retained for traceability; their implementation and effect interpretations remain review questions. The [understanding guide](study_guide.zh-CN.md) uses these records to practice the distinction.
