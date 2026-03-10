# Uncertainty

Uncertainty is useful only when it changes a decision, threshold, or deployment policy.

## Current Anchors

- Confidence intervals (`modules/ml/evaluation/confidence-intervals`)
- Bootstrap intervals (`modules/ml/evaluation/bootstrap-intervals`)
- Wilson interval (`modules/ml/evaluation/wilson-interval`)
- Expected calibration error (`modules/ml/evaluation/expected-calibration-error`)
- Brier score (`modules/ml/evaluation/brier-score`)
- Log loss (`modules/ml/evaluation/log-loss`)

## Concepts to Cover Well

- Statistical uncertainty vs predictive uncertainty
- Confidence intervals for estimates and experiments
- Bootstrap intervals when analytic formulas are awkward
- Calibration as uncertainty quality, not just accuracy
- Why overconfident probabilities are dangerous in production
- When uncertainty should gate routing, abstention, or review
