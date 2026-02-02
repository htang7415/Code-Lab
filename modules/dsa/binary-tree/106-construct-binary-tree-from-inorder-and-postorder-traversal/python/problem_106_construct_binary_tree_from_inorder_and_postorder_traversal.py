from __future__ import annotations

from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        index_map = {value: i for i, value in enumerate(inorder)}

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            idx = index_map[root_val]
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            return root

        return helper(0, len(inorder) - 1)
