# DDPM Reverse Mean Step

> Track: `ml` | Topic: `generative`

## Concept

DDPM sampling reverses the forward noising process one step at a time.
This module computes the mean of the reverse transition before optional Gaussian noise is added.

## Math

$$\mu_\theta(x_t, t) = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, t) \right)$$

- $x_t$ -- noisy sample at step $t$
- $\epsilon_\theta(x_t, t)$ -- predicted noise at step $t$
- $\alpha_t$ -- per-step signal retention
- $\bar{\alpha}_t$ -- cumulative signal retention up to step $t$
- $\beta_t$ -- per-step noise variance
- $\mu_\theta$ -- mean of the reverse transition

## Key Points

- The denoiser predicts noise, not the clean sample directly in the basic DDPM formulation.
- Sampling uses many reverse steps, which is why vanilla diffusion is slow.
- This module models only the mean update, not the stochastic variance term.

## Function

```python
def ddpm_reverse_mean(
    x_t: float,
    predicted_noise: float,
    alpha_t: float,
    alpha_bar_t: float,
    beta_t: float,
) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/ddpm-sampling/python -q
```
