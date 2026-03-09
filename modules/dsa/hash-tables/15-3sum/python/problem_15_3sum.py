def three_sum(nums: list[int]) -> list[list[int]]:
    result: set[tuple[int, int, int]] = set()

    for i, first in enumerate(nums):
        seen: set[int] = set()
        for second in nums[i + 1 :]:
            third = -first - second
            if third in seen:
                result.add(tuple(sorted((first, second, third))))
            seen.add(second)

    return [list(triplet) for triplet in sorted(result)]
