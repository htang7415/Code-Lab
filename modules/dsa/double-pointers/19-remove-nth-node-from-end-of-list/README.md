# 19.Remove Nth Node From End of List

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Delete the `n`th node from the end of a linked list and return the new head.

## Recognition Cues

- The target position is counted from the end, not the front.
- You want one pass instead of computing the length first.
- A fixed gap between two pointers lets one pointer stop just before the node to delete.

## Baseline Idea

Walk the list once to get its length, compute the front index to remove, then walk again and delete that node. This works, but it needs two passes.

## Core Insight

Start both pointers at a dummy node, move the fast pointer `n + 1` steps ahead, then move both together. When the fast pointer reaches the end, the slow pointer is right before the node to remove.

## Invariant / State

- The gap between `fast` and `slow` stays at `n + 1` nodes.
- When `fast` is `None`, `slow.next` is the node to delete.

## Walkthrough

For `1 -> 2 -> 3 -> 4 -> 5` and `n = 2`:
- Advance `fast` three steps ahead from the dummy node.
- Move `fast` and `slow` together until `fast` hits the end.
- `slow` stops at `3`, so remove `slow.next`, which is `4`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Single-node list
- Removing the head
- Removing the tail

## Common Mistakes

- Forgetting the dummy node when the head might be removed
- Advancing `fast` only `n` steps instead of `n + 1`
- Rewiring the wrong `next` pointer

## Pattern Transfer

- Fixed-gap two-pointer linked-list problems
- 876.Middle of the Linked List
- 19-style one-pass deletion logic

## Self-Check

- Why does the dummy node simplify head deletion?
- Why must the gap be `n + 1` instead of `n` here?
- Which node should `slow` point to when deletion happens?

## Function

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/19-remove-nth-node-from-end-of-list/python -q
```
