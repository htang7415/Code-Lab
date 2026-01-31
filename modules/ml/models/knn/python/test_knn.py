from knn import knn_predict


def test_knn_predict():
    pred = knn_predict([0.1, 0.2, 0.3], [1, 1, 0], k=2)
    assert pred == 1
