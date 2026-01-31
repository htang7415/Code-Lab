# Embeddings

> Track: `ml` | Topic: `llm`

## Concept

Embeddings map discrete token ids to continuous vectors used by the model.

## Math

$$Given embedding matrix \texttt{E ∈ R\^\{\}\{V×d\}}, the embedding for token \texttt{i} is \texttt{E[i]}.$$

## Function

```python
def embed(tokens: list[int], embeddings: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/embeddings/python -q
```
