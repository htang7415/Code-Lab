from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode], low: int | None, high: int | None) -> bool:
            if node is None:
                return True
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, None, None)
