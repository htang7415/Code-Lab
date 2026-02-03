# Embeddings

> Track: `ml` | Topic: `llm`

## Concept

Embeddings map discrete token ids to continuous vectors used by the model.

## Math

$$\texttt{E} \in \mathbb{R}^{V \times d},\ \text{embedding for token } i \text{ is } \texttt{E[i]}.$$

- $V$ -- value matrix
- $d$ -- dimension
- $i$ -- index

## Function

```python
def embed(tokens: list[int], embeddings: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/embeddings/python -q
```
