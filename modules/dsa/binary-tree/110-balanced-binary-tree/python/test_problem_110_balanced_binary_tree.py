from problem_110_balanced_binary_tree import Solution, TreeNode


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


def test_balanced_true():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().isBalanced(root) is True


def test_balanced_false():
    root = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert Solution().isBalanced(root) is False
