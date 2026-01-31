# LoRA

> Track: `ml` | Topic: `llm`

## Concept

LoRA applies a low-rank update ΔW = A @ B while keeping base weights frozen.

## Math

W' = W + (α / r) * A B.

## Function

```python
def lora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/lora/python -q
```
