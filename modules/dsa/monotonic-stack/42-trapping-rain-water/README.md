# 42.Trapping Rain Water

> Track: `dsa` | Topic: `monotonic-stack`

## Problem in One Line

Compute how much rainwater is trapped between elevation bars after raining.

## Recognition Cues

- Water above a bar depends on a left boundary and a right boundary.
- A new taller bar can close a valley and determine trapped water.
- A monotonic stack can keep unresolved boundaries in order.

## Baseline Idea

For each bar, search left and right for the highest boundaries and compute the water above it. That works, but repeated scanning is expensive.

## Core Insight

Use a decreasing stack of bar indices. When a new bar is taller than the stack top, it closes a basin. The popped bar becomes the basin bottom, the new stack top is the left wall, and the current bar is the right wall.

## Invariant / State

- The stack stores indices of bars in non-increasing height order.
- Any bar still in the stack has not yet found a right boundary tall enough to resolve its trapped water.

## Walkthrough

For `[0, 1, 0, 2]`:
- Push `0`, then `1`.
- When `2` arrives, pop the `0` bar as the basin bottom.
- The left wall is `1`, the right wall is `2`, so one unit of water is trapped above the bottom.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- Empty input
- Monotonic increasing heights
- Monotonic decreasing heights
- Deep nested valleys

## Common Mistakes

- Forgetting that the stack stores indices, not heights
- Computing water when there is no left wall after popping
- Using the wrong width between boundaries

## Pattern Transfer

- Monotonic stack for unresolved boundaries
- 84.Largest Rectangle in Histogram
- Nearest greater element reasoning

## Self-Check

- Why does popping reveal a trapped basin?
- What does the bar left on top of the stack represent after a pop?
- Why is the bounded height `min(left_wall, right_wall) - bottom_height`?

## Function

```python
class Solution:
    def trap(self, height: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/monotonic-stack/42-trapping-rain-water/python -q
```
