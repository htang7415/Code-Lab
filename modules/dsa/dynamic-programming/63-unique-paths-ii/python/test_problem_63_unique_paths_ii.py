from problem_63_unique_paths_ii import Solution


def test_unique_paths_with_obstacles_basic():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().uniquePathsWithObstacles(grid) == 2


def test_unique_paths_with_obstacles_small():
    grid = [[0, 1], [0, 0]]
    assert Solution().uniquePathsWithObstacles(grid) == 1
