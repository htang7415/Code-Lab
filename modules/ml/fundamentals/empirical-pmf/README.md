# Empirical PMF

> Track: `ml` | Topic: `fundamentals`

## Concept

An empirical probability mass function estimates the probabilities of discrete
outcomes directly from observed counts in data.

## Math

$$p(x)=count(x)/N$$

- $p(x)$ -- estimated probability of outcome $x$
- $\mathrm{count}(x)$ -- number of times outcome $x$ appears in the sample
- $N$ -- total number of observations

## Key Points

- The empirical PMF is a plug-in estimate from data, not a parametric model.
- Probabilities sum to 1 because counts sum to $N$.
- More data usually makes the empirical estimate more stable.

## Function

```python
def empirical_pmf(samples: list[int]) -> dict[int, float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/empirical-pmf/python -q
```
