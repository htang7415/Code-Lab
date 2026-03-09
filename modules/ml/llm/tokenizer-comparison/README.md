# Tokenizer Count Comparison

> Track: `ml` | Topic: `llm`

## Concept

Different tokenizers can represent the same text with very different token counts.
This module compares whitespace tokenization with a greedy subword tokenizer.

## Math

$$n_{\mathrm{word}} \ne n_{\mathrm{subword}}$$

- $n_{\mathrm{word}}$ -- number of whitespace tokens
- $n_{\mathrm{subword}}$ -- number of greedy subword tokens

## Key Points

- Token count affects context usage, cost, and perplexity comparisons.
- Subword tokenization can split one word into several smaller units.
- This module uses a simple greedy longest-match tokenizer, not a full BPE trainer.

## Function

```python
def compare_token_counts(text: str, subword_vocab: set[str]) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/ml/llm/tokenizer-comparison/python -q
```
