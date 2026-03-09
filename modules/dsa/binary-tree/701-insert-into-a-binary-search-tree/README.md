# 701.Insert into a Binary Search Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Insert a new value into a BST while preserving BST order.

## Recognition Cues

- The input is a BST.
- The new value must end up on one root-to-leaf search path.
- Each comparison decides whether to go left or right.

## Baseline Idea

Collect all values, add the new one, sort, and rebuild the whole BST. That works, but it throws away the structure you already have.

## Core Insight

A BST insertion only needs local comparisons. Recurse left if the new value is smaller, recurse right if it is larger, and create a node when you reach an empty child position.

## Invariant / State

- Before and after insertion, every subtree remains a valid BST.
- Only one search path is modified.

## Walkthrough

For root `4` and `val = 5`:
- `5 > 4`, so move right to `7`.
- `5 < 7`, so move left.
- That child is empty, so place the new node there.

## Complexity

- Time: `O(h)` where `h` is the tree height
- Space: `O(h)` recursion stack

## Edge Cases

- Empty tree
- Insert the new minimum
- Insert the new maximum
- Highly skewed BST

## Common Mistakes

- Rebuilding the whole tree instead of following one path
- Returning the wrong subtree root during recursion
- Forgetting that an empty tree should create a new root

## Pattern Transfer

- BST search
- BST delete
- Recursive descent guided by ordering

## Self-Check

- Why is only one path affected by insertion?
- What does the base case return for an empty child?
- How does tree height affect runtime?

## Function

```python
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/701-insert-into-a-binary-search-tree/python -q
```
