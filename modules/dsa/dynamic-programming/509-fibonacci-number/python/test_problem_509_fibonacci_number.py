from problem_509_fibonacci_number import Solution


def test_fibonacci_basic():
    assert Solution().fib(2) == 1


def test_fibonacci_four():
    assert Solution().fib(4) == 3
