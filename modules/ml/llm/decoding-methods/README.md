# Decoding Methods

> Track: `ml` | Topic: `llm`

## Concept

LLM decoding is the policy that turns next-token scores into an actual
generation path. Greedy decoding and beam search are deterministic ranking
methods; temperature, top-k, and top-p are stochastic filtering methods that
shape diversity and risk.

## Math

- $\mathrm{greedy}(z)=\arg\max_i z_i$
- $p_i=\frac{\exp(z_i/T)}{\sum_j \exp(z_j/T)}$
- $\mathrm{TopK}(p,k)$ keeps the $k$ highest-probability tokens
- $\mathrm{TopP}(p,p^\star)$ keeps the smallest prefix with cumulative mass at least $p^\star$
- $s(y_{1:t})=s(y_{1:t-1})+\log p(y_t\mid y_{<t})$

- $z_i$ -- logit for token $i$
- $T$ -- temperature
- $k$ -- fixed candidate count
- $p^\star$ -- nucleus threshold
- $s(y_{1:t})$ -- beam score of a partial sequence

## Key Points

- Greedy decoding is cheapest but can collapse to bland outputs.
- Beam search explores several high-score continuations but often reduces diversity.
- Temperature changes sharpness before any filtering happens.
- Top-k sets a hard cap on candidate count; top-p adapts to the probability shape.
- Real generation stacks these steps into one pipeline.

## Function

```python
def greedy_choice(scores: list[float]) -> int:
def temperature_probabilities(logits: list[float], temperature: float) -> list[float]:
def top_k_filter(probabilities: list[float], k: int) -> list[int]:
def top_p_filter(probabilities: list[float], p: float) -> list[int]:
def sampling_pipeline_candidates(
    logits: list[float],
    temperature: float,
    top_k: int,
    top_p: float,
) -> list[int]:
def beam_search_step(
    beams: list[tuple[list[int], float]],
    next_token_log_probs: list[list[float]],
    beam_width: int,
) -> list[tuple[list[int], float]]:
```

## Pitfalls

- Comparing beam search with sampling is a trade-off question, not a universal ranking.
- Temperature cannot rescue a broken candidate set if top-k or top-p is too restrictive.
- Top-p should be applied to normalized probabilities, not raw logits.
- Wider beams cost more compute and can over-favor generic high-likelihood text.

## Run tests

```bash
pytest modules/ml/llm/decoding-methods/python -q
```
