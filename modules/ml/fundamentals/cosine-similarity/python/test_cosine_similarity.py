from cosine_similarity import cosine_similarity


def test_cosine_similarity():
    assert abs(cosine_similarity([1, 0], [1, 0]) - 1.0) < 1e-6
