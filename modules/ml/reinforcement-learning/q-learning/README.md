# Q-Learning

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to learn the basic value-based RL update that bootstraps action
values toward a Bellman target.

## First Principles

- Q-learning estimates how good each state-action pair is.
- The update uses the reward plus the best estimated future action value.
- This is an off-policy method because it learns from the greedy target even if behavior was exploratory.
- Q-learning is the simplest bridge from Bellman equations to practical RL updates.

## Core Math

$$
Q \leftarrow Q + \eta\left(r + \gamma \max_{a'} Q(s',a') - Q(s,a)\right)
$$

- $\eta$ -- learning rate
- $\gamma$ -- discount factor
- $Q$ -- action-value function
- $r$ -- reward
- $s, a$ -- current state and action

## Minimal Code Mental Model

```python
target = reward + gamma * next_max
new_q = q_update(q, reward, next_max, alpha, gamma)
```

## Function

```python
def q_update(q: float, reward: float, next_max: float, alpha: float, gamma: float) -> float:
```

## When To Use What

- Use Q-learning as the default first value-based RL algorithm.
- Move to double Q-learning when overestimation becomes the main issue.
- Pair this module with `q-target` and `target-network-update` when studying deep Q-learning variants.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/q-learning/python -q
```
