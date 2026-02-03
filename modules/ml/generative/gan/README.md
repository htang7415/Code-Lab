# GAN

> Track: `ml` | Topic: `generative`

## Concept

A Generative Adversarial Network (GAN) consists of two neural networks -- a generator $G$ and a discriminator $D$ -- trained simultaneously in a minimax game. The generator maps random noise $z$ to synthetic samples, while the discriminator tries to distinguish real data from generated data. Training alternates between updating $D$ to better classify real versus fake, and updating $G$ to better fool $D$.

GANs matter because they can produce remarkably sharp, high-fidelity samples without requiring an explicit density model. The adversarial setup avoids the pixel-wise loss functions that cause blurriness in other generative models. However, this two-player game is inherently unstable: if one player becomes too strong, gradients for the other vanish and training collapses.

The original GAN objective can suffer from vanishing gradients when $D$ is optimal. Wasserstein GAN (WGAN) replaces the JS-divergence with the Earth Mover distance, providing smoother gradients and more stable training. Other stabilization techniques include spectral normalization, gradient penalties, and progressive growing.

## Math

The minimax objective for the GAN value function is:

$$\min_G \max_D \; \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$

The discriminator loss for a single sample pair is:

$$\mathcal{L}_D = -\log D(x) - \log(1 - D(G(z)))$$

- $D(x)$ -- discriminator output (probability that $x$ is real)
- $G(z)$ -- generator output given noise $z$
- $p_z$ -- prior distribution over latent noise (typically $\mathcal{N}(0, I)$)

- $\mathbb{E}$ -- expectation
- $x$ -- input (feature vector or sample)
- $p$ -- probability
- $z$ -- latent variable
- $\mathcal{L}$ -- loss function
- $\mathcal{N}$ -- normal (Gaussian) distribution
- $I$ -- identity matrix

## Key Points

- GAN training is inherently unstable because the generator and discriminator can oscillate rather than converge to a Nash equilibrium.
- Mode collapse is the most common failure: the generator learns to produce only a few outputs that fool the discriminator, ignoring the full data distribution.
- Wasserstein loss with gradient penalty (WGAN-GP) provides more meaningful gradients and is often the first remedy for training instability.
- GANs produce sharper samples than VAEs but offer no direct way to compute likelihoods or encode data into a latent space.

## Function

```python
def gan_loss(d_real: float, d_fake: float) -> float:
```

- `d_real` -- discriminator output on a real sample, $D(x)$
- `d_fake` -- discriminator output on a generated sample, $D(G(z))$

## Run tests

```bash
pytest modules/ml/generative/gan/python -q
```
