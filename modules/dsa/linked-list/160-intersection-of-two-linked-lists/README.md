# 160.Intersection Of Two Linked Lists

> Track: `dsa` | Topic: `linked-list`

## Problem in One Line

Return the first shared node of two linked lists, or `None` if they never meet.

## Recognition Cues

- Two singly linked lists may merge into one shared tail.
- The answer depends on node identity, not node value.
- Pointer switching equalizes different list lengths without extra space.

## Baseline Idea

Store all nodes from one list in a set and scan the other list until you find a repeated node. That works, but it costs extra memory.

## Core Insight

Let one pointer walk list A then switch to list B, and let the other pointer walk list B then switch to list A. Each pointer travels the same total distance, so they line up at the intersection or both end at `None`.

## Invariant / State

- Each pointer walks exactly `len(A) + len(B)` nodes.
- Any initial path-length difference is canceled after the switch.

## Walkthrough

For lists `4 -> 1 -> 8 -> 4 -> 5` and `5 -> 6 -> 1 -> 8 -> 4 -> 5`:
- Start one pointer on each head.
- When a pointer reaches the end, move it to the other list's head.
- They first match at the shared node `8`.

## Complexity

- Time: `O(m + n)`
- Space: `O(1)`

## Edge Cases

- No intersection
- Both heads already point to the same list
- One list is empty

## Common Mistakes

- Comparing node values instead of node objects
- Resetting each pointer to its own head instead of the other head
- Stopping before both pointers have finished switching

## Pattern Transfer

- Pointer switching to equalize path length
- Shared-tail linked-list problems
- 142.Linked List Cycle II for pointer meeting reasoning

## Self-Check

- Why do both pointers travel the same total distance?
- Why must intersection be checked by identity?
- What do both pointers become if the lists do not intersect?

## Function

```python
def get_intersection_node(head_a: ListNode | None, head_b: ListNode | None) -> ListNode | None:
```

## Run tests

```bash
pytest modules/dsa/linked-list/160-intersection-of-two-linked-lists/python -q
```
