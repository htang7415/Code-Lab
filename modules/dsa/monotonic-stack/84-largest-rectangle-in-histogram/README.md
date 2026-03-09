# 84.Largest Rectangle in Histogram

> Track: `dsa` | Topic: `monotonic-stack`

## Problem in One Line

Find the largest rectangle area that can be formed in a histogram.

## Recognition Cues

- Every bar could be the limiting height of the best rectangle.
- You need the widest span where a bar stays the minimum height.
- A monotonic stack can find boundaries when a shorter bar appears.

## Baseline Idea

For each bar, expand left and right until you hit a shorter bar, then compute the rectangle area. This works, but doing that from every bar repeats too much work.

## Core Insight

Keep indices in an increasing stack. When a shorter bar appears, it tells you that the popped bar can no longer extend further right, so its maximal rectangle is determined immediately.

## Invariant / State

- The stack stores indices of bars in increasing height order.
- Bars left in the stack have not yet found their first shorter bar on the right.

## Walkthrough

For `[2, 1, 5, 6, 2, 3]`:
- Push increasing bars until `2` arrives after `6`.
- Pop `6`, then `5`, because `2` is the first shorter bar to the right for both.
- Use the new stack top as the left boundary and the current index as the right boundary.
- Track the largest area seen during these pops.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- One bar
- Strictly increasing heights
- Strictly decreasing heights
- Repeated heights

## Common Mistakes

- Forgetting the sentinel flush at the end
- Using bar values instead of indices in the stack
- Miscomputing the width after a pop

## Pattern Transfer

- Monotonic stack with left and right boundaries
- 42.Trapping Rain Water
- Largest span under a constraint

## Self-Check

- Why does a shorter incoming bar finalize rectangles for taller bars?
- What do the current index and new stack top mean after a pop?
- Why is an extra trailing `0` useful?

## Function

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
```

## Run tests

```bash
pytest modules/dsa/monotonic-stack/84-largest-rectangle-in-histogram/python -q
```
