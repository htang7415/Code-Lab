# Group-Based Optimization (GSPO / GRPO)

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Group-based policy optimization builds advantages by normalizing rewards within
a group of sampled responses. GRPO uses token-level importance ratios, while
GSPO switches to a sequence-level ratio to reduce token-level instability.

## Math
$$A_i = \frac{r_i - \mu_r}{\sigma_r + \epsilon}$$

$$\rho_{i,t} = \exp(\log \pi_\theta - \log \pi_{\text{old}}),\quad \mathrm{ratio}_i = \frac{1}{T}\sum_t \rho_{i,t}$$

$$J = \frac{1}{N}\sum_i \mathrm{ratio}_i A_i$$

- $A_i$ -- advantage for sample i
- $r_i$ -- reward for sample i
- $\mu_r$ -- mean reward
- $\sigma_r$ -- reward standard deviation
- $\epsilon$ -- small constant for numerical stability
- $\rho_{i,t}$ -- importance ratio for sample i at step t
- $\mathrm{ratio}_i$ -- sequence-level importance ratio for sample i
- $T$ -- number of tokens or steps
- $N$ -- number of samples
- $\pi_\theta$ -- current policy
- $\pi_{\text{old}}$ -- reference (old) policy
- $J$ -- objective

## Function

```python
def group_advantages(rewards: list[float], eps: float = 1e-8) -> list[float]:

def grpo_objective(
    old_logps: list[list[float]],
    new_logps: list[list[float]],
    rewards: list[float],
) -> float:

def gspo_objective(
    old_logps: list[list[float]],
    new_logps: list[list[float]],
    rewards: list[float],
) -> float:
```

## Demo code

```python
old_logps = [[-0.1, -0.2], [-0.3, -0.1]]
new_logps = [[-0.15, -0.25], [-0.25, -0.05]]
rewards = [0.2, 0.8]
print(grpo_objective(old_logps, new_logps, rewards))
print(gspo_objective(old_logps, new_logps, rewards))
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/group-based-optimization/python -q
cargo test --manifest-path modules/ml/reinforcement-learning/group-based-optimization/rust/Cargo.toml
```
