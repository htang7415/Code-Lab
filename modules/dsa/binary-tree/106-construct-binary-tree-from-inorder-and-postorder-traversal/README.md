# 106.Construct Binary Tree from Inorder and Postorder Traversal

> Track: `dsa` | Topic: `binary-tree`

## Concept

Use postorder's last element as root and split inorder ranges.

## Function

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
```
