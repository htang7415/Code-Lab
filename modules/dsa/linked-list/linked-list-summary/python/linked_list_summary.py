from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def linked_list_summary(head: Optional[ListNode]) -> dict[str, int | bool | None]:
    if head is None:
        return {
            "length": 0,
            "head": None,
            "tail": None,
            "has_cycle": False,
        }

    if _has_cycle(head):
        return {
            "length": None,
            "head": head.val,
            "tail": None,
            "has_cycle": True,
        }

    length = 0
    tail = head
    current = head
    while current:
        length += 1
        tail = current
        current = current.next

    return {
        "length": length,
        "head": head.val,
        "tail": tail.val,
        "has_cycle": False,
    }


def _has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
