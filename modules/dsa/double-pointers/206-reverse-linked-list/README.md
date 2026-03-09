# 206.Reverse Linked List

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Reverse a singly linked list in place and return the new head.

## Recognition Cues

- The list direction must be flipped, not copied.
- Each node's `next` pointer needs to be rewired exactly once.
- A moving `prev` and `current` pair is the natural iterative state.

## Baseline Idea

Copy the node values into an array and rebuild the list in reverse order. That works, but it uses extra memory and avoids the actual pointer exercise.

## Core Insight

Walk through the list once while keeping track of the previous node. For each node, save its original `next`, reverse the link to `prev`, then advance both pointers.

## Invariant / State

- `prev` always points to the already reversed prefix.
- `current` always points to the first node not yet reversed.

## Walkthrough

For `1 -> 2 -> 3`:
- Start with `prev = None`, `current = 1`.
- Reverse `1.next` to `None`.
- Reverse `2.next` to `1`.
- Reverse `3.next` to `2`.
- `prev` ends at `3`, which becomes the new head.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty list
- One node
- Two nodes

## Common Mistakes

- Losing the rest of the list by overwriting `next` too early
- Returning the old head instead of `prev`
- Forgetting that the original head becomes the new tail

## Pattern Transfer

- Linked-list pointer rewiring
- 24.Swap Nodes in Pairs
- Reverse a sublist between two positions

## Self-Check

- Why must the next node be saved before reversing the link?
- What do `prev` and `current` represent after each step?
- Which node becomes the new head at the end?

## Function

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/206-reverse-linked-list/python -q
```
