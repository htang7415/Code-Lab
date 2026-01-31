# Markov Decision Process

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

An MDP defines states, actions, transitions, and rewards.

## Math

P(s'|s,a) defines transition probabilities.

## Function

```python
def transition_prob(transitions: dict[tuple[int, int], dict[int, float]], s: int, a: int, s_next: int) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/mdp/python -q
```
