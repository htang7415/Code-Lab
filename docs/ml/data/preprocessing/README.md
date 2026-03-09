# Data Preprocessing

Preprocessing decides whether downstream models learn signal or shortcuts.

## Current Anchors

- Data leakage (`modules/ml/data/data-leakage`)
- Polynomial features (`modules/ml/data/polynomial-features`)
- Class imbalance (`modules/ml/data/class-imbalance`)
- Missing-data imputation (`modules/ml/data/imputation`)
- SMOTE-style synthetic oversampling (`modules/ml/data/smote`)

## Concepts to Cover Well

- Scaling and normalization choices
- Label encoding and one-hot encoding
- Missing-value handling and its failure modes
- Outlier handling
- Class imbalance remedies such as weighting, resampling, and SMOTE
