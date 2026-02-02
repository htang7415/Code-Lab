from problem_131_palindrome_partitioning import Solution


def test_partition_basic():
    result = Solution().partition("aab")
    assert sorted(result) == [["a", "a", "b"], ["aa", "b"]]
