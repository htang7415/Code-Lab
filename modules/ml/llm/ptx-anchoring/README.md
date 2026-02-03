# PTX Anchoring

> Track: `ml` | Topic: `llm`

## Concept

PTX anchoring mixes a small amount of pretraining loss during alignment to retain base behavior.

## Math

$$L = (1-\alpha) L_{\text{align}} + \alpha L_{\text{ptx}}$$

- $L$ -- total loss
- $L_{\text{align}}$ -- alignment loss
- $L_{\text{ptx}}$ -- pretraining (PTX) loss
- $\alpha$ -- mixing weight for PTX loss

## Function

```python
def anchored_loss(align_loss: float, ptx_loss: float, alpha: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/ptx-anchoring/python -q
```
