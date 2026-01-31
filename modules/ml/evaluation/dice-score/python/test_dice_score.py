from dice_score import dice


def test_dice():
    assert dice({1, 2}, {2, 3}) == 2 / 4
