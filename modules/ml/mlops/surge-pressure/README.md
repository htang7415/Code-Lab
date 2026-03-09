# Surge Pressure

> Track: `ml` | Topic: `mlops`

## Concept

Surge pressure is an overload score that weights large capacity exceedances more heavily than small ones.

## Math

For each observation $x_i$ and capacity $C$, this module accumulates the squared relative excess:

$$
s_i =
\begin{cases}
0 & x_i \le C \\
\left(\frac{x_i - C}{C}\right)^2 & x_i > C
\end{cases}
$$

$$
\mathrm{SurgePressure} = \frac{1}{N} \sum_{i=1}^{N} s_i
$$

## Key Points

- Larger spikes contribute disproportionately more than mild breaches.
- This complements breach-rate style metrics that only count incidents.
- The score is zero when no observation exceeds capacity.

## Function

```python
def surge_pressure(observations: list[float], capacity: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/surge-pressure/python -q
```
