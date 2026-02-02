from problem_104_maximum_depth_of_binary_tree import Solution, TreeNode


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


def test_max_depth_basic():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().maxDepth(root) == 3


def test_max_depth_empty():
    assert Solution().maxDepth(None) == 0
