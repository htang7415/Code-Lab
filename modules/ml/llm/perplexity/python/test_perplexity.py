import pytest

from perplexity import perplexity


def test_perplexity_fair_coin_tokens():
    assert perplexity([0.5, 0.5]) == pytest.approx(2.0)


def test_perplexity_certain_predictions():
    assert perplexity([1.0, 1.0, 1.0]) == pytest.approx(1.0)
