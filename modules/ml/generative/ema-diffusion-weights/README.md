# EMA for Diffusion Weights

> Track: `ml` | Topic: `generative`

## Concept

Diffusion models are often sampled from an exponential moving average of the
training weights instead of the raw live weights. EMA damps noisy parameter
updates and usually produces cleaner samples at evaluation time.

## Math

$$\theta_{\mathrm{ema}}' = \beta \theta_{\mathrm{ema}} + (1 - \beta)\theta$$

- $\theta_{\mathrm{ema}}$ -- current EMA weights
- $\theta$ -- latest model weights
- $\beta$ -- decay factor
- $\theta_{\mathrm{ema}}'$ -- updated EMA weights

## Function

```python
def ema_update(ema_weights: list[float], model_weights: list[float], decay: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/generative/ema-diffusion-weights/python -q
```
