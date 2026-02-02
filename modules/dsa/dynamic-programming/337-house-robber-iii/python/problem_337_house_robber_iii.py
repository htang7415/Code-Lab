from __future__ import annotations

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if node is None:
                return (0, 0)
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            rob_this = node.val + left_skip + right_skip
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
            return (rob_this, skip_this)

        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)
