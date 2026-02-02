from problem_101_symmetric_tree import Solution, TreeNode


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


def test_symmetric_true():
    root = build_tree([1, 2, 2, 3, 4, 4, 3])
    assert Solution().isSymmetric(root) is True


def test_symmetric_false():
    root = build_tree([1, 2, 2, None, 3, None, 3])
    assert Solution().isSymmetric(root) is False
