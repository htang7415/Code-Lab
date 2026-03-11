from cache_warming_patterns import recommend_warm_keys, serve_requests, warm_cache
import pytest


def test_recommendation_picks_hottest_keys_first():
    assert recommend_warm_keys({"doc:1": 100, "doc:2": 20, "doc:3": 5}, top_n=2) == [
        "doc:1",
        "doc:2",
    ]


def test_warming_reduces_origin_reads_on_first_request_burst():
    store = {"doc:1": "alpha", "doc:2": "beta"}
    requests = ["doc:1", "doc:1", "doc:2"]

    cold_responses, cold_origin_reads = serve_requests(store, {}, requests)

    warmed_cache: dict[str, str] = {}
    assert warm_cache(store, warmed_cache, ["doc:1"]) == ["doc:1"]
    warm_responses, warm_origin_reads = serve_requests(store, warmed_cache, requests)

    assert cold_responses == warm_responses
    assert warm_origin_reads < cold_origin_reads
    assert warm_origin_reads == 1


def test_invalid_warm_recommendation_inputs_are_rejected():
    with pytest.raises(ValueError, match="top_n"):
        recommend_warm_keys({"doc:1": 100}, top_n=-1)

    with pytest.raises(ValueError, match="access counts"):
        recommend_warm_keys({"doc:1": -1}, top_n=1)
