from ab_testing import conversion_rate


def test_conversion_rate():
    assert conversion_rate(50, 100) == 0.5
