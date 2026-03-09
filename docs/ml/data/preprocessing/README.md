# Data Preprocessing

Preprocessing decides whether downstream models learn signal or shortcuts.

## Current Anchors

- Data leakage (`modules/ml/data/data-leakage`)
- Feature scaling (`modules/ml/data/feature-scaling`)
- Robust scaling (`modules/ml/data/robust-scaling`)
- Polynomial features (`modules/ml/data/polynomial-features`)
- Count-vector lexical baseline (`modules/ml/data/count-vectorizer`)
- TF-IDF lexical features (`modules/ml/data/tf-idf`)
- Hash trick for fixed-width sparse features (`modules/ml/data/hash-trick`)
- Chi-square feature scoring for sparse features (`modules/ml/data/chi-square-feature-selection`)
- Frequency encoding for categorical counts (`modules/ml/data/frequency-encoding`)
- Target encoding for high-cardinality categories (`modules/ml/data/target-encoding`)
- Rare-category grouping for long-tail categoricals (`modules/ml/data/rare-category-grouping`)
- Weight-of-evidence encoding (`modules/ml/data/weight-of-evidence`)
- Smoothed mean encoding (`modules/ml/data/mean-encoding-smoothing`)
- Category cross features (`modules/ml/data/category-cross-features`)
- Entity embeddings for categorical IDs (`modules/ml/data/entity-embedding-intuition`)
- Class imbalance (`modules/ml/data/class-imbalance`)
- Missing-data imputation (`modules/ml/data/imputation`)
- Missing-value indicators (`modules/ml/data/missing-indicator`)
- SMOTE-style synthetic oversampling (`modules/ml/data/smote`)
- Z-score outlier screening (`modules/ml/data/outlier-detection`)

## Concepts to Cover Well

- Scaling and normalization choices
- Robust alternatives when z-score scaling is too sensitive
- Label encoding and one-hot encoding
- Count vectors as the simplest bag-of-words baseline
- Text feature extraction such as TF-IDF
- Vocabulary-free hashing for large sparse feature spaces
- Chi-square filtering for sparse lexical or one-hot features
- Frequency encoding as a label-free categorical baseline
- Target encoding and the leakage risk around per-category means
- Rare-category grouping before downstream encodings
- Weight of evidence as a supervised categorical transformation
- Smoothing category means toward the global target average
- Category crosses for sparse interaction features
- Dense entity embeddings as a learned alternative to very wide one-hot features
- Missing-value handling and its failure modes
- Missingness indicators alongside imputation
- Outlier handling and when simple z-score rules fail
- Class imbalance remedies such as weighting, resampling, and SMOTE
