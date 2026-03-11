import math


def _softmax(logits: list[float], temp: float) -> list[float]:
    if not logits:
        raise ValueError("logits must be non-empty")
    if temp <= 0.0:
        raise ValueError("temp must be positive")

    m = max(logits)
    exps = [math.exp((x - m) / temp) for x in logits]
    s = sum(exps)
    return [e / s for e in exps]


def distill_loss(student: list[float], teacher: list[float], temp: float = 1.0) -> float:
    if len(student) != len(teacher):
        raise ValueError("student and teacher must have the same length")

    ps = _softmax(student, temp)
    pt = _softmax(teacher, temp)
    loss = 0.0
    for p_s, p_t in zip(ps, pt):
        if p_t > 0 and p_s > 0:
            loss += p_t * math.log(p_t / p_s)
    return loss
