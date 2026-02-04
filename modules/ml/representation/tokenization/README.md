# Tokenization

> Track: `ml` | Topic: `representation`

## Concept

Tokenization splits raw text into units (tokens) that models can embed.
A simple tokenizer lowercases and splits on non-alphanumeric boundaries.

## Function

```python
def simple_tokenize(text: str) -> list[str]:
```

## Run tests

```bash
pytest modules/ml/representation/tokenization/python -q
```
