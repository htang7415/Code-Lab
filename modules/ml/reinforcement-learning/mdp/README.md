# Markov Decision Process

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

An MDP defines states, actions, transitions, and rewards.

## Math
$$P(s'\mid s,a) = \Pr(S_{t+1}=s'\mid S_t=s, A_t=a)$$

- $s$ -- state
- $a$ -- action
- $t$ -- timestep or iteration

- $A_t$ -- advantage estimate at step t
- $A$ -- advantage estimate

## Function

```python
def transition_prob(transitions: dict[tuple[int, int], dict[int, float]], s: int, a: int, s_next: int) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/mdp/python -q
```