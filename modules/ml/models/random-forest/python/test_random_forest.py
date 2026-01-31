from random_forest import bootstrap_indices


def test_bootstrap_indices_len():
    assert len(bootstrap_indices(5, seed=1)) == 5
