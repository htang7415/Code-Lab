from __future__ import annotations

import re
import string


def _normalize_answer(text: str) -> str:
    text = text.lower()
    text = "".join(character for character in text if character not in string.punctuation)
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def minority_cluster_count(answers: list[str]) -> int:
    if not answers:
        return 0

    normalized_answers = {_normalize_answer(answer) for answer in answers}
    return max(0, len(normalized_answers) - 1)
