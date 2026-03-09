# Entity Embedding Intuition

> Track: `ml` | Topic: `data`

## Concept

Entity embeddings replace high-cardinality categorical IDs with learned dense vectors, and multiple IDs can be pooled into one compact feature.

## Math

$$
\mathbf{z} = \frac{1}{m} \sum_{i=1}^{m} \mathbf{e}_{id_i}
$$

- $\mathbf{e}_{id_i}$ -- embedding vector for category ID $id_i$
- $m$ -- number of IDs being pooled

## Key Points

- Dense embeddings are a learned alternative to very wide one-hot features.
- Pooling gives a fixed-width representation even when multiple categories are present.
- This module focuses on lookup plus mean pooling, not training the embeddings.

## Function

```python
def pooled_entity_embedding(entity_ids: list[int], embedding_table: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/data/entity-embedding-intuition/python -q
```
