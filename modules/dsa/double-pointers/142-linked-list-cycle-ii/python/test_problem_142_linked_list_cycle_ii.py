from problem_142_linked_list_cycle_ii import ListNode, Solution


def build_cycle(values: list[int], pos: int) -> ListNode | None:
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def test_detect_cycle_entry():
    head = build_cycle([3, 2, 0, -4], 1)
    entry = Solution().detectCycle(head)
    assert entry is not None
    assert entry.val == 2


def test_detect_cycle_none():
    head = build_cycle([1, 2, 3], -1)
    assert Solution().detectCycle(head) is None
