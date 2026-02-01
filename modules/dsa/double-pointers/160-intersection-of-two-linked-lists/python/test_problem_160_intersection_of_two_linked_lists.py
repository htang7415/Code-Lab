from problem_160_intersection_of_two_linked_lists import ListNode, Solution


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


def tail(node: ListNode) -> ListNode:
    current = node
    while current.next:
        current = current.next
    return current


def test_intersection_found():
    common = build_list([8, 4, 5])
    headA = build_list([4, 1])
    headB = build_list([5, 6, 1])
    tail(headA).next = common
    tail(headB).next = common
    result = Solution().getIntersectionNode(headA, headB)
    assert result is common


def test_intersection_none():
    headA = build_list([2, 6, 4])
    headB = build_list([1, 5])
    result = Solution().getIntersectionNode(headA, headB)
    assert result is None
