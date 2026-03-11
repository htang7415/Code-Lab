from __future__ import annotations

import pytest

from run_sampling import realized_sample_rate, sampled_run_ids, should_sample_run


def test_run_sampling_is_deterministic() -> None:
    run_ids = ["run_1", "run_2", "run_3", "run_4"]
    first = sampled_run_ids(run_ids, 0.5)
    second = sampled_run_ids(run_ids, 0.5)
    assert first == second
    assert realized_sample_rate(run_ids, 0.5) == len(first) / len(run_ids)
    assert isinstance(should_sample_run("run_1", 0.5), bool)


def test_run_sampling_validation() -> None:
    with pytest.raises(ValueError):
        should_sample_run("", 0.5)
    with pytest.raises(ValueError):
        sampled_run_ids(["run_1"], 1.5)
