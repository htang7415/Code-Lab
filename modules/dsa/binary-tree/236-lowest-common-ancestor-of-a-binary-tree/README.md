# 236.Lowest Common Ancestor of a Binary Tree

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Find the lowest node in the binary tree that has both `p` and `q` in its subtree.

## Recognition Cues

- This is a general binary tree, so BST ordering does not help.
- The answer depends on where two searches meet.
- A postorder recursion can ask each subtree whether it contains `p` or `q`.

## Baseline Idea

Store parent pointers for every node, then walk ancestors upward. That works, but recursion can solve it directly without extra maps.

## Core Insight

If one target is found in the left subtree and the other in the right subtree, the current node is the LCA. Otherwise return whichever side found a target.

## Invariant / State

- `lowestCommonAncestor(node, p, q)` returns the LCA if found in this subtree, otherwise returns whichever target node is present in the subtree, or `None`.

## Walkthrough

For root `3` with targets `5` and `1`:
- One recursive branch finds `5`.
- The other finds `1`.
- Since both sides returned non-`None`, `3` is the LCA.

## Complexity

- Time: `O(n)`
- Space: `O(h)` recursion stack

## Edge Cases

- One target is an ancestor of the other
- Both targets lie in the same subtree
- Tree with only a few nodes

## Common Mistakes

- Using BST comparison logic on a general tree
- Forgetting that a target node can itself be the LCA
- Returning the current node too early before both subtrees are checked

## Pattern Transfer

- 235.Lowest Common Ancestor of a BST
- Postorder tree search
- Recursive “information bubbling up” problems

## Self-Check

- What does a non-`None` return from a subtree mean?
- Why can one of the target nodes itself be the answer?
- When does the current node become the LCA?

## Function

```python
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/236-lowest-common-ancestor-of-a-binary-tree/python -q
```
