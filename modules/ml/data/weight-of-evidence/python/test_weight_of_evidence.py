import pytest

from weight_of_evidence import weight_of_evidence


def test_weight_of_evidence_is_positive_for_category_skewed_toward_positive_class() -> None:
    score = weight_of_evidence(
        positive_count=30,
        negative_count=10,
        total_positive=100,
        total_negative=100,
    )

    assert score > 0.0


def test_weight_of_evidence_is_zero_when_class_rates_match() -> None:
    score = weight_of_evidence(
        positive_count=20,
        negative_count=20,
        total_positive=100,
        total_negative=100,
    )

    assert score == pytest.approx(0.0)


def test_weight_of_evidence_requires_positive_class_totals() -> None:
    with pytest.raises(ValueError, match="positive"):
        weight_of_evidence(positive_count=1, negative_count=1, total_positive=0, total_negative=10)
