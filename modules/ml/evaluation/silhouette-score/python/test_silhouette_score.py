from silhouette_score import silhouette


def test_silhouette():
    assert silhouette(0.2, 0.6) == 0.6666666666666666
