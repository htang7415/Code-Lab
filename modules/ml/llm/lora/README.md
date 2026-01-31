# LoRA

> Track: `ml` | Topic: `llm`

## Concept

LoRA applies a low-rank update $\Delta W = AB$ while keeping base weights frozen.

## Math

$$W' = W + \frac{\alpha}{r} AB$$

## Function

```python
def lora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/lora/python -q
```
