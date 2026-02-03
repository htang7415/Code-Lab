# Transformer Block

> Track: `ml` | Topic: `llm`

## Concept

A transformer block applies self-attention, a feed-forward network, and residual connections.

## Math
$$y = x + \mathrm{Attention}(x),\quad z = y + \mathrm{FFN}(y)$$

- $y$ -- target/label
- $x$ -- input (feature vector or sample)
- $z$ -- latent or pre-activation value

## Function

```python
def transformer_block(x: list[list[float]], w1: list[list[float]], w2: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/transformer/python -q
```