# 110.Balanced Binary Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Decide whether every node’s left and right subtrees differ in height by at most one.

## Recognition Cues

- The property depends on subtree heights everywhere, not just at the root.
- A bottom-up traversal can detect failure early.
- Returning only heights is not enough unless imbalance can propagate.

## Baseline Idea

Compute the height of every subtree separately and recheck balance at each node. That works, but it recomputes heights repeatedly.

## Core Insight

Use postorder traversal and return `-1` as a sentinel when a subtree is already unbalanced, so failure propagates upward immediately.

## Invariant / State

- `height(node)` returns the subtree height if balanced, otherwise `-1`.

## Walkthrough

For an unbalanced chain under one side:
- Deep recursion computes child heights first.
- Once a node sees a height difference greater than `1`, it returns `-1`.
- Every ancestor propagates that `-1`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single node
- A skewed tree

## Common Mistakes

- Recomputing heights top-down at every node
- Ignoring imbalance discovered in a child subtree
- Using `0` instead of a sentinel for failure

## Pattern Transfer

- 104.Maximum Depth of Binary Tree
- Postorder tree DP
- Sentinel-return recursive patterns

## Self-Check

- Why is postorder traversal natural here?
- What does `-1` mean?
- How does the sentinel avoid repeated work?

## Function

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/110-balanced-binary-tree/python -q
```
