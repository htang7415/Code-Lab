from elastic_net import elastic_net_penalty


def test_elastic_net_penalty():
    assert elastic_net_penalty([1.0, -2.0], 0.1, 0.1) == 0.3 + 0.5
