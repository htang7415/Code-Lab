# He Initialization

> Track: `ml` | Topic: `deep-learning`

## Concept

He initialization keeps variance stable for ReLU activations.

## Math

W ~ N(0, 2/fan_in) (demo uses deterministic pseudo-random).

## Function

```python
def he_normal(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/he-initialization/python -q
```
