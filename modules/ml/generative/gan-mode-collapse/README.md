# GAN Instability and Mode Collapse

> Track: `ml` | Topic: `generative`

## Concept

Mode collapse is the most common failure mode in GAN training. It occurs when the generator learns to map many different noise vectors $z$ to only a small number of distinct outputs, effectively "collapsing" onto a few modes of the data distribution while ignoring the rest. The discriminator may correctly reject these repetitive samples, but the generator oscillates between modes rather than covering the full distribution.

The root cause lies in the minimax dynamics. When the discriminator identifies a mode the generator is missing, the generator shifts to cover that mode -- but often abandons previously covered modes in the process. This cyclic behavior means the generator never settles on producing the full diversity of the training data.

Several practical remedies exist. Minibatch discrimination lets the discriminator compare samples within a batch, penalizing low diversity directly. Unrolled GANs compute generator gradients through multiple discriminator steps, giving $G$ a longer-horizon view. Feature matching replaces the adversarial signal with a loss based on matching intermediate discriminator features. Monitoring sample entropy or pairwise distances during training is the simplest way to detect collapse early.

## Math

The standard GAN value function is:

$$V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$

Mode collapse occurs when $G$ maps diverse inputs to few outputs. A diversity metric based on sample variance is:

$$\text{diversity} = \frac{1}{N}\sum_{i=1}^{N}(s_i - \bar{s})^2$$

- $V(D, G)$ -- GAN value function
- $D$ -- discriminator
- $G$ -- generator
- $p_{\text{data}}$ -- data distribution
- $p_z$ -- noise prior distribution
- $x$ -- real data sample
- $z$ -- noise sample
- $s_i$ -- i-th generated sample
- $\bar{s}$ -- mean of generated samples
- $N$ -- number of samples

## Key Points

- Detect mode collapse by monitoring the variance or pairwise distances of generated samples; a sudden drop signals the generator is producing repetitive outputs.
- Minibatch discrimination is a direct fix: it augments the discriminator with cross-sample statistics so it can penalize low-diversity batches.
- Wasserstein loss (WGAN) provides smoother gradients and reduces the incentive for the generator to focus on a single mode.
- Mode collapse and training instability are related but distinct: the generator can be unstable (oscillating losses) without collapsing, and can collapse while losses appear stable.
- Evaluation metrics like FID and Inception Score can mask mode collapse; always inspect generated samples visually.

## Function

```python
def diversity_score(samples: list[float]) -> float:
```

- `samples` -- list of generated sample values to evaluate for diversity

## Run tests

```bash
pytest modules/ml/generative/gan-mode-collapse/python -q
```
