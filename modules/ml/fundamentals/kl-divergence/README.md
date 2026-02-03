# KL Divergence

> Track: `ml` | Topic: `fundamentals`

## Concept

KL divergence measures how one distribution diverges from another.

## Math

$$\mathrm{KL}(p\|q) = \sum_i p_i \log\left(\frac{p_i}{q_i}\right)$$

- $\mathrm{KL}$ -- Kullback-Leibler divergence
- $p_i$ -- i-th probability
- $q_i$ -- i-th probability distribution
- $p$ -- probability
- $q$ -- probability distribution
- $i$ -- index

## Function

```python
def kl(p: list[float], q: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/kl-divergence/python -q
```
