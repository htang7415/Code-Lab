from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)

    dfs(root)
    return result
