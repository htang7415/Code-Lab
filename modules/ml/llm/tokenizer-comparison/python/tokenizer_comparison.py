from __future__ import annotations


def _greedy_subword_count(word: str, subword_vocab: set[str]) -> int:
    count = 0
    position = 0
    while position < len(word):
        longest = ""
        for token in subword_vocab:
            if word.startswith(token, position) and len(token) > len(longest):
                longest = token
        if longest:
            position += len(longest)
        else:
            position += 1
        count += 1
    return count


def compare_token_counts(text: str, subword_vocab: set[str]) -> tuple[int, int]:
    words = text.lower().split()
    word_count = len(words)
    subword_count = sum(_greedy_subword_count(word, subword_vocab) for word in words)
    return word_count, subword_count
