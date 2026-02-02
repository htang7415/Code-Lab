from problem_669_trim_a_binary_search_tree import Solution, TreeNode


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


def test_trim_bst_basic():
    root = build_tree([1, 0, 2])
    trimmed = Solution().trimBST(root, 1, 2)
    values: list[int] = []
    inorder(trimmed, values)
    assert values == [1, 2]


def test_trim_bst_deeper():
    root = build_tree([3, 0, 4, None, 2, None, None, 1])
    trimmed = Solution().trimBST(root, 1, 3)
    values: list[int] = []
    inorder(trimmed, values)
    assert values == [1, 2, 3]
