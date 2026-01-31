from svm_pegasos import pegasos_step


def test_pegasos_step():
    w = pegasos_step([0.0, 0.0], [1.0, 0.0], 1, 0.1, 0.1)
    assert w[0] > 0.0
