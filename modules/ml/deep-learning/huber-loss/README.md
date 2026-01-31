# Huber Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Huber loss is quadratic near zero and linear for large errors.

## Math

$$
L =
\begin{cases}
\frac{1}{2} e^2, & |e| \le \delta \\
\delta\left(|e| - \frac{1}{2}\delta\right), & \text{otherwise}
\end{cases}
$$

## Function

```python
def huber(y: float, y_hat: float, delta: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/huber-loss/python -q
```
