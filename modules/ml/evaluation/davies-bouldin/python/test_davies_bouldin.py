from davies_bouldin import davies_bouldin


def test_davies_bouldin():
    assert davies_bouldin(0.5, 0.5, 2.0) == 0.5
