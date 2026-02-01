from problem_383_ransom_note import can_construct


def test_can_construct_true():
    assert can_construct("aab", "baa") is True


def test_can_construct_false():
    assert can_construct("aa", "ab") is False
