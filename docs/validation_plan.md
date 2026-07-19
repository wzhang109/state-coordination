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
