from canary_deployment import split_traffic


def test_split_traffic():
    assert split_traffic(100, 0.1) == (10, 90)
