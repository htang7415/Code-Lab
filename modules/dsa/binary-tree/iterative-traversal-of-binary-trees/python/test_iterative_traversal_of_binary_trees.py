from iterative_traversal_of_binary_trees import (
    TreeNode,
    inorder_traversal,
    postorder_traversal,
    preorder_traversal,
)


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


def test_iterative_traversals():
    root = build_tree([1, 2, 3, 4, 5, None, 6])
    assert preorder_traversal(root) == [1, 2, 4, 5, 3, 6]
    assert inorder_traversal(root) == [4, 2, 5, 1, 3, 6]
    assert postorder_traversal(root) == [4, 5, 2, 6, 3, 1]
