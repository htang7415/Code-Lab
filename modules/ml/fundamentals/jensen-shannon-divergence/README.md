# Jensen–Shannon Divergence

> Track: `ml` | Topic: `fundamentals`

## Concept

JS divergence symmetrizes KL using the mean distribution.

## Math
$$\mathrm{JS}(p,q)=\tfrac{1}{2}\mathrm{KL}(p\|m)+\tfrac{1}{2}\mathrm{KL}(q\|m),\quad m=\tfrac{1}{2}(p+q)$$

- $\mathrm{KL}$ -- Kullback-Leibler divergence
- $p$ -- probability
- $q$ -- probability distribution
- $m$ -- number of features/units

## Function

```python
def js(p: list[float], q: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/jensen-shannon-divergence/python -q
```