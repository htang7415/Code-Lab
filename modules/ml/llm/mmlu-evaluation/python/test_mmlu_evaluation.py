import pytest

from mmlu_evaluation import mmlu_accuracy


def test_mmlu_accuracy_normalizes_case_and_spaces():
    value = mmlu_accuracy([" a", "C ", "d"], ["A", "B", "D"])
    assert value == pytest.approx(2 / 3)


def test_mmlu_accuracy_perfect():
    assert mmlu_accuracy(["A", "B"], ["A", "B"]) == 1.0
