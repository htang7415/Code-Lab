# Pretraining (Next-Token Loss)

> Track: `ml` | Topic: `llm`

## Concept

Pretraining optimizes next-token prediction on large corpora.

## Math

$$\text{Cross-entropy: } L = -\log\left(\mathrm{softmax}(\text{logits})_{\text{target}}\right)$$

- $L$ -- loss value

## Function

```python
def next_token_loss(logits: list[list[float]], targets: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/pretraining/python -q
```
