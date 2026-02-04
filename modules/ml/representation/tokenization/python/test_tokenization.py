from tokenization import simple_tokenize


def test_simple_tokenize_basic():
    assert simple_tokenize("Hello, world!") == ["hello", "world"]


def test_simple_tokenize_numbers_and_hyphen():
    assert simple_tokenize("ML-101 is fun") == ["ml", "101", "is", "fun"]
