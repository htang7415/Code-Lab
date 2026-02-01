from problem_242_valid_anagram import is_anagram


def test_is_anagram_true():
    assert is_anagram("anagram", "nagaram") is True


def test_is_anagram_false():
    assert is_anagram("rat", "car") is False
