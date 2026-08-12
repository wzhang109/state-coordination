# Coding Rubric: State Support Index

The State Support Index is intended to measure **pre-transition organizational support**, not state capacity itself. Each score must be traceable to a source passage.

## Unit of coding

- Sector-year-dimension cell
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
allocation under the original rubric, but they predict opposite outcomes.

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
