# Target Network Update

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Target network updates stabilize bootstrapped value learning by moving the target parameters more slowly than the online parameters.

## Math

$$
\theta_{\mathrm{target}} \leftarrow (1 - \tau)\theta_{\mathrm{target}} + \tau \theta_{\mathrm{online}}
$$

- $\theta_{\mathrm{target}}$ -- target network parameters
- $\theta_{\mathrm{online}}$ -- online network parameters
- $\tau$ -- soft-update rate

## Key Points

- Slower target updates reduce feedback instability in bootstrapped methods.
- This module uses soft updates rather than periodic hard copies.
- The same idea appears in DQN-style and actor-critic systems.

## Function

```python
def soft_target_update(target_values: list[float], online_values: list[float], tau: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/target-network-update/python -q
```
