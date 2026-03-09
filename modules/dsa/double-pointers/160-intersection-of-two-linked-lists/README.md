# 160.Intersection of Two Linked Lists

> Track: `dsa` | Topic: `double-pointers`

## Problem in One Line

Return the first shared node of two singly linked lists, or `None` if they do not intersect.

## Recognition Cues

- Two linked lists may merge into a shared tail.
- The answer depends on node identity, not node value.
- Pointer switching can equalize different path lengths without extra space.

## Baseline Idea

Store all nodes from one list in a set, then walk the other list until you find a repeated node. That works, but it uses extra memory.

## Core Insight

Let one pointer walk list A then switch to list B, and let the other walk list B then switch to list A. After both have traveled the same total distance, they either meet at the intersection node or both reach `None`.

## Invariant / State

- Each pointer walks exactly `len(A) + len(B)` nodes.
- After switching heads, the path-length difference is canceled out.

## Walkthrough

If list A is `4 -> 1 -> 8 -> 4 -> 5` and list B is `5 -> 6 -> 1 -> 8 -> 4 -> 5`:
- Pointer A starts on A and pointer B starts on B.
- After each reaches the end, it jumps to the other list's head.
- The first node where they match by identity is the shared node `8`.

## Complexity

- Time: `O(m + n)`
- Space: `O(1)`

## Edge Cases

- No intersection
- Both heads already point to the same list
- One list is empty

## Common Mistakes

- Comparing node values instead of node objects
- Resetting pointers to their own heads instead of the other list's head
- Stopping too early before both pointers finish the switch

## Pattern Transfer

- Pointer switching to equalize path length
- 142.Linked List Cycle II for pointer meeting logic
- Shared-tail linked-list problems

## Self-Check

- Why do both pointers walk the same total distance?
- Why must the comparison use node identity?
- What do both pointers become if there is no intersection?

## Function

```python
class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
```

## Run tests

```bash
pytest modules/dsa/double-pointers/160-intersection-of-two-linked-lists/python -q
```
