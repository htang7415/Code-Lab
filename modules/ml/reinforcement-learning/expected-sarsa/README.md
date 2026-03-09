# Expected SARSA Target

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Expected SARSA bootstraps from the policy-weighted average next-state action value instead of a sampled next action or a max.

## Math

$$
\mathrm{target} = r + \gamma \sum_a \pi(a \mid s') Q(s', a)
$$

- $r$ -- immediate reward
- $\gamma$ -- discount factor
- $\pi(a \mid s')$ -- policy probability for next action $a$
- $Q(s', a)$ -- next-state action value

## Key Points

- This sits between SARSA and Q-learning conceptually.
- It reduces sampling variance by averaging under the next-state policy.
- The module computes the bootstrapped target only.

## Function

```python
def expected_sarsa_target(reward: float, gamma: float, next_action_probs: list[float], next_q_values: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/expected-sarsa/python -q
```
