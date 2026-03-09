# 1047.Remove All Adjacent Duplicates in String

> Track: `dsa` | Topic: `stack-and-queue`

## Problem in One Line

Repeatedly remove adjacent equal characters until no such pair remains.

## Recognition Cues

- Removing one pair can create a new removable pair next to it.
- You need the final stabilized string after repeated cancellations.
- A stack naturally tracks the current unmatched prefix.

## Baseline Idea

Scan the string repeatedly and delete adjacent pairs until nothing changes. That works, but it rescans too much.

## Core Insight

Process characters once with a stack. If the current character matches the stack top, pop it to simulate removing the pair; otherwise push it.

## Invariant / State

- The stack always represents the fully reduced form of the processed prefix.
- No adjacent duplicate pair remains inside the stack.

## Walkthrough

For `"abbaca"`:
- Push `a`, then `b`.
- The next `b` matches the top, so pop.
- Push `a`, then the next `a` matches the top, so pop.
- Push `c`, then `a`.
- The final reduced string is `"ca"`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- Empty string
- No adjacent duplicates
- Cascading removals like `"azxxzy"`

## Common Mistakes

- Removing only one pass of duplicates instead of the fully reduced result
- Appending before checking the top
- Forgetting to rebuild the answer from the stack

## Pattern Transfer

- Parentheses matching with a stack
- Adjacent cancellation problems
- Streaming reduction over a sequence

## Self-Check

- Why can one stack pass simulate repeated removals?
- What does the stack represent after each processed character?
- Why can a new removable pair appear only at the top?

## Function

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
```

## Run tests

```bash
pytest modules/dsa/stack-and-queue/1047-remove-all-adjacent-duplicates-in-string/python -q
```
