# 538.Convert BST to Greater Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Replace each BST node value with its original value plus the sum of all greater values.

## Recognition Cues

- The operation depends on “all larger values.”
- A BST visited in reverse inorder gives values from largest to smallest.
- A running suffix sum is enough.

## Baseline Idea

Collect all values, sort them, compute suffix sums, then traverse again to rewrite nodes. That works, but reverse inorder does it in one pass.

## Core Insight

Traverse the BST in reverse inorder: right, node, left. Maintain a running total of values already seen, which are exactly the greater values.

## Invariant / State

- `total` is the sum of all node values greater than or equal to the current node among the nodes already visited in reverse inorder.

## Walkthrough

For BST `1 <- 2 -> 3`:
- Visit `3`, total becomes `3`.
- Visit `2`, total becomes `5`, so node `2` becomes `5`.
- Visit `1`, total becomes `6`, so node `1` becomes `6`.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Single node
- Right-skewed BST

## Common Mistakes

- Using normal inorder instead of reverse inorder
- Updating `total` after overwriting the node incorrectly
- Forgetting that greater values are all on the right side in a BST

## Pattern Transfer

- Reverse inorder BST traversal
- Prefix/suffix aggregation on trees
- 530.Minimum Absolute Difference in BST

## Self-Check

- Why is reverse inorder the right order?
- What does `total` mean before and after visiting a node?
- How does the BST property make this one-pass update possible?

## Function

```python
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/538-convert-bst-to-greater-tree/python -q
```
