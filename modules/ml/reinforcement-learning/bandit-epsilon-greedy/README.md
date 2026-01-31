# Epsilon-Greedy Bandit

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

The **multi-armed bandit** problem is a simplified RL setting: an agent
repeatedly chooses one of _K_ actions (arms) and receives a stochastic reward.
The goal is to maximize cumulative reward over time.

The **epsilon-greedy** strategy balances exploration and exploitation:

- With probability $\epsilon$, pick a random arm (explore)
- With probability $1-\epsilon$, pick the arm with the highest estimated value (exploit)

This is the simplest baseline for the explore-exploit tradeoff.
$\epsilon = 0$ is pure greedy; $\epsilon = 1$ is pure random.

## Math

Action-value estimate updated incrementally after pulling arm $a$ and observing reward $r$:

$$N_a \leftarrow N_a + 1$$

$$Q_a \leftarrow Q_a + \frac{1}{N_a}(r - Q_a)$$

- $Q_a$ — estimated value of arm $a$ (running mean of rewards)
- $N_a$ — number of times arm $a$ has been pulled
- The update computes the sample mean incrementally

Arm selection:

$$a_t = \begin{cases} \text{random arm from } \{0, \dots, K{-}1\} & \text{with probability } \epsilon \\ \arg\max_a Q_a & \text{with probability } 1 - \epsilon \end{cases}$$

## Function

```python
class EpsilonGreedyBandit:
    def __init__(self, k: int, epsilon: float = 0.1, seed: int | None = None)
    def select_arm(self) -> int
    def update(self, arm: int, reward: float) -> None
```

- `k` — number of arms
- `epsilon` — exploration probability (0 to 1)
- `select_arm()` — returns the index of the chosen arm
- `update(arm, reward)` — updates the value estimate for the given arm
- `q_values` — list of current estimated values per arm
- `counts` — list of pull counts per arm

## Run tests

```bash
pytest modules/ml/reinforcement-learning/bandit-epsilon-greedy/python -q
cargo test --manifest-path modules/ml/reinforcement-learning/bandit-epsilon-greedy/rust/Cargo.toml
```
