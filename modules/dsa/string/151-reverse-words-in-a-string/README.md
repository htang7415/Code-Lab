# 151.Reverse Words in a String

> Track: `dsa` | Topic: `string`

## Problem in One Line

Reverse the order of the words in a string while collapsing extra spaces.

## Recognition Cues

- The task is about words, not individual characters.
- Extra spaces must be removed in the final answer.
- Splitting on whitespace gives the exact word units to reorder.

## Baseline Idea

Scan the string manually, build each word character by character, then reconstruct the result. That works, but Python's string helpers make the intent much clearer here.

## Core Insight

`split()` already handles repeated spaces by extracting just the words. Once you have the word list, reverse it and join with single spaces.

## Invariant / State

- After `split()`, the list contains exactly the words in left-to-right order.
- `join()` always rebuilds the output with single spaces between words.

## Walkthrough

For `"  hello   world  "`:
- `split()` gives `["hello", "world"]`.
- Reverse the list to `["world", "hello"]`.
- Join to get `"world hello"`.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Edge Cases

- Leading and trailing spaces
- Multiple spaces between words
- A single word
- An input that is only spaces

## Common Mistakes

- Reversing characters instead of words
- Preserving extra spaces in the output
- Forgetting that the final spacing must be normalized

## Pattern Transfer

- Tokenize, transform, rebuild string problems
- String normalization tasks
- Word-based parsing

## Self-Check

- Why does `split()` solve the spacing issue directly?
- What should the result be for an input containing only spaces?
- Why is joining with `" "` important here?

## Function

```python
class Solution:
    def reverseWords(self, s: str) -> str:
```

## Run tests

```bash
pytest modules/dsa/string/151-reverse-words-in-a-string/python -q
```
