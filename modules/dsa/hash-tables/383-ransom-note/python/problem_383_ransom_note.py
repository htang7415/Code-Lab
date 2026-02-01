def can_construct(ransom_note: str, magazine: str) -> bool:
    counts: dict[str, int] = {}
    for ch in magazine:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in ransom_note:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True
