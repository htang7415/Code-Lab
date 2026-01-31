from data_quality_checks import missing_rate


def test_missing_rate():
    assert missing_rate([1.0, None, 2.0]) == 1 / 3
