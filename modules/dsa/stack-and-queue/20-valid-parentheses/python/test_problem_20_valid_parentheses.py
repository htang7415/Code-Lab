from problem_20_valid_parentheses import Solution


def test_valid_parentheses_true():
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("{[]}") is True


def test_valid_parentheses_false():
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("(") is False
