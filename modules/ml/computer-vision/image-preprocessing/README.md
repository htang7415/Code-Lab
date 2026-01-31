# Image Preprocessing

> Track: `ml` | Topic: `computer-vision`

## Concept

Preprocessing normalizes pixel ranges for stable training.

## Math

$$x' = x / 255$$

## Function

```python
def normalize_pixels(pixels: list[int]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/image-preprocessing/python -q
```
