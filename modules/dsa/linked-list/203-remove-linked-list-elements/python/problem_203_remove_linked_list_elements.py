from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def remove_linked_list_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev = dummy
    current = head
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return dummy.next
