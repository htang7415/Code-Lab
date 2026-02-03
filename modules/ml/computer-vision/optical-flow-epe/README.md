# Optical Flow (EPE)

> Track: `ml` | Topic: `computer-vision`

## Concept

Endpoint error measures flow prediction error.

## Math

$$\mathrm{EPE} = \sqrt{(u-u^*)^2 + (v-v^*)^2}$$

- $\mathrm{EPE}$ -- endpoint error
- $u^*$ -- horizontal flow component (ground truth)
- $v^*$ -- vertical flow component (ground truth)

- $u$ -- horizontal flow component (prediction)
- $v$ -- vertical flow component (prediction)

## Function

```python
def epe(pred: tuple[float, float], target: tuple[float, float]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/optical-flow-epe/python -q
```
