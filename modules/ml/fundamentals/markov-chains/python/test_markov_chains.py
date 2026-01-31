from markov_chains import next_distribution


def test_next_distribution():
    p = [1.0, 0.0]
    t = [[0.0, 1.0], [1.0, 0.0]]
    assert next_distribution(p, t) == [0.0, 1.0]
