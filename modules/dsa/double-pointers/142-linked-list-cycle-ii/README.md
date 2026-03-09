# 142.Linked List Cycle II

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Return the node where a linked-list cycle begins, or `None` if there is no cycle.

## Recognition Cues

- The input is a linked list with possible cycles.
- You need cycle existence and cycle entry, not just one or the other.
- `O(1)` extra space points to Floyd's two-pointer method.

## Baseline Idea

Store visited nodes in a set and return the first node you revisit. That is easy to reason about, but it uses extra memory.

## Core Insight

Use a slow pointer and a fast pointer to detect whether a cycle exists. Once they meet inside the cycle, start one pointer at `head` and keep the other at the meeting point; moving both one step at a time makes them meet again at the cycle entry.

## Invariant / State

- If a cycle exists, slow and fast eventually meet inside it.
- After the first meeting, the distance from `head` to the entry equals the distance from the meeting point to the entry along the cycle.

## Walkthrough

For `3 -> 2 -> 0 -> -4` with the tail pointing back to `2`:
- Slow and fast eventually meet inside the cycle.
- Reset one pointer to `head`.
- Move both pointers one step at a time.
- They meet at the node with value `2`, which is the entry.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty list
- One node with no cycle
- One node pointing to itself
- Cycle starts at the head

## Common Mistakes

- Returning the first meeting point instead of the cycle entry
- Advancing the pointers incorrectly after the first meeting
- Forgetting to handle the no-cycle case

## Pattern Transfer

- Floyd's cycle detection
- 141.Linked List Cycle
- Pointer distance reasoning on linked lists

## Self-Check

- Why is the first meeting point not always the cycle entry?
- Why do the reset pointer and meeting pointer meet at the entry?
- What happens if there is no cycle?

## Function

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/142-linked-list-cycle-ii/python -q
```
