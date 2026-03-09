# Importance Sampling Estimate

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Importance sampling reweights samples collected from one distribution so they estimate an expectation under another distribution.

## Math

$$\hat{\mu} = \frac{1}{n} \sum_{i=1}^{n} r_i \frac{\pi(a_i \mid s_i)}{b(a_i \mid s_i)}$$

- $r_i$ -- reward or sampled outcome
- $\pi(a_i \mid s_i)$ -- target-policy probability
- $b(a_i \mid s_i)$ -- behavior-policy probability
- $n$ -- number of samples

## Key Points

- Importance sampling is central to off-policy evaluation.
- Large weights can cause high variance.
- This module uses the ordinary, unnormalized estimator.

## Function

```python
def importance_sampling_estimate(
    rewards: list[float],
    target_probs: list[float],
    behavior_probs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/importance-sampling/python -q
```
