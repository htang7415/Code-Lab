# QLoRA

> Track: `ml` | Topic: `llm`

## Concept

QLoRA combines low-rank updates with quantized base weights.

## Math
$$W_q = \mathrm{Quantize}(W; s),\quad W' = W_q + \frac{\alpha}{r} AB$$

- $W$ -- base weight matrix
- $W_q$ -- quantized base weight matrix
- $W'$ -- updated weight matrix after QLoRA
- $\mathrm{Quantize}(\cdot; s)$ -- quantization operator with scale $s$
- $s$ -- quantization scale
- $A, B$ -- low-rank update matrices (rank $r$)
- $r$ -- rank of the LoRA update
- $\alpha$ -- LoRA scaling factor

## Function

```python
def qlora_update(w: list[list[float]], a: list[list[float]], b: list[list[float]], alpha: float, scale: float) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/qlora/python -q
```
