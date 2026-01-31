# Xavier/Glorot Initialization

> Track: `ml` | Topic: `deep-learning`

## Concept

Xavier init keeps variance stable for symmetric activations.

## Math

W ~ U(-sqrt(6/(fan_in+fan_out)), sqrt(6/(fan_in+fan_out))).

## Function

```python
def xavier_uniform(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/xavier-initialization/python -q
```
