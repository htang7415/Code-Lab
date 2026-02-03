# VAE Blurry Samples and Posterior Collapse

> Track: `ml` | Topic: `generative`

## Concept

Posterior collapse is a pathology in VAE training where the decoder learns to ignore the latent variable $z$ entirely. When this happens, the approximate posterior $q_\phi(z|x)$ collapses to match the prior $p(z)$, causing the KL divergence term in the ELBO to approach zero. The model degenerates into a standard autoregressive or feedforward decoder with no meaningful latent representation.

This failure is especially common when the decoder is powerful (e.g., an autoregressive model like an LSTM or Transformer). A strong decoder can reconstruct $x$ without extracting information from $z$, so the optimizer finds it easiest to simply set $q_\phi(z|x) \approx p(z)$ and pay zero KL cost. The result is a latent space that carries no information and cannot be used for interpolation or controlled generation.

The most widely used remedy is KL annealing: the KL term weight starts at zero and is gradually increased to its full value over the course of training, giving the encoder time to learn useful representations before the regularization penalty kicks in. The free-bits strategy sets a minimum target for the KL per latent dimension, preventing any single dimension from collapsing. Reducing decoder capacity can also help by forcing the model to rely on $z$.

## Math

The ELBO objective decomposes as:

$$\text{ELBO} = \underbrace{\mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)]}_{\text{reconstruction}} - \underbrace{D_{KL}(q_\phi(z|x) \| p(z))}_{\text{regularization}}$$

During posterior collapse, the KL term vanishes:

$$q_\phi(z|x) \approx p(z) \implies D_{KL}(q_\phi(z|x) \| p(z)) \approx 0$$

KL annealing introduces a weight $\lambda$ that ramps from 0 to 1:

$$\mathcal{L} = \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - \lambda \cdot D_{KL}(q_\phi(z|x) \| p(z))$$

- $\lambda$ -- annealing coefficient, linearly increased from 0 to 1 during training
- $q_\phi(z|x)$ -- approximate posterior (encoder output)
- $p(z)$ -- prior distribution, typically $\mathcal{N}(0, I)$

- $\mathrm{ELBO}$ -- evidence lower bound
- $\mathbb{E}$ -- expectation
- $\phi$ -- model/encoder parameters
- $\theta$ -- model parameters
- $q$ -- probability distribution
- $z$ -- latent variable
- $x$ -- input (feature vector or sample)
- $p$ -- probability
- $\mathcal{L}$ -- loss function
- $\mathcal{N}$ -- normal (Gaussian) distribution
- $I$ -- identity matrix

## Key Points

- The hallmark of posterior collapse is a KL term near zero combined with poor latent representations; the decoder reconstructs without using $z$.
- KL annealing (warmup) is the simplest fix: start with $\lambda = 0$ and linearly ramp to $\lambda = 1$ over training, giving the encoder time to learn before regularization dominates.
- The free-bits strategy enforces a minimum KL per dimension (e.g., $\geq 0.25$ nats), preventing individual latent dimensions from being ignored.
- Stronger decoders make posterior collapse worse; deliberately limiting decoder capacity forces the model to rely on the latent code.
- Monitoring per-dimension KL values during training is the most reliable way to detect which latent dimensions have collapsed.

## Function

```python
def kl_is_low(kl: float, threshold: float = 0.1) -> bool:
```

- `kl` -- measured KL divergence value $D_{KL}(q(z|x) \| p(z))$
- `threshold` -- KL value below which posterior collapse is flagged (default 0.1)

## Run tests

```bash
pytest modules/ml/generative/vae-posterior-collapse/python -q
```
