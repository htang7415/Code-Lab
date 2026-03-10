# Metric Learning

Metric learning shapes an embedding space so distance directly reflects similarity or preference.

## Purpose

Use this page to compare the main metric-learning setups:
- pair-based objectives
- triplet objectives
- preference-style ranking losses

## First Principles

- Classification predicts labels; metric learning predicts geometry.
- The training signal says which examples should move together and which should move apart.
- Good metric learning depends on meaningful positives, negatives, or ordered preferences.
- Hard examples matter because easy negatives rarely shape the space enough.

## Core Math

- Contrastive-style pull/push idea:
  $$
  d(z_i, z_j)
  $$
  should be small for positives and large for negatives.
- Triplet margin shape:
  $$
  \max(0, d(a,p) - d(a,n) + m)
  $$
- Pairwise ranking prefers the chosen score over the rejected score.

## Minimal Code Mental Model

```python
z_anchor = encoder(anchor)
z_positive = encoder(positive)
z_negative = encoder(negative)
loss = triplet_loss(z_anchor, z_positive, z_negative)
```

## Canonical Modules

- Pair-based learning: `contrastive-loss`
- Triplet geometry: `triplet-loss`
- Preference ordering: `pairwise-ranking-loss`
- Similarity baseline: `cosine-similarity`

## When To Use What

- Use `contrastive-loss` when you have positive and negative pairs.
- Use `triplet-loss` when anchor-positive-negative structure is natural.
- Use `pairwise-ranking-loss` when the main supervision is preference or ordered relevance.
- Use cosine similarity as the simplest baseline before more complex metric-learning setups.
