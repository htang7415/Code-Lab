from linked_list_summary import ListNode, linked_list_summary


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def test_linked_list_summary_basic():
    head = build_list([1, 2, 3])
    assert linked_list_summary(head) == {
        "length": 3,
        "head": 1,
        "tail": 3,
        "has_cycle": False,
    }


def test_linked_list_summary_cycle():
    nodes = [ListNode(1), ListNode(2), ListNode(3)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[1]
    assert linked_list_summary(nodes[0]) == {
        "length": None,
        "head": 1,
        "tail": None,
        "has_cycle": True,
    }
