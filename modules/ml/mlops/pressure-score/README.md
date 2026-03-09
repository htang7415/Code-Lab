# Pressure Score

> Track: `ml` | Topic: `mlops`

## Concept

Pressure score combines overload incidence and normalized overload margin into one serving-stress proxy.

## Math

For each observation $x_i$ and capacity $C$:

$$
s_i =
\begin{cases}
0 & x_i \le C \\
1 + \frac{x_i - C}{C} & x_i > C
\end{cases}
$$

$$
\mathrm{PressureScore} = \frac{1}{N} \sum_{i=1}^{N} s_i
$$

## Key Points

- A score of `0` means no overload at all.
- Crossing capacity contributes at least `1 / N` per breach, with extra penalty for larger overruns.
- This module is a compact overload summary, not a standard industry metric.

## Function

```python
def pressure_score(observations: list[float], capacity: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/pressure-score/python -q
```
