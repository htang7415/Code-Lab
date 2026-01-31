# Diffusion Sampling and Guidance Trade-offs

> Track: `ml` | Topic: `generative`

## Concept

Guidance improves fidelity but can slow sampling or reduce diversity.

## Math

$$guided = base + s * (cond - base)$$

## Function

```python
def guided_step(base: float, cond: float, scale: float) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/diffusion-guidance-tradeoffs/python -q
```
