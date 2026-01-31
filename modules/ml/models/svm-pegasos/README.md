# SVM (Pegasos)

> Track: `ml` | Topic: `models`

## Concept

Pegasos is a stochastic subgradient method for SVMs.

## Math

$$
w \leftarrow
\begin{cases}
(1-\text{lr}\,\lambda)w + \text{lr}\, y x, & y(w^\top x) < 1 \\
(1-\text{lr}\,\lambda)w, & \text{otherwise}
\end{cases}
$$

## Function

```python
def pegasos_step(w: list[float], x: list[float], y: int, lr: float, lam: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/svm-pegasos/python -q
```
