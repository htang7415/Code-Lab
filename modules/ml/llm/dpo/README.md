# DPO (Direct Preference Optimization)

> Track: `ml` | Topic: `llm`

## Concept

DPO optimizes policy preferences directly using a reference model.

## Math

Demo loss: L = -log(sigmoid(β * (Δlogπ - Δlogπ_ref))).

## Function

```python
def dpo_loss(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/dpo/python -q
```
