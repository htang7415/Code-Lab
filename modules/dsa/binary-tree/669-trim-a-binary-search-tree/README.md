# 669.Trim a Binary Search Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Remove all BST nodes whose values fall outside the inclusive range `[low, high]`.

## Recognition Cues

- The input tree is a BST.
- You need to drop whole branches based on value comparisons.
- The allowed value range is inclusive.

## Baseline Idea

Traverse every node, delete invalid ones, and reconnect the rest manually. That works, but it ignores the ordering power of the BST.

## Core Insight

If `root.val < low`, then the entire left subtree is too small and can be discarded. If `root.val > high`, then the entire right subtree is too large and can be discarded. Only nodes inside the range need both children trimmed recursively.

## Invariant / State

- Every returned subtree is still a valid BST.
- Every node in the returned subtree lies inside `[low, high]`.

## Walkthrough

For root `3` with range `[1, 3]`:
- `3` stays because it is inside the range.
- Its left child `0` is too small, so that branch is replaced by trimming its right side.
- Its right child `4` is too large, so that branch is replaced by trimming its left side.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Root outside the range
- All nodes trimmed away
- Boundary values equal to `low` or `high`

## Common Mistakes

- Trimming children even after the root itself should be skipped
- Treating the range as exclusive instead of inclusive
- Forgetting that a whole BST branch can be discarded immediately

## Pattern Transfer

- BST pruning by range
- Search and delete decisions using BST ordering
- Recursive tree filtering

## Self-Check

- Why can an entire left subtree be discarded when `root.val < low`?
- Why does BST ordering make the pruning faster to reason about?
- What should be returned if every node is out of range?

## Function

```python
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/669-trim-a-binary-search-tree/python -q
```
