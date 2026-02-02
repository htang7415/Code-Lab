from problem_501_find_mode_in_binary_search_tree import Solution, TreeNode


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


def test_find_mode_single():
    root = build_tree([1, None, 2, 2])
    assert Solution().findMode(root) == [2]


def test_find_mode_multiple():
    root = build_tree([2, 1, 2])
    assert Solution().findMode(root) == [2]
