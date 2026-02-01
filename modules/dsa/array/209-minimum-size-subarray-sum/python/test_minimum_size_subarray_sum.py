from minimum_size_subarray_sum import Solution

def test_example_1():
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2

def test_example_2():
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1

def test_no_solution():
    assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1]) == 0
