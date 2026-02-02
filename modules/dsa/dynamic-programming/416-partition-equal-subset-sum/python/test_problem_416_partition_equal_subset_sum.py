from problem_416_partition_equal_subset_sum import Solution


def test_partition_true():
    assert Solution().canPartition([1, 5, 11, 5]) is True


def test_partition_false():
    assert Solution().canPartition([1, 2, 3, 5]) is False
