from problem_496_next_greater_element_i import Solution


def test_next_greater_element_example():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert Solution().nextGreaterElement(nums1, nums2) == [-1, 3, -1]


def test_next_greater_element_simple():
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    assert Solution().nextGreaterElement(nums1, nums2) == [3, -1]
