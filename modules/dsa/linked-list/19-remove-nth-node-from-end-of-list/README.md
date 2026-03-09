# 19.Remove Nth Node From End Of List

> Track: `dsa` | Topic: `linked-list`

## Problem in One Line

Delete the `n`th node from the end of a linked list and return the new head.

## Recognition Cues

- The target is counted from the tail, not the head.
- One pass is possible with a fixed gap between two pointers.
- A dummy node simplifies deletion when the head must be removed.

## Baseline Idea

First compute the list length, then convert the position from the end into a position from the front and delete it on a second pass. This works, but it needs two scans.

## Core Insight

Advance the fast pointer `n` steps first, then move fast and slow together until fast reaches the last node. At that point, `slow.next` is the node to delete.

## Invariant / State

- Fast stays `n` nodes ahead of slow after the initial setup.
- When fast reaches the tail, slow is right before the target node.

## Walkthrough

For `1 -> 2 -> 3 -> 4 -> 5` and `n = 2`:
- Move fast two steps ahead.
- Move fast and slow together until fast reaches `5`.
- Slow stops at `3`, so remove `4`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Single-node list
- Removing the head
- Removing the tail

## Common Mistakes

- Forgetting the dummy node for head deletion
- Moving fast the wrong number of steps
- Rewiring the wrong `next` pointer

## Pattern Transfer

- Fixed-gap two-pointer linked-list problems
- 876.Middle of the Linked List
- One-pass linked-list deletion

## Self-Check

- Why does a dummy node simplify removing the head?
- What does the fast/slow gap represent?
- Which node should slow point to when deletion happens?

## Function

```python
def remove_nth_node_from_end(head: ListNode | None, n: int) -> ListNode | None:
```

## Run tests

```bash
pytest modules/dsa/linked-list/19-remove-nth-node-from-end-of-list/python -q
```
