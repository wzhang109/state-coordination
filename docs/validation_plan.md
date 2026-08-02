# Validation Plan

This document outlines a validation workflow for AI-assisted measurement. The purpose is to increase scale while preserving auditability.

## 1. Hand-coded benchmark

Create a benchmark sample of passages coded by a human reviewer before using machine-assisted scores.

Recommended stratification:

- sector
- decade or period
- document type
- coding dimension
- expected difficulty level

## 2. Evaluation metrics

At minimum, report:

- exact agreement with benchmark labels
- agreement within one score point
- confusion matrix by dimension
- disagreement rate by document type
- examples of false positives and false negatives

## Weighting and sensitivity

The four dimensions are currently equal-weighted (0.25 each). This is a default choice
under no prior information about relative importance, not a substantive claim.

Planned sensitivity checks, to be run once sector coverage is sufficient (n >= 8):

1. **Leave-one-dimension-out.** Recompute the index four times, each time dropping one
   dimension. Report how sector rankings change.
2. **Perturbation.** Draw 1,000 weight vectors from a Dirichlet(1,1,1,1) distribution.
   Report the share of draws under which the main qualitative conclusion is unchanged.
3. **Theory-motivated alternatives.** Report the index under at least one weighting
   derived from the mechanism rather than convenience — e.g. up-weighting network
   breadth and allocation, which are the two dimensions that distinguish the
   capacity-building hypothesis from the incumbent-entrenchment hypothesis.

A result that survives (1) and holds in >90% of (2) is reported as robust. A result
that does not is reported as weight-dependent, not suppressed.

## 3. Error typology

Classify recurring errors, such as:

- confusing broad macro policy with sector-specific support
- mistaking rhetorical goals for implementation instruments
- failing to distinguish broad coordination from incumbent-directed allocation
- over-scoring documents with vague technology or modernization language
- missing support embedded in legal or administrative terminology

## 4. Human review rules

Route cases to human review when:

- model confidence is low;
- evidence is indirect or ambiguous;
- passage involves multiple sectors;
- passage involves allocation to named firms or incumbents;
- model output conflicts with the coding rubric.

## 5. Reporting

A validation memo should summarize:

- benchmark design;
- model/prompt version;
- performance by dimension;
- major error patterns;
- examples of corrected cases;
- implications for index construction.
