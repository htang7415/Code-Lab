from return_discount import discounted_return


def test_discounted_return():
    assert discounted_return([1.0, 1.0], 0.5) == 1.5
