import pytest

from warmup_cosine_decay import warmup_cosine_lr


def test_warmup_cosine_lr_warms_up_linearly() -> None:
    assert warmup_cosine_lr(1.0, step=2, warmup_steps=4, total_steps=10) == pytest.approx(0.5)


def test_warmup_cosine_lr_switches_to_cosine_after_warmup() -> None:
    assert warmup_cosine_lr(1.0, step=7, warmup_steps=4, total_steps=10) == pytest.approx(0.5)


def test_warmup_cosine_lr_reaches_zero_at_end() -> None:
    assert warmup_cosine_lr(1.0, step=10, warmup_steps=4, total_steps=10) == pytest.approx(0.0)
