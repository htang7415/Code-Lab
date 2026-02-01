def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for idx, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], idx]
        seen[value] = idx
    raise ValueError("No solution")
