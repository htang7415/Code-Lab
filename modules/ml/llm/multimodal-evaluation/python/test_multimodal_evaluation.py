from __future__ import annotations

import pytest

from multimodal_evaluation import (
    average_multimodal_accuracy,
    modality_coverage_rate,
    vqa_consensus_accuracy,
)


def test_multimodal_evaluation_helpers_cover_consensus_and_modality_presence() -> None:
    assert vqa_consensus_accuracy(0) == pytest.approx(0.0)
    assert vqa_consensus_accuracy(2) == pytest.approx(2 / 3)
    assert vqa_consensus_accuracy(4) == pytest.approx(1.0)
    assert modality_coverage_rate(["text", "image"], ["text", "image"]) == pytest.approx(1.0)
    assert modality_coverage_rate(["text", "image", "audio"], ["text", "audio"]) == pytest.approx(
        2 / 3
    )


def test_average_multimodal_accuracy_aggregates_example_scores() -> None:
    assert average_multimodal_accuracy([1.0, 2 / 3, 1.0]) == pytest.approx((1 + 2 / 3 + 1) / 3)


def test_multimodal_evaluation_validation_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        vqa_consensus_accuracy(-1)
    with pytest.raises(ValueError):
        average_multimodal_accuracy([1.2])
