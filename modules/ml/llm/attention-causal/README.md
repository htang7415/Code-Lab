# Causal Attention Mask

> Track: `ml` | Topic: `llm`

## Concept

In autoregressive language models, each token can only attend to itself and
previous tokens. This is enforced by a **causal (lower-triangular) mask** applied
to the attention scores before softmax.

Given queries Q and keys K of shape `(seq_len, d_k)`:

```
scores = Q @ K^T / sqrt(d_k)
mask = upper-triangular matrix of -inf
masked_scores = scores + mask
weights = softmax(masked_scores, dim=-1)
output = weights @ V
```

## Key points

- Prevents information leakage from future tokens during training
- The mask is a constant that can be precomputed for a given sequence length
- Multi-head attention applies the same mask to each head independently

## Run tests

```bash
pytest modules/ml/llm/attention-causal/python -q
```
