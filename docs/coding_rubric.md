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

## Ambiguous cases

Ambiguous or low-confidence cases should be routed to human review. Scores should not be finalized only from machine-generated outputs.
