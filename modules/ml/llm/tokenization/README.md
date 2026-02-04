# Tokenization

> Track: `ml` | Topic: `llm`

## Concept

Tokenization maps raw text into discrete tokens that a model can embed.
This demo uses a simple whitespace split; real tokenizers may use regex or BPE.

## Math

$$Let \texttt{V} be the vocabulary. Tokenization is a mapping \texttt{f: text -> [id\_1, ..., id\_n]}.$$

- $V$ -- vocabulary
- $f$ -- tokenization mapping
- $id_i$ -- token id at position $i$
- $n$ -- number of tokens

## Function

```python
def tokenize(text: str, vocab: dict[str, int]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/llm/tokenization/python -q
```
