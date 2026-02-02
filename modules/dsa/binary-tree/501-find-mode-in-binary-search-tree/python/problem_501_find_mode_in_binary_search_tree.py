from __future__ import annotations

from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev: int | None = None
        self.count = 0
        self.max_count = 0
        modes: list[int] = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
            if self.count > self.max_count:
                self.max_count = self.count
                modes.clear()
                modes.append(node.val)
            elif self.count == self.max_count:
                modes.append(node.val)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return modes
