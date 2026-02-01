from problem_19_remove_nth_node_from_end_of_list import ListNode, remove_nth_node_from_end


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_remove_nth_node_from_end_basic():
    head = build_list([1, 2, 3, 4, 5])
    result = remove_nth_node_from_end(head, 2)
    assert to_list(result) == [1, 2, 3, 5]


def test_remove_nth_node_from_end_single():
    head = build_list([1])
    result = remove_nth_node_from_end(head, 1)
    assert to_list(result) == []
