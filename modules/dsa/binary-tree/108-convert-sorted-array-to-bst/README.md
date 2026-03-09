# 108.Convert Sorted Array to BST

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Turn a sorted array into a height-balanced binary search tree.

## Recognition Cues

- The input is already sorted.
- The output must satisfy BST order and stay balanced.
- Picking a middle element naturally splits the problem into two smaller sorted halves.

## Baseline Idea

Insert the numbers one by one into a BST. That preserves BST order, but for sorted input it becomes badly unbalanced.

## Core Insight

Choose the middle value as the root. Everything to the left is smaller and belongs in the left subtree, and everything to the right is larger and belongs in the right subtree. Repeating that choice keeps the tree balanced.

## Invariant / State

- `helper(left, right)` builds a balanced BST from `nums[left:right+1]`.
- The inorder traversal of the returned tree matches that slice exactly.

## Walkthrough

For `nums = [-10, -3, 0, 5, 9]`:
- Pick middle `0` as the root.
- Build the left subtree from `[-10, -3]`.
- Build the right subtree from `[5, 9]`.
- Each recursive step repeats the same middle-choice rule.

## Complexity

- Time: `O(n)`
- Space: `O(log n)` recursion stack for a balanced tree

## Edge Cases

- Empty array
- Single-element array
- Even-length array, where either middle convention can still be balanced

## Common Mistakes

- Picking an endpoint instead of a middle value
- Forgetting that the answer is not unique
- Checking only BST order and not balance

## Pattern Transfer

- Sorted data to balanced tree
- Divide-and-conquer on arrays
- 96.Unique Binary Search Trees for BST structure thinking

## Self-Check

- Why does choosing the middle preserve BST order?
- Why is the result balanced instead of skewed?
- What does the inorder traversal of the final tree look like?

## Function

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/108-convert-sorted-array-to-bst/python -q
```
