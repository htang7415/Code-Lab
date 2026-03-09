from problem_108_convert_sorted_array_to_bst import Solution, TreeNode


def inorder_traversal(root: TreeNode | None, out: list[int]) -> None:
    if root is None:
        return
    inorder_traversal(root.left, out)
    out.append(root.val)
    inorder_traversal(root.right, out)


def height(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root: TreeNode | None) -> bool:
    if root is None:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


def test_sorted_array_to_bst_example():
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)
    result: list[int] = []
    inorder_traversal(root, result)
    assert result == nums
    assert is_balanced(root) is True


def test_sorted_array_to_bst_edge_empty():
    assert Solution().sortedArrayToBST([]) is None


def test_sorted_array_to_bst_tricky_even_length():
    nums = [1, 2, 3, 4]
    root = Solution().sortedArrayToBST(nums)
    result: list[int] = []
    inorder_traversal(root, result)
    assert result == nums
    assert is_balanced(root) is True
