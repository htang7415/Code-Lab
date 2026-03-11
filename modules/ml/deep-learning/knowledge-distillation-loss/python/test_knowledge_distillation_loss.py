import math

import pytest

from knowledge_distillation_loss import distill_loss


def test_distill_loss_is_zero_for_matching_logits() -> None:
    loss = distill_loss([2.0, 0.0], [2.0, 0.0], temp=1.0)
    assert loss < 1e-6


def test_distill_loss_matches_teacher_to_student_kl() -> None:
    student = [2.0, 1.0, 0.0]
    teacher = [0.0, 2.0, 1.0]

    student_probs = [math.exp(value) for value in student]
    student_total = sum(student_probs)
    student_probs = [value / student_total for value in student_probs]

    teacher_probs = [math.exp(value) for value in teacher]
    teacher_total = sum(teacher_probs)
    teacher_probs = [value / teacher_total for value in teacher_probs]

    expected = sum(
        p_t * math.log(p_t / p_s)
        for p_s, p_t in zip(student_probs, teacher_probs)
    )
    assert distill_loss(student, teacher, temp=1.0) == pytest.approx(expected)


def test_distill_loss_validates_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        distill_loss([1.0], [1.0, 2.0])

    with pytest.raises(ValueError, match="positive"):
        distill_loss([1.0], [1.0], temp=0.0)
