# Early Stopping

> Track: `ml` | Topic: `deep-learning`

## Concept

Stop training when validation loss stops improving.

## Math

$$t - t_{\text{best}} \ge P$$

- $t$ -- timestep or iteration

## Function

```python
def should_stop(losses: list[float], patience: int) -> bool:
```

## Run tests

```bash
pytest modules/ml/deep-learning/early-stopping/python -q
```
