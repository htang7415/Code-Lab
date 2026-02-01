def four_sum_count(
    nums1: list[int],
    nums2: list[int],
    nums3: list[int],
    nums4: list[int],
) -> int:
    counts: dict[int, int] = {}
    for a in nums1:
        for b in nums2:
            counts[a + b] = counts.get(a + b, 0) + 1
    total = 0
    for c in nums3:
        for d in nums4:
            total += counts.get(-(c + d), 0)
    return total
