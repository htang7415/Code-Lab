from problem_701_insert_into_a_binary_search_tree import Solution, TreeNode


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


def test_insert_bst_example():
    root = build_tree([4, 2, 7, 1, 3])
    result = Solution().insertIntoBST(root, 5)
    values: list[int] = []
    inorder(result, values)
    assert values == [1, 2, 3, 4, 5, 7]


def test_insert_bst_edge_empty():
    result = Solution().insertIntoBST(None, 1)
    values: list[int] = []
    inorder(result, values)
    assert values == [1]


def test_insert_bst_tricky_deeper_branch():
    root = build_tree([5, 3, 7, 2, 4, None, 8])
    result = Solution().insertIntoBST(root, 6)
    values: list[int] = []
    inorder(result, values)
    assert values == [2, 3, 4, 5, 6, 7, 8]
