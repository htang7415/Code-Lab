# Tokenization

> Track: `ml` | Topic: `llm`

## Concept

Tokenization maps raw text into discrete tokens that a model can embed.

## Math

Let `V` be the vocabulary. Tokenization is a mapping `f: text -> [id_1, ..., id_n]`.

## Function

```python
def tokenize(text: str, vocab: dict[str, int]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/llm/tokenization/python -q
```
