# Masked Attention (Causal Mask)

> Track: `ml` | Topic: `llm`

## Concept

In autoregressive language models, each token can only attend to itself and
previous tokens. This is enforced by a **causal (lower-triangular) mask** applied
to the attention scores before softmax.

Without the mask, token at position _i_ could "see" tokens at positions _i+1, i+2, …_,
leaking future information during training. The mask sets those attention scores
to −∞ so that softmax drives them to zero.

Multi-head attention applies the same mask to every head independently.
The mask is a constant for a given sequence length and can be precomputed once.

## Math

$$\text{Scaled dot-product attention with causal mask:}$$

```
scores = Q @ K^T / sqrt(d_k)           # (seq_len, seq_len)

mask[i][j] = 0      if j <= i
           = -inf    if j >  i

masked = scores + mask
weights = softmax(masked, dim=-1)       # (seq_len, seq_len)
output  = weights @ V                   # (seq_len, d_v)
```

- $\text{\texttt{Q}, \texttt{K} — queries and keys, shape \texttt{(seq\_len, d\_k)}}$
- $\text{\texttt{V} — values, shape \texttt{(seq\_len, d\_v)}}$
- $\text{\texttt{d\_k} — key dimension (scaling factor prevents large dot products)}$

## Function

```python
def causal_self_attention(Q, K, V) -> np.ndarray
```

- `Q` — query matrix, shape `(seq_len, d_k)`
- `K` — key matrix, shape `(seq_len, d_k)`
- `V` — value matrix, shape `(seq_len, d_v)`
- Returns — output of shape `(seq_len, d_v)`, each row attending only to current and earlier positions

Helper functions:

```python
def causal_mask(seq_len) -> np.ndarray    # upper-tri of -inf
def softmax(x, axis=-1) -> np.ndarray     # numerically stable
```

## Run tests

```bash
pytest modules/ml/llm/attention-causal/python -q
```
