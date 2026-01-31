# Diffusion Models

> Track: `ml` | Topic: `generative`

## Concept

Diffusion models are a class of generative models built on two processes: a forward process that gradually adds Gaussian noise to data over $T$ timesteps until the signal is destroyed, and a learned reverse process that denoises step-by-step to recover the original data distribution. The forward process requires no learning -- it is a fixed Markov chain defined by a noise schedule $\{\beta_t\}$. The reverse process is parameterized by a neural network $\epsilon_\theta$ trained to predict the noise added at each step.

The training objective simplifies to a denoising score-matching loss: the network learns to predict the noise $\epsilon$ that was added to a clean sample $x_0$ to produce a noisy sample $x_t$. At generation time, the model starts from pure noise $x_T \sim \mathcal{N}(0, I)$ and iteratively denoises through all $T$ steps to produce a sample.

Diffusion models achieve state-of-the-art image quality and diversity, surpassing GANs on benchmarks like FID. The main drawback is sampling speed, since generation requires hundreds or thousands of sequential denoising steps. Accelerated samplers such as DDIM reduce this to tens of steps by converting the stochastic process into a deterministic ODE, making diffusion models practical for real applications.

## Math

The forward process adds noise at each timestep:

$$q(x_t | x_{t-1}) = \mathcal{N}\!\left(x_t;\, \sqrt{1 - \beta_t}\, x_{t-1},\, \beta_t I\right)$$

The closed-form noisy sample at timestep $t$ is:

$$x_t = \sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1 - \bar{\alpha}_t}\, \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

The simplified training loss is:

$$\mathcal{L} = \mathbb{E}_{t, x_0, \epsilon}\!\left[\|\epsilon - \epsilon_\theta(x_t, t)\|^2\right]$$

- $\beta_t$ -- noise variance at step $t$
- $\bar{\alpha}_t = \prod_{s=1}^{t}(1 - \beta_s)$ -- cumulative signal retention
- $\epsilon_\theta$ -- neural network predicting the noise component

## Key Points

- Diffusion models produce the highest-quality samples among current generative approaches, with excellent mode coverage and diversity.
- Sampling is slow by default ($T = 1000$ steps), but DDIM and other ODE-based solvers can reduce this to 20-50 steps with minimal quality loss.
- The forward noising process uses a fixed schedule ($\beta_t$) and requires no training; only the reverse denoiser is learned.
- Diffusion models connect to score-based models through the equivalence between predicting noise and estimating the score $\nabla_x \log p(x)$.

## Function

```python
def add_noise(x: float, noise: float, alpha: float) -> float:
```

- `x` -- clean data sample $x_0$
- `noise` -- Gaussian noise sample $\epsilon$
- `alpha` -- cumulative signal retention factor $\bar{\alpha}_t$

## Run tests

```bash
pytest modules/ml/generative/diffusion-models/python -q
```
