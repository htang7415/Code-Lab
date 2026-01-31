from f1_score import f1_score


def test_f1_score():
    assert f1_score(0.5, 0.5) == 0.5
