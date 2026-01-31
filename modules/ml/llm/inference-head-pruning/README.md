# Inference Head Pruning

> Track: `ml` | Topic: `llm`

## Concept

Head pruning removes less useful attention heads to reduce compute at inference.

## Math

Prune by slicing head blocks from weight matrices.

## Function

```python
def prune_heads(weights: list[list[float]], keep: list[int], head_dim: int) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/inference-head-pruning/python -q
```
