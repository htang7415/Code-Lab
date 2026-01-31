# Debug Overfitting vs Underfitting

> Track: `ml` | Topic: `systems`

## Concept

Compare train vs validation loss to detect fit issues.

## Math

If train << val => overfit; if both high => underfit.

## Function

```python
def diagnose(train_loss: float, val_loss: float) -> str:
```

## Run tests

```bash
pytest modules/ml/systems/debug-overfit-underfit/python -q
```
