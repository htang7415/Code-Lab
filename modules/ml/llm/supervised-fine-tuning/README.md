# Supervised Fine-Tuning

> Track: `ml` | Topic: `llm`

## Concept

SFT trains on curated prompt-response pairs with teacher forcing.

## Math

Masked cross-entropy over supervised target tokens.

## Function

```python
def sft_loss(logits: list[list[float]], targets: list[int], mask: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/supervised-fine-tuning/python -q
```
