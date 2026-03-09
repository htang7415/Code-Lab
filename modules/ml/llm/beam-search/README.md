# Beam Search Step

> Track: `ml` | Topic: `llm`

## Concept

Beam search keeps only the best few partial sequences at each decoding step instead of exploring every continuation.

## Math

$$s(y_{1:t}) = s(y_{1:t-1}) + \log p(y_t \mid y_{<t})$$

- $s(y_{1:t})$ -- cumulative log-score of a partial sequence
- $y_t$ -- next token
- $p(y_t \mid y_{<t})$ -- model probability for the next token

## Key Points

- Beam search is deterministic once the scores are fixed.
- Wider beams explore more candidates but cost more compute.
- This module models one expansion step, not full sequence termination logic.

## Function

```python
def beam_search_step(
    beams: list[tuple[list[int], float]],
    next_token_log_probs: list[list[float]],
    beam_width: int,
) -> list[tuple[list[int], float]]:
```

## Run tests

```bash
pytest modules/ml/llm/beam-search/python -q
```
