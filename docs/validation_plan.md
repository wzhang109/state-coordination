## Validation Plan

This document outlines a validation workflow for AI-assisted measurement. The purpose is to increase scale while preserving auditability.

### 1. Hand-coded benchmark

Create a benchmark sample of passages coded by a human reviewer before using machine-assisted scores.

Recommended stratification:

- sector
- decade or period
- document type
- coding dimension
- expected difficulty level

### 2. Evaluation metrics

At minimum, report:

- exact agreement with benchmark labels
- agreement within one score point
- confusion matrix by dimension
- disagreement rate by document type
- examples of false positives and false negatives

### 3. Error typology

Classify recurring errors, such as:

- confusing broad macro policy with sector-specific support
- mistaking rhetorical goals for implementation instruments
- failing to distinguish broad coordination from incumbent-directed allocation
- over-scoring documents with vague technology or modernization language
- missing support embedded in legal or administrative terminology

### 4. Human review rules

Route cases to human review when:

- model confidence is low;
- evidence is indirect or ambiguous;
- passage involves multiple sectors;
- passage involves allocation to named firms or incumbents;
- model output conflicts with the coding rubric.

### 5. Reporting

A validation memo should summarize:

- benchmark design;
- model/prompt version;
- performance by dimension;
- major error patterns;
- examples of corrected cases;
- implications for index construction.

### 6. Weighting and sensitivity

The four dimensions are currently equal-weighted (0.25 each). This is a default under no prior information about relative importance, not a substantive claim.

Planned sensitivity checks, to be run once sector coverage is sufficient (n >= 8):

1. **Leave-one-dimension-out.** Recompute the index four times, each time dropping one dimension. Report how sector rankings change.
2. **Perturbation.** Draw 1,000 weight vectors from a Dirichlet(1,1,1,1) distribution. Report the share of draws under which the main qualitative conclusion is unchanged.
3. **Theory-motivated alternative.** Report the index under at least one weighting derived from the mechanism rather than convenience — for example up-weighting network breadth and allocation, the two dimensions that distinguish the capacity-building hypothesis from the incumbent-entrenchment hypothesis.

A result that survives (1) and holds in more than 90% of (2) is reported as robust. A result that does not is reported as weight-dependent, not suppressed.

### 7. Reliability

Current status: single coder (wenwen_zhang), AI-assisted first pass with human review.

Reliability evidence, in order of strength:

1. **AI-draft vs human-final disagreement rate.** Recoverable from prompt logs where the model's initial score was recorded. Reported as a check on whether machine assistance is being rubber-stamped rather than reviewed.
2. **Test-retest (intra-coder).** Blind recode of a random subsample after a minimum seven-day gap, with scores and notes masked. Reported as exact agreement, within-one agreement, and quadratic-weighted Cohen's kappa. Quadratic weighting is used because the scores are ordinal: coding a 2 as a 1 is a smaller error than coding it as a 0.
3. **Independent second coder.** Planned; not yet available.

Dimension-level disagreement is treated diagnostically. Any dimension falling below kappa 0.60 triggers a rubric revision, logged with date and reason.

### 8. Identifying assumption and pre-trends

The event-study specification identifies effects under a parallel-trends assumption: absent the transition, sectors with different pre-transition support scores would have followed parallel paths in the outcome variable.

Pre-period coefficients (k < -1, with k = -1 omitted as reference) are the test of that assumption, not decoration. They are reported individually and as a joint test.

If pre-trends are present, the planned responses, in order:

1. Report results as descriptive associations rather than causal effects.
2. Narrow the event window to the periods over which pre-trends are flat.
3. Add sector-specific linear trends and report both specifications side by side.

None of these is treated as a way to recover a causal claim. They are ways to report honestly what the data does and does not support.
