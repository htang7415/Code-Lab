from tokenizer_comparison import compare_token_counts


def test_compare_token_counts_shows_subword_split() -> None:
    counts = compare_token_counts("playing now", {"play", "ing", "now"})

    assert counts == (2, 3)


def test_compare_token_counts_falls_back_to_single_char_units() -> None:
    counts = compare_token_counts("cat", {"ca"})

    assert counts == (1, 2)


def test_compare_token_counts_handles_empty_text() -> None:
    assert compare_token_counts("", {"a"}) == (0, 0)
