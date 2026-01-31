# VAE

> Track: `ml` | Topic: `generative`

## Concept

A Variational Autoencoder (VAE) is a generative model that learns a latent representation by combining a probabilistic encoder with a decoder. The encoder $q_\phi(z|x)$ maps input data to a distribution in latent space, and the decoder $p_\theta(x|z)$ reconstructs data from latent samples. Training maximizes a lower bound on the log-likelihood, known as the Evidence Lower Bound (ELBO).

The key innovation is the reparameterization trick, which allows gradients to flow through the stochastic sampling step. Instead of sampling $z$ directly from $q_\phi(z|x)$, the encoder outputs $\mu$ and $\sigma$, and $z$ is computed deterministically from an auxiliary noise variable $\epsilon$. This makes the entire network end-to-end differentiable.

VAEs produce a smooth, continuous latent space where nearby points decode to similar outputs, making them well-suited for interpolation and controlled generation. The trade-off is that samples tend to be blurrier than those from GANs, because the reconstruction loss averages over possible outputs. However, VAEs offer stable training and a principled probabilistic framework with tractable likelihood bounds.

## Math

The ELBO objective that VAEs maximize is:

$$\text{ELBO} = \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - D_{KL}(q_\phi(z|x) \| p(z))$$

The reparameterization trick computes latent samples as:

$$z = \mu + \sigma \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

- $q_\phi(z|x)$ -- encoder (approximate posterior) parameterized by $\phi$
- $p_\theta(x|z)$ -- decoder (likelihood) parameterized by $\theta$
- $p(z)$ -- prior, typically $\mathcal{N}(0, I)$
- $D_{KL}$ -- Kullback-Leibler divergence regularizing the latent distribution

## Key Points

- The ELBO balances reconstruction quality (first term) against latent regularization (KL term); tuning the weight between them controls sample sharpness versus latent smoothness.
- VAE samples are typically blurrier than GAN outputs because the Gaussian decoder averages over modes, but training is much more stable.
- The smooth latent space enables meaningful interpolation between data points -- a property GANs do not guarantee.
- Posterior collapse occurs when the decoder becomes powerful enough to ignore $z$, causing the KL term to vanish (see VAE Posterior Collapse module).

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

- `recon` -- reconstruction log-likelihood term, $\mathbb{E}_{q(z|x)}[\log p(x|z)]$
- `kl` -- KL divergence between the approximate posterior and the prior, $D_{KL}(q(z|x) \| p(z))$

## Run tests

```bash
pytest modules/ml/generative/vae/python -q
```
