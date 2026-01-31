# Pretraining (Next-Token Loss)

> Track: `ml` | Topic: `llm`

## Concept

Pretraining optimizes next-token prediction on large corpora.

## Math

Cross-entropy: L = -log softmax(logits)[target].

## Function

```python
def next_token_loss(logits: list[list[float]], targets: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/pretraining/python -q
```
