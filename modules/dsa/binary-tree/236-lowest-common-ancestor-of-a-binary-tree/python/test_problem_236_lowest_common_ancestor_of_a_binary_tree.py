from problem_236_lowest_common_ancestor_of_a_binary_tree import Solution, TreeNode


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


def find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def test_lca_binary_root():
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = find_node(root, 5)
    q = find_node(root, 1)
    assert Solution().lowestCommonAncestor(root, p, q).val == 3


def test_lca_binary_subtree():
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = find_node(root, 5)
    q = find_node(root, 4)
    assert Solution().lowestCommonAncestor(root, p, q).val == 5
