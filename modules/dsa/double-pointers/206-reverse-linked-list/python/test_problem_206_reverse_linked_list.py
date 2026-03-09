from problem_206_reverse_linked_list import ListNode, Solution


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


def test_reverse_list_example():
    head = build_list([1, 2, 3, 4, 5])
    result = Solution().reverseList(head)
    assert to_list(result) == [5, 4, 3, 2, 1]


def test_reverse_list_edge_empty():
    assert Solution().reverseList(None) is None


def test_reverse_list_tricky_two_nodes():
    head = build_list([1, 2])
    result = Solution().reverseList(head)
    assert to_list(result) == [2, 1]
