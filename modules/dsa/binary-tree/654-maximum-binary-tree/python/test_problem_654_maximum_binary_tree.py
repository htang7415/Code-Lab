from problem_654_maximum_binary_tree import Solution, TreeNode


def inorder(node: TreeNode | None, out: list[int]) -> None:
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)


def test_maximum_binary_tree_inorder():
    nums = [3, 2, 1, 6, 0, 5]
    root = Solution().constructMaximumBinaryTree(nums)
    values: list[int] = []
    inorder(root, values)
    assert values == nums
