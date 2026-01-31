# QLoRA

> Track: `ml` | Topic: `llm`

## Concept

QLoRA combines low-rank updates with quantized base weights.

## Math

$$\text{Quantize base weights, then apply LoRA-style low-rank update.}$$

## Function

```python
def qlora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float, scale: float) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/qlora/python -q
```
