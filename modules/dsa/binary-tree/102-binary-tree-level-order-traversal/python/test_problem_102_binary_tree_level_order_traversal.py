from problem_102_binary_tree_level_order_traversal import Solution, TreeNode


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


def test_level_order_basic():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]


def test_level_order_empty():
    assert Solution().levelOrder(None) == []
