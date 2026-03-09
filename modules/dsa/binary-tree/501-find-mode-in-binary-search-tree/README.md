# 501.Find Mode in Binary Search Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Return the value or values that appear most often in the BST.

## Recognition Cues

- Equal values appear consecutively in BST inorder order.
- You need frequency counts, but a full hash map is avoidable.
- Tracking the current run length is enough.

## Baseline Idea

Traverse all nodes, count with a hash map, then return the max-frequency values. That works, but inorder order lets you compress the counting state.

## Core Insight

During inorder traversal, repeated values appear in one consecutive run. Compare each node with the previous value and update the current run length.

## Invariant / State

- `prev` is the previous value seen in inorder order.
- `count` is the length of the current run.
- `max_count` is the best run length seen so far.

## Walkthrough

For BST `[2,1,2]`:
- Inorder visits `1,2,2`.
- The run for `2` reaches length `2`, so `2` becomes the mode.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Single node
- Multiple modes with equal frequency
- Repeated values appearing in one long inorder run

## Common Mistakes

- Resetting the count incorrectly on a new value
- Forgetting to clear prior modes when a larger frequency appears
- Using BST logic without relying on inorder sorted order

## Pattern Transfer

- 530.Minimum Absolute Difference in BST
- Inorder aggregation problems
- Run-length tracking over sorted traversal

## Self-Check

- Why does inorder order matter here?
- What does `count` represent?
- When should the modes list be cleared?

## Function

```python
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/501-find-mode-in-binary-search-tree/python -q
```
