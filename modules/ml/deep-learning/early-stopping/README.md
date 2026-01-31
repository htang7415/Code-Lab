# Early Stopping

> Track: `ml` | Topic: `deep-learning`

## Concept

Stop training when validation loss stops improving.

## Math

Stop if best_loss hasn't improved for patience steps.

## Function

```python
def should_stop(losses: list[float], patience: int) -> bool:
```

## Run tests

```bash
pytest modules/ml/deep-learning/early-stopping/python -q
```
