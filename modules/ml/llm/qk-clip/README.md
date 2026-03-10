# QK-Clip

> Track: `ml` | Topic: `llm`

## Concept

QK-clip stabilizes attention by clipping query-key scores before the softmax.
This keeps rare large dot products from dominating the attention distribution.

## Math

$$s'_{ij} = \mathrm{clip}(s_{ij}, -c, c)$$

- $s_{ij}$ -- raw query-key score before softmax
- $c$ -- clipping threshold
- $s'_{ij}$ -- clipped score used by attention

## Function

```python
def qk_clip(scores: list[list[float]], clip_value: float) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/qk-clip/python -q
```
