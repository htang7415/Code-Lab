# Group-Based Optimization (GSPO / GRPO)

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Group-based policy optimization builds advantages by normalizing rewards within
a group of sampled responses. GRPO uses token-level importance ratios, while
GSPO switches to a sequence-level ratio to reduce token-level instability.

## Math

- A_i = (r_i - mean(r)) / (std(r) + eps)
- GRPO: r_{i,t} = exp(log pi_theta - log pi_old)
- GSPO: r_i = exp(sum_t (log pi_theta - log pi_old))
- Objective (demo): J = mean_i(ratio_i * A_i)

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
