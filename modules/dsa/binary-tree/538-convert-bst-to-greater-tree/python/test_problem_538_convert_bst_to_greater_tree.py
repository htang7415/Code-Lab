from problem_538_convert_bst_to_greater_tree import Solution, TreeNode


def inorder(node: TreeNode | None, out: list[int]) -> None:
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)


def test_convert_bst():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    result = Solution().convertBST(root)
    values: list[int] = []
    inorder(result, values)
    assert values == [6, 5, 3]
