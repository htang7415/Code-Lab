# Non-Maximum Suppression

> Track: `ml` | Topic: `computer-vision`

## Concept

NMS removes overlapping boxes with lower scores.

## Math
$$b^* = \arg\max_i s_i,\quad \text{discard } b_i \text{ if } \mathrm{IoU}(b_i, b^*) > \tau$$

- $b_i$ -- bounding box $i$
- $b^*$ -- highest-scoring box
- $s_i$ -- confidence score for box $i$
- $\mathrm{IoU}$ -- intersection over union
- $\tau$ -- IoU threshold

## Function

```python
def iou(box_a: tuple[float, float, float, float], box_b: tuple[float, float, float, float]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/non-maximum-suppression/python -q
```