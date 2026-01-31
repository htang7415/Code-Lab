from two_sample_t_test import t_stat


def test_t_stat():
    assert t_stat([1, 1, 1], [2, 2, 2]) < 0
