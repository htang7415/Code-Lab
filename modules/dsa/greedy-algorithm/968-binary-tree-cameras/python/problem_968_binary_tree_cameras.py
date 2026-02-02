from __future__ import annotations

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 0: not covered, 1: has camera, 2: covered
        self.cameras = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 2
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.cameras += 1
                return 1
            if left == 1 or right == 1:
                return 2
            return 0

        if dfs(root) == 0:
            self.cameras += 1
        return self.cameras
