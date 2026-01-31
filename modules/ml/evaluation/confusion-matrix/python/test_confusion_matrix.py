from confusion_matrix import confusion_matrix


def test_confusion_matrix():
    assert confusion_matrix([0, 1], [0, 0]) == [[1, 0], [1, 0]]
