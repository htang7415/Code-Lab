# Tokenization

> Track: `ml` | Topic: `llm`

## Concept

Tokenization maps raw text into discrete tokens that a model can embed.

## Math

$$Let \texttt{V} be the vocabulary. Tokenization is a mapping \texttt{f: text -> [id\_1, ..., id\_n]}.$$

## Function

```python
def tokenize(text: str, vocab: dict[str, int]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/llm/tokenization/python -q
```
