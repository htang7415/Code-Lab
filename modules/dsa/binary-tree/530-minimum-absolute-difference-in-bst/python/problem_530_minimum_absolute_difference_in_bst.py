from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            raise ValueError("BST must contain at least two nodes")

        self.prev: int | None = None
        self.min_diff: int | None = None

        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None:
                diff = node.val - self.prev
                if self.min_diff is None:
                    self.min_diff = diff
                else:
                    self.min_diff = min(self.min_diff, diff)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        if self.min_diff is None:
            raise ValueError("BST must contain at least two nodes")
        return self.min_diff
