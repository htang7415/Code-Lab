from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            traverse(node.right)
            self.total += node.val
            node.val = self.total
            traverse(node.left)

        traverse(root)
        return root
