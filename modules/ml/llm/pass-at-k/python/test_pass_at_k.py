import pytest

from pass_at_k import pass_at_k


def test_pass_at_k_known_value():
    assert pass_at_k(total_samples=5, correct_samples=2, k=2) == pytest.approx(0.7)


def test_pass_at_k_zero_and_one_cases():
    assert pass_at_k(total_samples=4, correct_samples=0, k=1) == 0.0
    assert pass_at_k(total_samples=4, correct_samples=3, k=2) == 1.0
