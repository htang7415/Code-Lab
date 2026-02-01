from spiral_matrix_ii import Solution

def test_n_1():
    assert Solution().generateMatrix(1) == [[1]]

def test_n_3():
    assert Solution().generateMatrix(3) == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]
