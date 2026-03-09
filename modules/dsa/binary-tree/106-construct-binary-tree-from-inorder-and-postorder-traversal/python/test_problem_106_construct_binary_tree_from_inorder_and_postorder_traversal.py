from problem_106_construct_binary_tree_from_inorder_and_postorder_traversal import Solution, TreeNode


def level_order(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []
    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def test_build_tree_example():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = Solution().buildTree(inorder, postorder)
    assert level_order(root) == [3, 9, 20, None, None, 15, 7]


def test_build_tree_edge_empty():
    assert Solution().buildTree([], []) is None


def test_build_tree_tricky_right_skewed():
    inorder = [1, 2, 3]
    postorder = [3, 2, 1]
    root = Solution().buildTree(inorder, postorder)
    assert level_order(root) == [1, None, 2, None, 3]
