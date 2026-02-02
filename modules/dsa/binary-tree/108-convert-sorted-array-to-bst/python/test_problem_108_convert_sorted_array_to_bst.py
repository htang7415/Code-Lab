from problem_108_convert_sorted_array_to_bst import Solution, TreeNode


def inorder_traversal(root: TreeNode | None, out: list[int]) -> None:
    if root is None:
        return
    inorder_traversal(root.left, out)
    out.append(root.val)
    inorder_traversal(root.right, out)


def test_sorted_array_to_bst_inorder():
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)
    result: list[int] = []
    inorder_traversal(root, result)
    assert result == nums
