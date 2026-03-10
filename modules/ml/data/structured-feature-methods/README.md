# Structured Feature Methods

> Track: `ml` | Topic: `data`

## Concept

Structured feature methods turn raw tabular fields into representations that simpler models can use more effectively.
This family groups three common moves:

- bucket numeric values into discrete bins
- cross categories to expose sparse interactions
- replace high-cardinality IDs with dense entity embeddings

## Why Learn Them Together

- Bucketing creates coarse thresholds from continuous signals.
- Crosses let linear models capture pairwise interactions.
- Entity embeddings compress wide categorical spaces into dense learned vectors.

These methods sit on the same design path: choose whether a feature should stay numeric, become discrete, or become dense.

## Core Functions

```python
def bucketize(values: list[float], boundaries: list[float]) -> list[int]:
def category_cross_features(left: list[str], right: list[str], separator: str = "__X__") -> list[str]:
def pooled_entity_embedding(entity_ids: list[int], embedding_table: list[list[float]]) -> list[float]:
```

## Comparison

| Method | Best for | Output |
| --- | --- | --- |
| Bucketing | Simple threshold effects | bucket indices |
| Category crosses | Sparse pairwise interactions | crossed categorical tokens |
| Entity embeddings | High-cardinality learned representations | dense vectors |

## Key Points

- Start with bucketing and crosses when you want interpretable tabular baselines.
- Move to entity embeddings when one-hot or cross spaces get too wide.
- Bucketing often pairs naturally with crosses because bins can act like categories.
- Dense embeddings help when IDs have many repeated observations and enough data to learn useful structure.

## Run tests

```bash
pytest modules/ml/data/structured-feature-methods/python -q
```
