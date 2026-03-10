# Diffusion Models

Diffusion models learn to reverse a gradual noising process, which makes training stable but sampling relatively expensive.

## Purpose

Use this page to keep diffusion in the right order:
- forward noising
- reverse denoising
- sampling choices
- guidance
- EMA stabilization

## First Principles

- Training adds noise to data and asks the model to predict or remove it.
- Sampling runs the reverse process step by step, so quality improves at the cost of speed.
- DDPM and DDIM mostly differ in how they trade stochasticity against speed and determinism.
- Guidance improves alignment or prompt-following, but too much guidance can hurt diversity.
- EMA weights act like a smoother sampling-time copy of the model.

## Core Math

- Forward noising shape:
  $$
  x_t = \sqrt{\alpha_t} x_0 + \sqrt{1-\alpha_t}\,\epsilon
  $$
- Training often minimizes an MSE between predicted and true noise.

## Minimal Code Mental Model

```python
noise = sample_noise(x.shape)
noisy_x = add_noise(x, noise, t)
pred = model(noisy_x, t)
loss = mse(pred, noise)
```

## Canonical Modules

- Core diffusion idea: `diffusion-models`
- Sampling: `ddpm-sampling`, `ddim-sampling`
- Guidance: `diffusion-guidance-tradeoffs`
- Stabilization: `ema-diffusion-weights`

## When To Use What

- Start with `diffusion-models` before DDPM or DDIM details.
- Use `ddpm-sampling` when you want the basic stochastic reverse process.
- Use `ddim-sampling` when you want faster or more deterministic sampling intuition.
- Use guidance and EMA only after the base forward/reverse picture is clear.
