# DPO (Direct Preference Optimization)

> Track: `ml` | Topic: `llm`

## Concept

DPO optimizes policy preferences directly using a reference model.

## Math

$$\text{Demo loss: } L = -\log\left(\sigma\left(\beta(\Delta \log \pi - \Delta \log \pi_{\text{ref}})\right)\right)$$

## Function

```python
def dpo_loss(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/dpo/python -q
```
