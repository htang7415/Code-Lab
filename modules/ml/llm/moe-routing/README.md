# Sparse Mixture of Experts Layer

> Track: `ml` | Topic: `llm`

## Concept

A sparse Mixture of Experts (MoE) layer replaces one dense feedforward block
with many expert matrices and a small gating network. For each token, the gate
scores all experts, keeps only the top-k experts, renormalizes those gate
weights, and combines just the selected expert outputs.

This is conditional computation: the model has many parameters, but each token
uses only a small subset of them. That is why MoE layers can scale model
capacity without paying the full dense compute cost on every token.

## Math

For one token vector $x \in \mathbb{R}^{d_{\text{model}}}$:

$$g = \text{softmax}(x W_g), \qquad g \in \mathbb{R}^{n_{\text{experts}}}$$

$$\mathcal{K} = \text{TopK}(g, k)$$

$$y = \sum_{i \in \mathcal{K}} \frac{g_i}{\sum_{j \in \mathcal{K}} g_j}\,(x W_{e,i})$$

- $W_g$ -- gating weights, shape `(d_model, n_experts)`
- $W_{e,i}$ -- expert $i$ weight matrix, shape `(d_model, d_model)`
- $\mathcal{K}$ -- the selected top-k expert indices
- $y$ -- routed token output

## Key Points

- The gate computes a full softmax over experts, but only the top-k experts are
  used for the token's forward pass.
- Top-k probabilities are renormalized so the selected expert weights still sum
  to 1.
- Different tokens in the same batch can be sent to different experts.

## Function

```python
def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
def moe(
    x: np.ndarray,
    We: np.ndarray,
    Wg: np.ndarray,
    n_experts: int,
    top_k: int,
) -> np.ndarray:
```

- `x` -- input tensor of shape `(n_batch, l_seq, d_model)`
- `We` -- expert weights of shape `(n_experts, d_model, d_model)`
- `Wg` -- gating weights of shape `(d_model, n_experts)`
- `n_experts` -- total number of experts
- `top_k` -- number of experts selected per token
- Returns -- output tensor of shape `(n_batch, l_seq, d_model)`

## Run tests

```bash
pytest modules/ml/llm/moe-routing/python -q
```
