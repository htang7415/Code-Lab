from problem_62_unique_paths import Solution


def test_unique_paths_basic():
    assert Solution().uniquePaths(3, 7) == 28


def test_unique_paths_small():
    assert Solution().uniquePaths(3, 2) == 3
