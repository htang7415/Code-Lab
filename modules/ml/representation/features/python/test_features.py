from features import bag_of_words


def test_bag_of_words_counts():
    tokens = ["cat", "dog", "cat"]
    vocab = ["cat", "dog", "mouse"]
    assert bag_of_words(tokens, vocab) == [2, 1, 0]


def test_bag_of_words_ignores_unknown():
    tokens = ["cat", "bird"]
    vocab = ["cat"]
    assert bag_of_words(tokens, vocab) == [1]
