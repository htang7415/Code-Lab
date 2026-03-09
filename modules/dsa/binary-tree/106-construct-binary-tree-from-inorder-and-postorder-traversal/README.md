# 106.Construct Binary Tree from Inorder and Postorder Traversal

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Rebuild the original binary tree from its inorder and postorder traversals.

## Recognition Cues

- You are given two traversal orders of the same tree.
- The values are unique, so each root position in inorder is unambiguous.
- One traversal identifies the root, while the other splits left and right subtrees.

## Baseline Idea

Take the last postorder value as the root, find it in inorder with a linear scan, and recurse on sliced subarrays. This works, but repeated scans and slicing add extra cost.

## Core Insight

The last postorder value is always the current root. In inorder, everything left of that root belongs to the left subtree and everything right belongs to the right subtree. With an index map, you can split in `O(1)`, and because postorder is consumed from the end, you must build the right subtree before the left subtree.

## Invariant / State

- `helper(left, right)` builds exactly the subtree whose inorder range is `[left, right]`.
- The remaining tail of `postorder` always ends with that subtree's root.

## Walkthrough

For `inorder = [9, 3, 15, 20, 7]` and `postorder = [9, 15, 7, 20, 3]`:
- Pop `3` from postorder, so `3` is the root.
- In inorder, `3` splits the array into left `[9]` and right `[15, 20, 7]`.
- Pop `20` next, so it becomes the root of the right subtree.
- Keep splitting by inorder positions until each range is empty.

## Complexity

- Time: `O(n)`
- Space: `O(n)` for the index map and recursion stack

## Edge Cases

- Empty traversals
- Single-node tree
- Fully skewed tree

## Common Mistakes

- Building the left subtree before the right subtree while popping from the end of postorder
- Scanning inorder every time instead of using an index map
- Forgetting that an empty inorder range means no node

## Pattern Transfer

- 105.Construct Binary Tree from Preorder and Inorder Traversal
- Divide-and-conquer tree construction
- Tree recursion over index ranges

## Self-Check

- Why does postorder reveal the root immediately?
- Why must the right subtree be built before the left subtree here?
- What does the inorder index tell you about subtree boundaries?

## Function

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/106-construct-binary-tree-from-inorder-and-postorder-traversal/python -q
```
