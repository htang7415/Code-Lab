from __future__ import annotations

from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths: list[str] = []

        def dfs(node: Optional[TreeNode], path: str) -> None:
            if node is None:
                return
            current = f"{path}{node.val}"
            if node.left is None and node.right is None:
                paths.append(current)
                return
            dfs(node.left, current + "->")
            dfs(node.right, current + "->")

        dfs(root, "")
        return paths
