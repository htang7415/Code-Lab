from alternative_deduplication_in_backtracking import Solution


def test_alternative_deduplication():
    result = Solution().subsetsWithDup([1, 2, 2])
    assert sorted(result) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
