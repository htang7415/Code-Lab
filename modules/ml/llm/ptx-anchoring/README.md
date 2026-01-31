# PTX Anchoring

> Track: `ml` | Topic: `llm`

## Concept

PTX anchoring mixes a small amount of pretraining loss during alignment to retain base behavior.

## Math

Anchored loss: L = (1-α) * L_align + α * L_ptx.

## Function

```python
def anchored_loss(align_loss: float, ptx_loss: float, alpha: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/ptx-anchoring/python -q
```
