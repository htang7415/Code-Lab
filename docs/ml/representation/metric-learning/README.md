# Metric Learning

Metric learning shapes a representation space so that distance directly reflects semantic similarity or preference.

## Current Anchors

- Contrastive loss (`modules/ml/representation/contrastive-loss`)
- Pairwise ranking loss (`modules/ml/representation/pairwise-ranking-loss`)
- Triplet loss (`modules/ml/representation/triplet-loss`)
- Cosine similarity (`modules/ml/fundamentals/cosine-similarity`)

## Concepts to Cover Well

- Positive and negative pairs vs anchor-positive-negative triplets
- Margin-based separation objectives
- Cosine-normalized embeddings for retrieval
- Hard negative mining and collapse risk
- The difference between metric learning and supervised classification
