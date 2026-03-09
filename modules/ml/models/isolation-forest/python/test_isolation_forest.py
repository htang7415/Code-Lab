import pytest

from isolation_forest import isolation_score


def test_isolation_score_shorter_paths_are_more_anomalous():
    short_path = isolation_score(avg_path_length=2.0, sample_size=8)
    long_path = isolation_score(avg_path_length=5.0, sample_size=8)
    assert short_path > long_path


def test_isolation_score_known_value():
    assert isolation_score(avg_path_length=3.0, sample_size=4) == pytest.approx(0.3829915893, rel=1e-5)
