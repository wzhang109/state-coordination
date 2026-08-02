# Outputs folder

Generated output files from the demo scripts:

- `event_study_coefficients.csv`
- `event_study_plot.png`

These outputs are based on synthetic data and are for workflow demonstration only.

### Identifying assumption

The event-study specification identifies effects under a parallel-trends assumption:
absent the transition, sectors with different pre-transition support scores would have
followed parallel paths in the outcome variable.

Pre-period coefficients (k < -1, with k = -1 omitted as reference) are the test of
this assumption, not decoration. If they are jointly indistinguishable from zero, the
assumption is supported. If they trend, the design does not identify a causal effect
and the results are reported as descriptive rather than causal.

### Current scale and what it supports

Real coded data currently covers 2 sectors. The event-study specification in
`scripts/02_` requires many more clusters for valid inference and is retained as a
demonstration of the intended workflow, not as an estimation of the current sample.
At present the repository supports descriptive measurement and documentation of
institutional continuity, not causal estimation.
