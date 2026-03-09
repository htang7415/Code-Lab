# Pass@k

> Track: `ml` | Topic: `llm`

## Concept

Pass@k estimates the chance that at least one of the top-$k$ sampled solutions is correct.

## Math

$$\mathrm{pass@}k = 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}$$

- $n$ -- total sampled solutions
- $c$ -- number of correct solutions
- $k$ -- number of attempts considered

## Key Points

- Pass@k increases as either $c$ or $k$ increases.
- If fewer than $k$ incorrect solutions exist, pass@k becomes $1$.
- This is a sampling-based success metric, not token-level likelihood.

## Function

```python
def pass_at_k(total_samples: int, correct_samples: int, k: int) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/pass-at-k/python -q
```
