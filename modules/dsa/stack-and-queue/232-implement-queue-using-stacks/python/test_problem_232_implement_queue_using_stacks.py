from problem_232_implement_queue_using_stacks import MyQueue


def test_queue_basic():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() is False
    assert queue.pop() == 2
    assert queue.empty() is True
