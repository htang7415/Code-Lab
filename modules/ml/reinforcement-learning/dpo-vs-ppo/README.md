# DPO vs PPO

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Compare preference optimization to policy optimization.

## Math
$$L_{\text{PPO}} = \min\left(r_t A_t, \mathrm{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t\right)$$

$$L_{\text{DPO}} = -\log \sigma\left(\beta(\Delta \log \pi - \Delta \log \pi_{\text{ref}})\right)$$

- $L_{\text{PPO}}$ -- PPO clipped objective
- $r_t$ -- policy probability ratio at step $t$
- $A_t$ -- advantage estimate at step $t$
- $\epsilon$ -- PPO clip range
- $L_{\text{DPO}}$ -- DPO loss
- $\beta$ -- temperature scaling the preference gap
- $\pi$ -- policy
- $\pi_{\text{ref}}$ -- reference policy
- $\sigma$ -- sigmoid (logistic) function

## Function

```python
def compare_methods() -> list[str]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/dpo-vs-ppo/python -q
```
