# Embeddings

Embeddings turn raw or discrete inputs into dense vectors whose geometry can be searched, compared, and reused.

## Purpose

Use this page to understand:
- what an embedding is
- why embedding geometry matters
- when similarity, retrieval, and transfer all depend on the same vector space

## First Principles

- An embedding maps input $x$ to a vector $z = f(x)$.
- The goal is not compression alone; it is useful geometry.
- Similar inputs should become nearby when the downstream task depends on similarity.
- Normalization changes the meaning of distance, especially for cosine-based retrieval.

## Core Math

- Embedding map:
  $$
  z = f(x)
  $$
- Cosine similarity:
  $$
  \frac{z_1^\top z_2}{\|z_1\|\|z_2\|}
  $$

## Minimal Code Mental Model

```python
z_query = encoder(query)
z_doc = encoder(doc)
score = cosine_similarity(z_query, z_doc)
```

## Canonical Modules

- Core embedding idea: `embeddings`
- Similarity geometry: `cosine-similarity`
- Compression baseline: `autoencoder`

## Supporting Modules

- Metric-learning losses: `contrastive-loss`, `triplet-loss`, `pairwise-ranking-loss`

## When To Use What

- Start with `embeddings` and cosine similarity before metric-learning losses.
- Use `autoencoder` when the main question is compression or latent structure, not retrieval ranking.
- Use metric-learning losses only when pair, triplet, or preference structure is explicit in the data.
