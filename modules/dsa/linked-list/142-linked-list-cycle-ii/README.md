# 142.Linked List Cycle II

> Track: `dsa` | Topic: `linked-list`

## Problem in One Line

Return the node where a linked-list cycle begins, or `None` if no cycle exists.

## Recognition Cues

- The input is a linked list with possible cycles.
- You need the cycle entry, not just cycle existence.
- Constant extra space suggests Floyd's two-pointer method.

## Baseline Idea

Store visited nodes in a set and stop when you see one twice. That works, but it uses extra memory.

## Core Insight

Use slow and fast pointers to detect a meeting point inside the cycle. Then reset one pointer to `head` and move both one step at a time; they meet again at the cycle entry.

## Invariant / State

- If a cycle exists, slow and fast eventually meet inside it.
- After the first meeting, the distance from `head` to the entry equals the distance from the meeting point to the entry.

## Walkthrough

For `3 -> 2 -> 0 -> -4` with the tail linking back to `2`:
- Slow and fast meet somewhere inside the cycle.
- Reset one pointer to `head`.
- Move both one step at a time.
- They meet at node `2`, which is the entry.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty list
- One node with no cycle
- One node pointing to itself
- Cycle begins at the head

## Common Mistakes

- Returning the first meeting point instead of the entry
- Forgetting the no-cycle case
- Comparing values instead of node identity

## Pattern Transfer

- Floyd's cycle detection
- 141.Linked List Cycle
- Pointer distance arguments on linked lists

## Self-Check

- Why is the first meeting point not necessarily the cycle entry?
- Why do the reset pointer and meeting pointer meet at the entry?
- What should be returned when no cycle exists?

## Function

```python
def detect_cycle(head: ListNode | None) -> ListNode | None:
```

## Run tests

```bash
pytest modules/dsa/linked-list/142-linked-list-cycle-ii/python -q
```
