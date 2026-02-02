from problem_763_partition_labels import Solution


def test_partition_labels_basic():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_partition_labels_single():
    assert Solution().partitionLabels("eccbbbbdec") == [10]
