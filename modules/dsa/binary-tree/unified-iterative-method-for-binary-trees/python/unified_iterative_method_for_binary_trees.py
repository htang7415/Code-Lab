from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []
    stack: list[tuple[TreeNode | None, bool]] = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            result.append(node.val)
        else:
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
            stack.append((node, True))
    return result


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []
    stack: list[tuple[TreeNode | None, bool]] = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            result.append(node.val)
        else:
            if node.right:
                stack.append((node.right, False))
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
    return result


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []
    stack: list[tuple[TreeNode | None, bool]] = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            result.append(node.val)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    return result
