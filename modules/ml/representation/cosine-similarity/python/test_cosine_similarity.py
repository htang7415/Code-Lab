import math

from cosine_similarity import cosine_similarity


def test_cosine_similarity_identity():
    assert math.isclose(cosine_similarity([1.0, 0.0], [1.0, 0.0]), 1.0, rel_tol=1e-6)


def test_cosine_similarity_orthogonal():
    assert math.isclose(cosine_similarity([1.0, 0.0], [0.0, 1.0]), 0.0, abs_tol=1e-6)


def test_cosine_similarity_opposite():
    assert math.isclose(cosine_similarity([1.0, 0.0], [-1.0, 0.0]), -1.0, rel_tol=1e-6)
