# Chunked Prefill Rounds

> Track: `ml` | Topic: `systems`

## Concept

Chunked prefill breaks a long prompt into smaller prefill slices so the scheduler can interleave work instead of letting one huge prompt monopolize the prefill stage.

## Math

$$r_i = \left\lceil \frac{L_i}{C} \right\rceil$$

$$T_t = \sum_i \min(R_{i,t}, C)$$

- $L_i$ -- prompt length for request $i$
- $C$ -- chunk size
- $r_i$ -- number of prefill rounds required for request $i$
- $R_{i,t}$ -- remaining prompt tokens for request $i$ at round $t$
- $T_t$ -- total prefill tokens processed in round $t$

## Key Points

- Chunking does not reduce total prompt tokens; it changes when they are processed.
- The main benefit is lower tail latency and better scheduler fairness.
- Very small chunks improve interleaving but can add overhead.

## Function

```python
def chunked_prefill_rounds(prompt_lengths: list[int], chunk_size: int) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/systems/chunked-prefill/python -q
```
