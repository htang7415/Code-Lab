from cache_admission_policies import (
    admit_on_frequency,
    admitted_keys,
    request_counts,
)


def test_frequency_gate_rejects_one_hit_noise() -> None:
    stream = ["cold-1", "hot", "hot", "cold-2", "hot", "warm", "warm"]
    counts = request_counts(stream)

    assert admit_on_frequency("cold-1", counts, min_hits=2) is False
    assert admit_on_frequency("hot", counts, min_hits=2) is True
    assert admit_on_frequency("warm", counts, min_hits=2) is True


def test_admitted_keys_returns_stable_first_seen_order() -> None:
    stream = ["cold-1", "hot", "hot", "cold-2", "warm", "warm", "hot"]

    assert admitted_keys(stream, min_hits=2) == {
        "always": ["cold-1", "hot", "cold-2", "warm"],
        "frequency_threshold": ["hot", "warm"],
        "rejected_by_frequency": ["cold-1", "cold-2"],
    }


def test_min_hits_of_one_admits_every_seen_key() -> None:
    stream = ["a", "b", "a"]

    assert admitted_keys(stream, min_hits=1)["frequency_threshold"] == ["a", "b"]
