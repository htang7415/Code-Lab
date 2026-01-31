# Step Decay

> Track: `ml` | Topic: `optimization`

## Concept

Step decay drops LR by a factor every k steps.

## Math

$$\text{lr}_t = \text{lr} \cdot \gamma^{\lfloor t / \text{step} \rfloor}$$

## Function

```python
def step_decay(lr: float, step: int, gamma: float, t: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-step-decay/python -q
```
