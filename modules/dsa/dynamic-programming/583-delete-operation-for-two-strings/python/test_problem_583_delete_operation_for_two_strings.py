from problem_583_delete_operation_for_two_strings import Solution


def test_delete_operation_basic():
    assert Solution().minDistance("sea", "eat") == 2


def test_delete_operation_more():
    assert Solution().minDistance("leetcode", "etco") == 4
