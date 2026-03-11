from compaction_vs_repair_tradeoffs import (
    compacted_levels,
    recommended_action,
    tradeoff_summary,
)
import pytest


def test_high_read_amplification_points_to_compaction():
    summary = tradeoff_summary([3, 5, 10], divergent_key_count=0)

    assert compacted_levels([3, 5, 10]) == [1, 1, 1]
    assert summary["read_amp_after_compaction"] < summary["read_amp_before"]
    assert summary["recommended_action"] == "compaction"


def test_divergence_points_to_repair_even_if_read_amplification_is_low():
    assert recommended_action([1, 1], divergent_key_count=3) == "repair"
    assert recommended_action([3, 5, 10], divergent_key_count=2) == "both"


def test_invalid_tradeoff_inputs_are_rejected():
    with pytest.raises(ValueError, match="divergent_key_count"):
        tradeoff_summary([3, 5, 10], divergent_key_count=-1)

    with pytest.raises(ValueError, match="read_amp_threshold"):
        recommended_action([3, 5, 10], divergent_key_count=0, read_amp_threshold=0)
