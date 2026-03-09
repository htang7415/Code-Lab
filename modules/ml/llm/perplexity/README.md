# Perplexity

> Track: `ml` | Topic: `llm`

## Concept

Perplexity measures how surprised a language model is by the true next tokens.
Lower perplexity means the model assigned higher probability to the observed sequence.

## Math

$$\mathrm{PPL} = \exp \left( - \frac{1}{n} \sum_{i=1}^{n} \log p_i \right)$$

- $n$ -- number of tokens
- $p_i$ -- probability assigned to the correct token at position $i$

## Key Points

- Perplexity is an intrinsic metric, not a direct measure of task usefulness.
- It is very sensitive to tokenization and evaluation setup.
- A perplexity of $1$ means the model assigns probability $1$ to every observed token.

## Function

```python
def perplexity(token_probs: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/perplexity/python -q
```
