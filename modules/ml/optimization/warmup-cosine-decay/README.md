# Warmup Plus Cosine Decay

> Track: `ml` | Topic: `optimization`

## Concept

Warmup plus cosine decay uses a linear learning-rate ramp at the start of training and then smoothly anneals the rate with a cosine curve.

## Math

$$\eta_t = \eta_0 \frac{t}{T_{\mathrm{warm}}} \quad \text{for } t < T_{\mathrm{warm}}$$

$$\eta_t = \eta_0 \frac{1 + \cos\left(\pi \frac{t - T_{\mathrm{warm}}}{T - T_{\mathrm{warm}}}\right)}{2} \quad \text{for } t \ge T_{\mathrm{warm}}$$

- $\eta_0$ -- base learning rate
- $t$ -- training step
- $T_{\mathrm{warm}}$ -- warmup length
- $T$ -- total training steps

## Key Points

- Warmup reduces early optimization instability.
- Cosine decay lowers the learning rate smoothly near the end of training.
- This schedule is a common default for transformer training.

## Function

```python
def warmup_cosine_lr(
    base_lr: float,
    step: int,
    warmup_steps: int,
    total_steps: int,
) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/warmup-cosine-decay/python -q
```
