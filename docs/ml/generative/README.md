# Generative Models

Core generative families and trade-offs.
Each bullet maps to a module under `modules/ml/generative/`.

Leaf guides:

- Diffusion map (`docs/ml/generative/diffusion`)

## Core Families

- GAN (generator vs discriminator, mode collapse) (`modules/ml/generative/gan`)
- VAE (ELBO, reconstruction + KL) (`modules/ml/generative/vae`)
- Diffusion models (forward noise / reverse denoise, training objective) (`modules/ml/generative/diffusion-models`)

## Interview-Level Skills

- Choose GAN vs VAE vs Diffusion for a task (trade-offs) (`modules/ml/generative/model-selection`)
- GAN instability, mode collapse (`modules/ml/generative/gan-mode-collapse`)
- VAE blurry samples, posterior collapse (`modules/ml/generative/vae-posterior-collapse`)
- DDPM reverse mean step (`modules/ml/generative/ddpm-sampling`)
- DDIM deterministic step (`modules/ml/generative/ddim-sampling`)
- Diffusion guidance trade-offs / classifier-free guidance (`modules/ml/generative/diffusion-guidance-tradeoffs`)
- EMA for diffusion weights (`modules/ml/generative/ema-diffusion-weights`)

## Rebalancing Notes

- Diffusion now has enough anchors to teach training objective, sampling, guidance, and EMA separately.
- The next generative additions should prefer canonical gaps like schedulers or latent diffusion over more narrow score variants.
