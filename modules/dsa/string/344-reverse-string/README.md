# 344.Reverse String

> Track: `dsa` | Topic: `string`

## Problem in One Line

Reverse the character array in place.

## Recognition Cues

- The input is mutable, so the change must happen in place.
- Only symmetric swaps are needed.
- A left pointer and a right pointer fit the problem exactly.

## Baseline Idea

Create a reversed copy of the array and assign it back. That works, but it uses extra space and avoids the in-place requirement.

## Core Insight

Swap the leftmost and rightmost characters, then move both pointers inward. Each swap places two characters into their final positions.

## Invariant / State

- Characters outside `[left, right]` are already in their final reversed positions.
- Only the middle segment still needs work.

## Walkthrough

For `["h", "e", "l", "l", "o"]`:
- Swap `"h"` and `"o"`.
- Swap `"e"` and `"l"`.
- Stop when the pointers cross.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Edge Cases

- Empty array
- One character
- Even-length and odd-length arrays

## Common Mistakes

- Returning a new array instead of modifying in place
- Moving only one pointer after a swap
- Stopping too early before the pointers cross

## Pattern Transfer

- Two-pointer array reversal
- Reverse part of an array or string
- Symmetric swap problems

## Self-Check

- Why does each swap place two characters correctly?
- What part of the array is guaranteed done after each step?
- When should the loop stop?

## Function

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
```

## Run tests

```bash
pytest modules/dsa/string/344-reverse-string/python -q
```
