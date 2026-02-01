from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def linked_list_basics(values: list[int]) -> dict[str, int | None]:
    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None
    length = 0
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
        length += 1
    return {
        "length": length,
        "head": head.val if head else None,
        "tail": tail.val if tail else None,
    }
