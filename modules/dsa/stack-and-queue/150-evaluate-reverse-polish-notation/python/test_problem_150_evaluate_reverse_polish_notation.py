from problem_150_evaluate_reverse_polish_notation import Solution


def test_eval_rpn_basic():
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9


def test_eval_rpn_division():
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
