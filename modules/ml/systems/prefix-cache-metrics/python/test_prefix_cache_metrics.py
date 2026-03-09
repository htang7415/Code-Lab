import pytest

from prefix_cache_metrics import prefix_cache_savings


def test_prefix_cache_savings_returns_saved_tokens_and_fraction() -> None:
    saved_tokens, saved_fraction = prefix_cache_savings(
        prompt_lengths=[100, 50, 20],
        hit_lengths=[80, 0, 20],
    )

    assert saved_tokens == 100
    assert saved_fraction == pytest.approx(100 / 170)


def test_prefix_cache_savings_handles_full_miss_workload() -> None:
    saved_tokens, saved_fraction = prefix_cache_savings(
        prompt_lengths=[32, 64],
        hit_lengths=[0, 0],
    )

    assert saved_tokens == 0
    assert saved_fraction == 0.0


def test_prefix_cache_savings_validates_hit_lengths() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        prefix_cache_savings([16], [17])
