# KL Divergence

> Track: `ml` | Topic: `fundamentals`

## Concept

KL divergence measures how one distribution diverges from another.

## Math

$$\mathrm{KL}(p\|q) = \sum_i p_i \log\left(\frac{p_i}{q_i}\right)$$

If some $p_i > 0$ while $q_i = 0$, then $\mathrm{KL}(p\|q) = \infty$.

- $\mathrm{KL}$ -- Kullback-Leibler divergence
- $p_i$ -- i-th probability
- $q_i$ -- i-th probability under $q$
- $p$ -- source distribution
- $q$ -- reference distribution
- $i$ -- index

## Function

```python
def kl(p: list[float], q: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/kl-divergence/python -q
```
