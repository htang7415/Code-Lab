# Embeddings

> Track: `ml` | Topic: `representation`

## Concept

Embeddings map discrete items (tokens, documents, users) to dense vectors.
Similar items land near each other in vector space.

## Math

$$z = \frac{1}{n}\sum_{i=1}^n e_i$$

- $e_i$ -- embedding vector for token $i$
- $z$ -- pooled (sentence-level) embedding

## Function

```python
def mean_pool(embeddings: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/representation/embeddings/python -q
```
