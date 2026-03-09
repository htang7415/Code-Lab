from problem_538_convert_bst_to_greater_tree import Solution, TreeNode


def inorder(node: TreeNode | None, out: list[int]) -> None:
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)


def test_convert_bst_example():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    result = Solution().convertBST(root)
    values: list[int] = []
    inorder(result, values)
    assert values == [6, 5, 3]


def test_convert_bst_edge_empty():
    assert Solution().convertBST(None) is None


def test_convert_bst_tricky_single():
    root = TreeNode(1)
    result = Solution().convertBST(root)
    values: list[int] = []
    inorder(result, values)
    assert values == [1]
