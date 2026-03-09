from problem_19_remove_nth_node_from_end_of_list import ListNode, Solution


def build_list(values: list[int]) -> ListNode | None:
    head = None
    current = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head


def to_list(head: ListNode | None) -> list[int]:
    out = []
    current = head
    while current:
        out.append(current.val)
        current = current.next
    return out


def test_remove_nth_example():
    head = build_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 2)
    assert to_list(result) == [1, 2, 3, 5]


def test_remove_nth_edge_single_node():
    head = build_list([1])
    result = Solution().removeNthFromEnd(head, 1)
    assert to_list(result) == []


def test_remove_nth_tricky_remove_head():
    head = build_list([1, 2, 3])
    result = Solution().removeNthFromEnd(head, 3)
    assert to_list(result) == [2, 3]
