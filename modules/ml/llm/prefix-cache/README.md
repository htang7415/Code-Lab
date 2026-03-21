# Prefix Cache Hit Length

> Track: `ml` | Topic: `llm`

## Concept

Prefix caching reuses work when a new prompt shares an initial token prefix with previously seen prompts.

## Math

$$h = \max_j \; \mathrm{LCP}(q, c_j)$$

- $h$ -- best cache hit length
- $q$ -- query prompt tokens
- $c_j$ -- cached prompt tokens
- $\mathrm{LCP}$ -- longest common prefix

## Key Points

- Cache value comes from shared prompt prefixes, not from arbitrary overlap.
- Longer prefix hits save more prefill compute.
- Workloads with repeated system prompts often benefit strongly.

## Function

```python
def longest_prefix_cache_hit(
    prompt_tokens: list[int],
    cached_prefixes: list[list[int]],
) -> int:
```

## References

- OpenAI (2024). [Prompt Caching in the API](https://openai.com/index/api-prompt-caching/)
- OpenAI. [Prompt caching](https://platform.openai.com/docs/guides/prompt-caching)

## Run tests

```bash
pytest modules/ml/llm/prefix-cache/python -q
```
