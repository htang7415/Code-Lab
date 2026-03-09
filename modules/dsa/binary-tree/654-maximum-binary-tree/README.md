# 654.Maximum Binary Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Build a binary tree where each subtree root is the maximum value in its subarray.

## Recognition Cues

- The tree structure is defined directly by array maxima.
- Each root splits the array into a left part and a right part.
- The recursive structure comes from contiguous subarrays.

## Baseline Idea

For each subarray, scan for the maximum value, make it the root, and recurse on the left and right pieces. This is simple and matches the definition directly.

## Core Insight

The problem statement already describes a recursive decomposition: maximum becomes root, left slice builds the left subtree, right slice builds the right subtree.

## Invariant / State

- The subtree returned for a slice is the maximum binary tree of exactly that slice.
- Inorder traversal of the final tree reproduces the original array.

## Walkthrough

For `nums = [3, 2, 1, 6, 0, 5]`:
- The maximum is `6`, so `6` is the root.
- Left slice `[3, 2, 1]` builds the left subtree with root `3`.
- Right slice `[0, 5]` builds the right subtree with root `5`.
- Continue until each slice is empty.

## Complexity

- Time: `O(n^2)` in the worst case because each recursive call scans for a maximum
- Space: `O(n)` recursion stack in the worst case

## Edge Cases

- Empty array
- Single-element array
- Strictly increasing or decreasing input

## Common Mistakes

- Forgetting that the array slices must stay contiguous
- Assuming the tree is balanced
- Misreading inorder reconstruction as a BST rule

## Pattern Transfer

- Recursive tree construction from array structure
- Divide-and-conquer over subarrays
- Monotonic-stack optimization ideas

## Self-Check

- Why does the inorder traversal equal the original array?
- What input shape causes the worst-case recursion depth?
- How does the maximum value determine the subtree root?

## Function

```python
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/654-maximum-binary-tree/python -q
```
