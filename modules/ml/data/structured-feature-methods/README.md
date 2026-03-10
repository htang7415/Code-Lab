# Structured Feature Methods

> Track: `ml` | Topic: `data`

## Purpose

Use this module to compare the main ways to enrich tabular features without
jumping straight to a large end-to-end model.

## First Principles

- Bucketing turns numeric signals into coarse thresholds.
- Category crosses expose sparse interactions that linear models would otherwise miss.
- Entity embeddings compress high-cardinality identifiers into learned dense vectors.
- These methods answer one design question: should this feature stay numeric, become discrete, or become dense?

## Core Math

- Bucket assignment is a thresholded bin index.
- A category cross forms a joint token such as `city__X__device`.
- Entity embeddings learn a vector lookup table indexed by category ID.

## Minimal Code Mental Model

```python
buckets = bucketize(values, boundaries)
crosses = category_cross_features(left, right)
embedding = pooled_entity_embedding(entity_ids, embedding_table)
```

## Core Functions

```python
def bucketize(values: list[float], boundaries: list[float]) -> list[int]:
def category_cross_features(left: list[str], right: list[str], separator: str = "__X__") -> list[str]:
def pooled_entity_embedding(entity_ids: list[int], embedding_table: list[list[float]]) -> list[float]:
```

## When To Use What

- Use bucketing when threshold effects matter more than exact numeric scale.
- Use category crosses for sparse pairwise interactions in tabular baselines.
- Use entity embeddings when categorical spaces are too wide for one-hot or crosses alone.
- Start with bucketing and crosses before learned embeddings when interpretability matters.

## Run tests

```bash
pytest modules/ml/data/structured-feature-methods/python -q
```
