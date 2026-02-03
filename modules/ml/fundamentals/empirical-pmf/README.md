# Empirical PMF

> Track: `ml` | Topic: `fundamentals`

## Concept

Empirical PMF estimates probability from samples.

## Math

$$p(x)=count(x)/N$$

- $p$ -- probability
- $x$ -- input (feature vector or sample)

- $N$ -- number of samples

## Function

```python
def empirical_pmf(samples: list[int]) -> dict[int, float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/empirical-pmf/python -q
```
