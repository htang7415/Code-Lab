# MoE Routing

> Track: `ml` | Topic: `llm`

## Concept

Mixture-of-Experts routes tokens to top-k experts based on gating scores.

## Math
$$y = \sum_{i \in \mathcal{K}} g_i f_i(x),\quad \mathcal{K} = \mathrm{TopK}(g)$$

- $g_i$ -- i-th gradient
- $y$ -- target/label
- $i$ -- index
- $g$ -- gradient
- $x$ -- input (feature vector or sample)

## Function

```python
def moe_combine(experts: list[list[float]], gates: list[float], k: int) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/llm/moe-routing/python -q
```