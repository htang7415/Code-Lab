from problem_142_linked_list_cycle_ii import ListNode, detect_cycle


def test_detect_cycle_found():
    nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = nodes[1]
    head = nodes[0]
    assert detect_cycle(head) is nodes[1]


def test_detect_cycle_none():
    head = ListNode(1, ListNode(2))
    assert detect_cycle(head) is None
