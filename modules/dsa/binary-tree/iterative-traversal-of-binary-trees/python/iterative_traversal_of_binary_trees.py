from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    result: list[int] = []
    stack: list[TreeNode] = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []
    stack: list[TreeNode] = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        node = stack.pop()
        result.append(node.val)
        current = node.right
    return result


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []
    stack: list[TreeNode] = []
    current = root
    prev: TreeNode | None = None
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        node = stack[-1]
        if node.right and prev is not node.right:
            current = node.right
        else:
            result.append(node.val)
            prev = stack.pop()
    return result
