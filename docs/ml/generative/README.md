# Generative Models

Core generative families and trade-offs.
Each bullet maps to a module under `modules/ml/generative/`.

## Core Families

- GAN (generator vs discriminator, mode collapse) (`modules/ml/generative/gan`)
- VAE (ELBO, reconstruction + KL) (`modules/ml/generative/vae`)
- Diffusion models (forward noise / reverse denoise, training objective) (`modules/ml/generative/diffusion-models`)

## Interview-Level Skills

- Choose GAN vs VAE vs Diffusion for a task (trade-offs) (`modules/ml/generative/model-selection`)
- GAN instability, mode collapse (`modules/ml/generative/gan-mode-collapse`)
- VAE blurry samples, posterior collapse (`modules/ml/generative/vae-posterior-collapse`)
- Diffusion slow sampling, guidance trade-offs (`modules/ml/generative/diffusion-guidance-tradeoffs`)
