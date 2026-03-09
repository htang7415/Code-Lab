# Log Prevalence Ratio

> Track: `ml` | Topic: `evaluation`

## Concept

Log prevalence ratio takes the logarithm of a multiplicative prevalence comparison.

## Math

$$
\log \mathrm{PR} = \log\left(\frac{p_A}{p_B}\right)
$$

- $p_A$ -- positive rate of group A
- $p_B$ -- positive rate of group B

## Key Points

- Log ratios turn multiplicative effects into additive ones.
- A value of `0` means the two groups have the same positive rate.
- This module returns infinities when one rate is zero and the other is positive.

## Function

```python
def log_prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-prevalence-ratio/python -q
```
