# 19.Remove Nth Node From End of List

> Track: `dsa` | Topic: `double-pointers`

## Concept

Use two pointers separated by n nodes so the slow pointer stops before the removal.

## Function

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
```
