from problem_139_word_break import Solution


def test_word_break_example():
    assert Solution().wordBreak("leetcode", ["leet", "code"]) is True


def test_word_break_edge_empty():
    assert Solution().wordBreak("", ["leet", "code"]) is True


def test_word_break_tricky_false():
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
