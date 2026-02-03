# Cosine Similarity

> Track: `ml` | Topic: `fundamentals`

## Concept

Cosine similarity measures angle between vectors.

## Math
$$\cos(\theta) = \frac{a \cdot b}{\lVert a \rVert \lVert b \rVert}$$

- $a$ -- vector $a$
- $b$ -- vector $b$
- $\theta$ -- angle between vectors

## Function

```python
def cosine_similarity(a: list[float], b: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/cosine-similarity/python -q
```