import math

import pytest

from bleu_meteor import bleu1_meteor


def test_bleu1_meteor_are_perfect_for_exact_match() -> None:
    bleu1, meteor = bleu1_meteor("the cat sat", "the cat sat")

    assert bleu1 == 1.0
    assert meteor == 1.0


def test_bleu1_meteor_capture_brevity_and_recall_tradeoff() -> None:
    bleu1, meteor = bleu1_meteor("cat sat", "the cat sat")

    assert bleu1 == pytest.approx(math.exp(-0.5))
    assert meteor == pytest.approx(20.0 / 29.0)


def test_bleu1_meteor_requires_tokens() -> None:
    with pytest.raises(ValueError, match="at least one token"):
        bleu1_meteor("", "reference")
