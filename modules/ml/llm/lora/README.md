# LoRA

> Track: `ml` | Topic: `llm`

## Concept

LoRA applies a low-rank update $\Delta W = AB$ while keeping base weights frozen.

## Math

$$W' = W + \frac{\alpha}{r} AB$$

- $W$ -- frozen base weight matrix
- $W'$ -- updated weight matrix after LoRA
- $A, B$ -- low-rank update matrices (rank $r$)
- $r$ -- rank of the LoRA update
- $\alpha$ -- LoRA scaling factor

## Function

```python
def lora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/lora/python -q
```
