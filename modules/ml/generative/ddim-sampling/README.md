# DDIM Deterministic Step

> Track: `ml` | Topic: `generative`

## Concept

DDIM sampling reuses the diffusion denoiser but takes a deterministic update, which can produce good samples with fewer steps than vanilla DDPM.

## Math

$$\hat{x}_0 = \frac{x_t - \sqrt{1 - \bar{\alpha}_t}\,\epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}}$$

$$x_{t-1} = \sqrt{\bar{\alpha}_{t-1}}\,\hat{x}_0 + \sqrt{1 - \bar{\alpha}_{t-1}}\,\epsilon_\theta(x_t, t)$$

- $x_t$ -- noisy sample at the current step
- $\hat{x}_0$ -- estimated clean sample
- $\epsilon_\theta(x_t, t)$ -- predicted noise
- $\bar{\alpha}_t$ -- cumulative signal retention at step $t$
- $\bar{\alpha}_{t-1}$ -- cumulative signal retention at the previous step

## Key Points

- DDIM uses the same denoiser as DDPM but changes the sampler.
- The deterministic path makes faster sampling practical.
- This module focuses on the common $\eta = 0$ update.

## Function

```python
def ddim_step(
    x_t: float,
    predicted_noise: float,
    alpha_bar_t: float,
    alpha_bar_prev: float,
) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/ddim-sampling/python -q
```
