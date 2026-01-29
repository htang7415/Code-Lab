# Epsilon-Greedy Bandit

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

The **multi-armed bandit** problem is a simplified RL setting: an agent
repeatedly chooses one of K actions (arms) and receives a reward. The goal is
to maximize cumulative reward.

The **epsilon-greedy** strategy balances exploration and exploitation:

- With probability `epsilon`, pick a random arm (explore)
- With probability `1 - epsilon`, pick the arm with the highest estimated reward (exploit)

Action-value estimates are updated incrementally:

```
Q[a] += (1/N[a]) * (reward - Q[a])
```

where `N[a]` is the number of times arm `a` has been pulled.

## Key points

- Simple baseline strategy for the explore-exploit tradeoff
- epsilon = 0 is pure greedy; epsilon = 1 is pure random
- Does not decay epsilon by default (can be extended to do so)

## Run tests

```bash
pytest modules/ml/reinforcement-learning/bandit-epsilon-greedy/python -q
```
