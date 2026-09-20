# Exploratory analysis plan, 2026-09-20

Written after reviewing source documentation and repository status, before estimating associations. This is a transparent analysis log, not a preregistration or a causal identification claim.

## Hypotheses to keep separate

1. Prior state capacity predicts subsequent economic performance.
2. Higher capacity before an observed democratization predicts better subsequent performance than lower capacity before an observed democratization.
3. Building capacity before democratization is necessary, or more beneficial than building it under democracy.
4. Autocratic rule, or a historically defined Legalist governing philosophy, causes capacity and is necessary for prosperity.

The planned data can describe 1 and 2; they do not directly identify 3 or 4. No indicator will be named 'Legalism'. Singapore and countries without a transition must not be assigned a fictitious transition date. Do not select countries on economic success or on remaining democratic afterward.

## Data and scope

- Hanson & Sigman state capacity v1 (1960–2015), including original capacity estimates, uncertainty and public-administration component.
- Acemoglu, Naidu, Restrepo & Robinson (DDCG) original replication data, using its regime coding and GDP series as documented. This is a new exploratory merge, not a replication of their causal estimates.
- If obtainable, Maddison Project Database 2023 through 2022, for longer outcome windows and GDP-source sensitivity. Preserve source versions; do not splice GDP levels between datasets.
- Use all eligible countries for estimation; show an East/Southeast Asian case comparison for the user's motivation. Exclusions and unavailable cases will be exported.

## Outcomes and main comparisons

- Primary outcome: annualized log real GDP per capita change from the year before transition to ten years later (exactly ten calendar years).
- Secondary: twenty-year annualized log change, subsequent negative-growth years, and a public-administration rather than composite-capacity specification.
- Capacity: mean in the five full years before transition. Require five observed years; do not use post-transition capacity to define exposure. Use a continuous score for regressions; a contemporaneous world median split is descriptive only, not a validated threshold for a capable state.
- Main transition sample: first observed 0→1 change preceded by five consecutive observed non-democratic years, from 1965 onward. No requirement of future democratic survival. Report repeated transitions separately if used as sensitivity, clustered by country.
- Models: raw association; adjusted for pre-transition log income and transition year; then add prior ten-year growth where available. Show estimates and 95% uncertainty, not only significance. Never interpret adjusted associations as causal.
- All-country comparison: non-overlapping decade baseline cohorts with capacity, democracy, initial income and subsequent ten-year growth; include cohort effects, then country effects with country-clustered uncertainty. Capacity×democracy is a descriptive interaction, not a test of historical sequencing.
- Sensitivity: exclude Korea/Taiwan, leave one country out, alternative capacity component, alternative GDP source and twenty-year horizon where possible. Differences in sample composition must be explicit.

## Limits to report

Selection into democratization, baseline income, prior growth, human capital, wars, colonial legacies, international support, trade opportunities, resource dependence, survival/border changes, measurement error and incomplete historical coverage all remain potential explanations. A composite that includes coercive and extractive capacity is not identical to coordination or administrative competence. Temporal ordering of regressors does not remove endogeneity or latent-model retrospective information. Ten/twenty-year GDP growth is not equivalent to enduring, inclusive prosperity.

## Existing project

Audit the current GitHub snapshot separately: historical policy-text measurement and China WTO outcomes are a different unit and transition from national democratization. Existing synthetic outputs are not empirical findings. Existing raw patent pulls may support descriptive checks only; broad categories, provenance and pre-trends require examination before any interpretation.

## Logged amendments after the first calculation

- The two GDP sources produced different association magnitudes. Add fixed-common-sample comparisons swapping the GDP outcome and initial-income control separately; also examine MPD twenty-year results with prior growth, with the administration component, and without Korea/Taiwan. These are diagnostic, exploratory additions, not a new confirmatory test. All coefficients are retained.
- Entity audit found that HS uses CZE for Czechoslovakia before 1993 and Czech Republic afterward, whereas DDCG uses Czech Republic. Exclude pre-capacity windows crossing this predecessor/successor boundary rather than assigning Czechoslovakia's capacity to Czech Republic. This reduces the initial 58-country ten-year sample by one. This is a data-integrity correction, unrelated to the result's direction.
- HS has 177 named entities with capacity estimates but 175 distinct ISO-like codes, because CZE and YGS each represent more than one named historical entity. Preserve named entities and years; country codes alone are not sufficient historical identities. SER is not automatically mapped to SRB. Other border changes remain a substantive historical limitation.
- Taiwan's regime sequence is present in DDCG under TAW, but its GDP outcome is missing. It enters MPD analyses only. The DDCG 'excluding Korea/Taiwan' sensitivity therefore removes only Korea.
- GDP-source audit found a large sign discrepancy for Mozambique (1993–2003). The MPD Stata values match its independently downloaded Excel release, so this is not a local reshaping error. Add a current World Bank constant-price GDP-per-capita series (NY.GDP.PCAP.KD, 1960–2024), matching the same country cohorts before comparing sources. This is an exploratory source diagnostic added after seeing the discrepancy. Do not drop countries because their growth looks surprising or selectively present the stronger MPD association.
