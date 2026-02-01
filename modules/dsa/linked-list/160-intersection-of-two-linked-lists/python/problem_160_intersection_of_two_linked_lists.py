from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def get_intersection_node(
    head_a: Optional[ListNode],
    head_b: Optional[ListNode],
) -> Optional[ListNode]:
    pointer_a = head_a
    pointer_b = head_b
    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next if pointer_a else head_b
        pointer_b = pointer_b.next if pointer_b else head_a
    return pointer_a
