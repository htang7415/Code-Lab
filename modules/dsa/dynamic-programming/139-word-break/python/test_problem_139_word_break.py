from problem_139_word_break import Solution


def test_word_break_true():
    assert Solution().wordBreak("leetcode", ["leet", "code"]) is True


def test_word_break_false():
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
