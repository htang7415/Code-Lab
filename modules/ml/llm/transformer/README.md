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

$$A(X) = \mathrm{softmax}\!\left(\frac{X X^\top}{\sqrt{d_{\text{model}}}}\right) X$$

$$Y = X + A(X),\quad Z = Y + \mathrm{FFN}(Y)$$

$$
\mathrm{FFN}(Y)=\mathrm{ReLU}(Y W_1) W_2
$$

- $X$ -- token representation matrix of shape $(T, d_{\text{model}})$
- $T$ -- number of tokens in the block
- $d_{\text{model}}$ -- model dimension used for attention scaling
- $A(X)$ -- self-attention output
- $Y$ -- residual output after attention
- $Z$ -- residual output after the feed-forward network
- $W_1, W_2$ -- feed-forward weights

## From Math To Code

- Compute attention weights first.
- Multiply those weights by the value matrix to get the attention output.
- Add residuals around attention and the feed-forward network.

## Function

```python
def attention_weights(x: list[list[float]]) -> list[list[float]]:
def self_attention_output(x: list[list[float]]) -> list[list[float]]:
def transformer_block(x: list[list[float]], w1: list[list[float]], w2: list[list[float]]) -> list[list[float]]:
```

## Minimal Code Mental Model

```python
weights = attention_weights(tokens)
attended = self_attention_output(tokens)
updated = transformer_block(tokens, w1, w2)
```

## Run tests

```bash
pytest modules/ml/llm/transformer/python -q
```
