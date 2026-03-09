# Log Loss

> Track: `ml` | Topic: `evaluation`

## Concept

Log loss penalizes confident wrong probability predictions more harshly than mild mistakes.

## Math

$$
\mathrm{LogLoss} = -\frac{1}{n} \sum_{i=1}^{n} \left( y_i \log p_i + (1-y_i)\log(1-p_i) \right)
$$

- $y_i$ -- binary label
- $p_i$ -- predicted probability of the positive class
- $n$ -- number of examples

## Key Points

- Lower is better.
- This is a standard probabilistic classification loss.
- It complements accuracy and calibration metrics by using full probabilities.

## Function

```python
def log_loss(labels: list[int], probabilities: list[float], eps: float = 1.0e-15) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-loss/python -q
```
