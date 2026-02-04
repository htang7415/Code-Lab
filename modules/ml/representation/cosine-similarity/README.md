# Cosine Similarity

> Track: `ml` | Topic: `representation`

## Concept

Cosine similarity measures the angle between two vectors.
It is scale-invariant and widely used for embedding retrieval.

## Math

$$
\text{cosine}(a, b) = \frac{a \cdot b}{\|a\|\|b\|}
$$

## Function

```python
def cosine_similarity(a: list[float], b: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/representation/cosine-similarity/python -q
```
