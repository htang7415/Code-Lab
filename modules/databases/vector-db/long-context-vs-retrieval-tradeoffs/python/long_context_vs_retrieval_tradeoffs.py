"""long_context_vs_retrieval_tradeoffs - compare token load and fit for long context versus retrieval."""

from __future__ import annotations


def long_context_token_load(source_tokens: int, prompt_overhead: int = 0) -> int:
    return max(source_tokens, 0) + max(prompt_overhead, 0)


def retrieval_token_load(
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> int:
    return max(top_k, 0) * max(avg_chunk_tokens, 0) + max(prompt_overhead, 0)


def fits_context_window(total_tokens: int, model_window: int) -> bool:
    return total_tokens <= model_window


def choose_strategy(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> str:
    long_load = long_context_token_load(source_tokens, prompt_overhead)
    retrieval_load = retrieval_token_load(top_k, avg_chunk_tokens, prompt_overhead)
    relevant_fraction = 0.0 if source_tokens <= 0 else relevant_tokens / source_tokens

    if not fits_context_window(long_load, model_window):
        return "retrieval"
    if relevant_fraction >= 0.7:
        return "long-context"
    return "retrieval"


def strategy_summary(
    source_tokens: int,
    relevant_tokens: int,
    model_window: int,
    top_k: int,
    avg_chunk_tokens: int,
    prompt_overhead: int = 0,
) -> dict[str, int | float | str | bool]:
    long_load = long_context_token_load(source_tokens, prompt_overhead)
    retrieval_load = retrieval_token_load(top_k, avg_chunk_tokens, prompt_overhead)
    return {
        "long_context_tokens": long_load,
        "retrieval_tokens": retrieval_load,
        "fits_long_context": fits_context_window(long_load, model_window),
        "relevant_fraction": 0.0 if source_tokens <= 0 else relevant_tokens / source_tokens,
        "choice": choose_strategy(
            source_tokens,
            relevant_tokens,
            model_window,
            top_k,
            avg_chunk_tokens,
            prompt_overhead,
        ),
    }
