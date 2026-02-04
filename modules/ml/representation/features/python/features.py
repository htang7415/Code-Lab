def bag_of_words(tokens: list[str], vocab: list[str]) -> list[int]:
    index = {token: i for i, token in enumerate(vocab)}
    counts = [0] * len(vocab)
    for token in tokens:
        position = index.get(token)
        if position is not None:
            counts[position] += 1
    return counts
