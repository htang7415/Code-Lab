# Contrast and Brightness

> Track: `ml` | Topic: `computer-vision`

## Concept

Adjust brightness and contrast via linear transform.

## Math

$$x' = a x + b$$

## Function

```python
def adjust(x: float, a: float, b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/contrast-brightness/python -q
```
