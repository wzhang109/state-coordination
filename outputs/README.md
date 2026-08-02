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
