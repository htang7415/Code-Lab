from __future__ import annotations

def build_vocab(texts: list[str]) -> dict[str, int]:
    vocab: dict[str, int] = {}
    for text in texts:
        for token in text.lower().split():
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab


def tokenize(text: str, vocab: dict[str, int]) -> list[int]:
    return [vocab[token] for token in text.lower().split() if token in vocab]
