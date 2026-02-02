from problem_450_delete_node_in_a_bst import Solution, TreeNode


def build_tree(values: list[int | None]) -> TreeNode | None:
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def inorder(node: TreeNode | None, out: list[int]) -> None:
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)


def test_delete_node_leaf():
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    result = Solution().deleteNode(root, 3)
    values: list[int] = []
    inorder(result, values)
    assert values == [2, 4, 5, 6, 7]


def test_delete_node_root():
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    result = Solution().deleteNode(root, 5)
    values: list[int] = []
    inorder(result, values)
    assert values == [2, 3, 4, 6, 7]
