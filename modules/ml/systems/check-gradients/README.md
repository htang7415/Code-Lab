# Check Gradients Are Flowing

> Track: `ml` | Topic: `systems`

## Concept

Check that gradients are non-zero and finite.

## Math

ok if any(|g| > 0) and no NaN

## Function

```python
def gradients_ok(grads: list[float]) -> bool:
```

## Run tests

```bash
pytest modules/ml/systems/check-gradients/python -q
```
