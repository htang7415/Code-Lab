# Dropout

> Track: `ml` | Topic: `deep-learning`

## Concept

Dropout randomly zeroes activations during training to reduce co-adaptation.

## Math

x' = mask * x / (1-p)

## Function

```python
def dropout(x: list[float], p: float, seed: int = 0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/dropout/python -q
```
