# Choose GAN vs VAE vs Diffusion

> Track: `ml` | Topic: `generative`

## Concept

Choosing among GANs, VAEs, and diffusion models requires balancing several practical criteria: sample quality (fidelity), diversity (mode coverage), sampling speed, training stability, and whether a structured latent space is needed. No single model dominates on every axis, so the right choice depends on the application.

GANs produce sharp, high-fidelity samples and generate them quickly in a single forward pass, but they suffer from training instability and mode collapse, and they provide no latent density or likelihood estimate. VAEs offer stable training and a smooth, interpretable latent space with tractable likelihood bounds, making them ideal for representation learning and interpolation, though their samples tend to be blurrier. Diffusion models achieve the best sample quality and mode coverage, surpassing GANs on benchmarks like FID, but at the cost of slow iterative sampling.

In practice the decision often comes down to constraints. If you need real-time generation (e.g., game assets), GANs or VAEs are preferred. If you need the best possible quality and can afford slower inference (e.g., image synthesis pipelines), diffusion models are the current state of the art. If you need a meaningful latent space for downstream tasks, VAEs are the natural choice. Hybrid approaches like latent diffusion models combine a VAE encoder with a diffusion process in the latent space to get the best of both worlds.

## Math

There is no single formula for model selection. The comparison is driven by empirical metrics.

| Criterion | GAN | VAE | Diffusion |
|---|---|---|---|
| Sample fidelity | High | Medium | Highest |
| Mode coverage | Low-Medium | High | High |
| Sampling speed | Fast (1 pass) | Fast (1 pass) | Slow ($T$ steps) |
| Training stability | Unstable | Stable | Stable |
| Latent space | No | Smooth | No |

FID (Frechet Inception Distance) is the standard quantitative comparison:

$$\text{FID} = \|\mu_r - \mu_g\|^2 + \text{Tr}\!\left(\Sigma_r + \Sigma_g - 2(\Sigma_r \Sigma_g)^{\frac{1}{2}}\right)$$

- $\mu_r, \Sigma_r$ -- mean and covariance of real data features
- $\mu_g, \Sigma_g$ -- mean and covariance of generated data features

## Key Points

- Use GANs when sampling speed and sharpness matter most and you can invest effort in stabilizing training.
- Use VAEs when you need a smooth, interpretable latent space for interpolation, editing, or downstream representation learning.
- Use diffusion models when sample quality is the top priority and slow sampling is acceptable.
- Latent diffusion models (e.g., Stable Diffusion) combine VAE compression with diffusion in latent space, offering a strong practical compromise.
- FID is the most common single metric for comparison, but always consider diversity, speed, and application-specific requirements alongside it.

## Function

```python
def choose_model(priority: str) -> str:
```

- `priority` -- a string indicating the primary requirement: `"fidelity"`, `"speed"`, `"latent_space"`, or `"quality"`

## Run tests

```bash
pytest modules/ml/generative/model-selection/python -q
```
