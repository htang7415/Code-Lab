# 450.Delete Node in a BST

> Track: `dsa` | Topic: `binary-tree`

## Problem in One Line

Delete the node with key `key` from the BST and return the new root.

## Recognition Cues

- BST ordering should guide the search for the node to delete.
- Deletion splits into cases based on the number of children.
- The two-child case needs an inorder predecessor or successor replacement.

## Baseline Idea

Rebuild the BST from all values except the deleted one. That works, but it discards the tree structure and wastes work.

## Core Insight

Search recursively using BST ordering. When the target is found:
- if it has 0 or 1 child, return that child directly
- if it has 2 children, replace its value with the inorder successor and delete that successor from the right subtree

## Invariant / State

- `deleteNode(root, key)` returns the correct BST root after deletion in that subtree.

## Walkthrough

For deleting `5` from `[5,3,6,2,4,None,7]`:
- Find the node `5`.
- Its inorder successor is `6`.
- Replace `5` with `6`, then delete the old `6` node from the right subtree.

## Complexity

- Time: `O(h)` average on a balanced BST
- Space: `O(h)` recursion stack

## Edge Cases

- Key not present
- Deleting a leaf
- Deleting the root
- Deleting a node with two children

## Common Mistakes

- Forgetting to delete the successor after copying its value
- Violating BST ordering during reconnection
- Mishandling the one-child cases

## Pattern Transfer

- BST insert/search/delete
- 700.Search in a Binary Search Tree
- Structural BST updates

## Self-Check

- Why is the inorder successor a valid replacement?
- What happens in the one-child case?
- What must the recursive call return after deletion?

## Function

```python
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
```

## Run tests

```bash
pytest modules/dsa/binary-tree/450-delete-node-in-a-bst/python -q
```
