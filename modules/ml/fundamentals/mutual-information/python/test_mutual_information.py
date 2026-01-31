from mutual_information import mutual_information


def test_mutual_information():
    joint = [[0.25, 0.25], [0.25, 0.25]]
    assert mutual_information(joint) == 0.0
