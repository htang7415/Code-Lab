# Covariance

> Track: `ml` | Topic: `fundamentals`

## Concept

Covariance measures how two variables vary together.

## Math

$$\mathrm{cov}(X,Y)=\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]$$

## Function

```python
def covariance(x: list[float], y: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/covariance/python -q
```
