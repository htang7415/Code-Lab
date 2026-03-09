from collections import defaultdict


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    pair_sums: dict[int, list[tuple[int, int]]] = defaultdict(list)
    result: set[tuple[int, int, int, int]] = set()
    n = len(nums)

    for right_start in range(1, n):
        for end in range(right_start + 1, n):
            complement = target - nums[right_start] - nums[end]
            for first, second in pair_sums.get(complement, []):
                result.add(
                    tuple(sorted((nums[first], nums[second], nums[right_start], nums[end])))
                )
        for left in range(right_start):
            pair_sums[nums[left] + nums[right_start]].append((left, right_start))

    return [list(quadruplet) for quadruplet in sorted(result)]
