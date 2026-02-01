from problem_160_intersection_of_two_linked_lists import ListNode, get_intersection_node


def build_list(values: list[int]) -> tuple[ListNode | None, ListNode | None]:
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next, current if dummy.next else None


def test_get_intersection_node_found():
    common_head, _ = build_list([8, 4, 5])
    head_a, tail_a = build_list([4, 1])
    head_b, tail_b = build_list([5, 6, 1])
    if tail_a:
        tail_a.next = common_head
    if tail_b:
        tail_b.next = common_head
    assert get_intersection_node(head_a, head_b) is common_head


def test_get_intersection_node_none():
    head_a, _ = build_list([1, 2, 3])
    head_b, _ = build_list([4, 5])
    assert get_intersection_node(head_a, head_b) is None
