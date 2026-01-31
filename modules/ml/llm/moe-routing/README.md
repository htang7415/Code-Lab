# MoE Routing

> Track: `ml` | Topic: `llm`

## Concept

Mixture-of-Experts routes tokens to top-k experts based on gating scores.

## Math

Select top-k gates g_i; output = sum(g_i * expert_i).

## Function

```python
def moe_combine(experts: list[list[float]], gates: list[float], k: int) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/llm/moe-routing/python -q
```
