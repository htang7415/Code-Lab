# Diffusion Models

Diffusion models trade fast one-shot generation for stable likelihood-free denoising steps.

## Current Anchors

- Diffusion models (`modules/ml/generative/diffusion-models`)
- DDPM reverse step (`modules/ml/generative/ddpm-sampling`)
- DDIM deterministic step (`modules/ml/generative/ddim-sampling`)
- Guidance trade-offs / classifier-free guidance (`modules/ml/generative/diffusion-guidance-tradeoffs`)
- EMA for diffusion weights (`modules/ml/generative/ema-diffusion-weights`)

## Concepts to Cover Well

- Forward noising and reverse denoising
- Noise schedules and timestep parameterization
- DDPM vs DDIM sampling trade-offs
- Guidance strength vs diversity
- EMA weights as a smoother sampling-time model copy
- Why diffusion is stable but sampling-expensive
