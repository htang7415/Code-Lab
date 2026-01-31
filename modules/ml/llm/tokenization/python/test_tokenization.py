from tokenization import build_vocab, tokenize


def test_tokenize_basic():
    vocab = build_vocab(["hello world", "hello there"])
    ids = tokenize("hello world", vocab)
    assert ids == [vocab["hello"], vocab["world"]]
