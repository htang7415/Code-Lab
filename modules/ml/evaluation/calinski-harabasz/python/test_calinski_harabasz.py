from calinski_harabasz import calinski_harabasz


def test_calinski_harabasz():
    assert calinski_harabasz(10.0, 5.0, 2, 10) == 20.0
