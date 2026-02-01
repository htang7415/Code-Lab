from problem_707_design_linked_list import MyLinkedList


def test_design_linked_list_example():
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)
    assert linked_list.get(1) == 2
    linked_list.deleteAtIndex(1)
    assert linked_list.get(1) == 3


def test_design_linked_list_bounds():
    linked_list = MyLinkedList()
    assert linked_list.get(0) == -1
    linked_list.addAtIndex(1, 10)
    assert linked_list.get(0) == -1
    linked_list.addAtIndex(0, 5)
    assert linked_list.get(0) == 5
