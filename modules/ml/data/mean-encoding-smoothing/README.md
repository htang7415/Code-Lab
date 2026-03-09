# Mean Encoding Smoothing

> Track: `ml` | Topic: `data`

## Concept

Mean encoding smoothing pulls category means toward the global mean so rare categories do not overfit as aggressively.

## Math

$$
\mathrm{enc}(c) = \frac{\sum_{i:x_i=c} y_i + m \mu}{N_c + m}
$$

- $N_c$ -- number of examples for category $c$
- $\mu$ -- global mean target
- $m$ -- smoothing strength

## Key Points

- This is a regularized follow-on to raw target encoding.
- Larger smoothing values pull categories more strongly toward the global mean.
- The module returns the smoothed category map only; fold-safe computation is still the user’s responsibility.

## Function

```python
def smoothed_mean_encoding_map(categories: list[str], targets: list[float], smoothing: float) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/data/mean-encoding-smoothing/python -q
```
