from problem_455_assign_cookies import Solution


def test_assign_cookies_basic():
    assert Solution().findContentChildren([1, 2, 3], [1, 1]) == 1


def test_assign_cookies_more():
    assert Solution().findContentChildren([1, 2], [1, 2, 3]) == 2
