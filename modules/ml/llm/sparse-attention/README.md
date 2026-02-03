# Sparse Attention

> Track: `ml` | Topic: `llm`

## Concept

Sparse attention limits attention to a local window to reduce complexity.

## Math

$$
\tilde{s}_{i,j} =
\begin{cases}
s_{i,j}, & |i - j| \le w \\
-\infty, & |i - j| > w
\end{cases},
\quad
\alpha_{i,j} = \mathrm{softmax}(\tilde{s}_{i,j})
$$

- $s_{i,j}$ -- attention score between tokens $i$ and $j$
- $\tilde{s}_{i,j}$ -- masked attention score
- $\alpha_{i,j}$ -- attention weight after softmax
- $w$ -- attention window size
- $i$ -- token index
- $j$ -- token index

## Function

```python
def window_mask(seq_len: int, window: int) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/ml/llm/sparse-attention/python -q
```
