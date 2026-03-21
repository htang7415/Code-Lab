def _validate_head_counts(num_query_heads: int, num_kv_heads: int) -> None:
    if num_query_heads <= 0 or num_kv_heads <= 0:
        raise ValueError("head counts must be positive")
    if num_query_heads % num_kv_heads != 0:
        raise ValueError("num_query_heads must be divisible by num_kv_heads")


def kv_heads_for_layout(
    num_query_heads: int,
    layout: str,
    grouped_kv_heads: int | None = None,
) -> int:
    if num_query_heads <= 0:
        raise ValueError("num_query_heads must be positive")

    if layout == "mha":
        return num_query_heads
    if layout == "mqa":
        return 1
    if layout == "gqa":
        if grouped_kv_heads is None:
            raise ValueError("grouped_kv_heads is required for gqa")
        _validate_head_counts(num_query_heads=num_query_heads, num_kv_heads=grouped_kv_heads)
        return grouped_kv_heads
    raise ValueError("layout must be one of: mha, mqa, gqa")


def queries_per_kv_head(num_query_heads: int, num_kv_heads: int) -> int:
    _validate_head_counts(num_query_heads=num_query_heads, num_kv_heads=num_kv_heads)
    return num_query_heads // num_kv_heads


def kv_cache_fraction(num_query_heads: int, num_kv_heads: int) -> float:
    _validate_head_counts(num_query_heads=num_query_heads, num_kv_heads=num_kv_heads)
    return num_kv_heads / num_query_heads


def kv_cache_reduction_ratio(num_query_heads: int, num_kv_heads: int) -> float:
    return 1.0 - kv_cache_fraction(num_query_heads=num_query_heads, num_kv_heads=num_kv_heads)
