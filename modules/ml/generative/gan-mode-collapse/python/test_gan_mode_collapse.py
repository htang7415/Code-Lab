from gan_mode_collapse import diversity_score


def test_diversity_score():
    assert diversity_score([1, 1, 1]) == 1 / 3
