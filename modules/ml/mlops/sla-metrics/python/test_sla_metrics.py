from sla_metrics import violation_rate


def test_violation_rate():
    assert violation_rate(2, 10) == 0.2
