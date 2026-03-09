# Transformer Block (Minimal)

> Track: `ml` | Topic: `llm`

## Concept

A transformer block mixes token information with self-attention, then applies a
position-wise feed-forward network, with residual connections around both
sub-layers.

This lab is a deliberately minimal transformer-style block: it uses a single
attention head with $x$ acting directly as queries, keys, and values, and it
omits layer normalization, learned Q/K/V projections, and masking to keep the
implementation small enough to inspect line by line.

## Math

$$A(x) = \mathrm{softmax}\!\left(\frac{x x^\top}{\sqrt{d}}\right) x$$

$$y = x + A(x),\quad z = y + \mathrm{FFN}(y)$$

- $x$ -- token representation matrix
- $d$ -- hidden dimension used for attention scaling
- $A(x)$ -- self-attention output
- $y$ -- residual output after attention
- $z$ -- residual output after the feed-forward network

## Key Points

- Attention lets each token build a weighted combination of other token vectors.
- Residual connections preserve the original signal while adding learned
  updates.
- Real transformer blocks add more structure than this toy version; treat this
  module as a skeleton, not a full production block.

## Function

```python
def transformer_block(x: list[list[float]], w1: list[list[float]], w2: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/transformer/python -q
```
