# Non-Maximum Suppression

> Track: `ml` | Topic: `computer-vision`

## Concept

NMS removes overlapping boxes with lower scores.

## Math

Keep highest score; suppress IoU > threshold.

## Function

```python
def iou(box_a: tuple[float, float, float, float], box_b: tuple[float, float, float, float]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/non-maximum-suppression/python -q
```
