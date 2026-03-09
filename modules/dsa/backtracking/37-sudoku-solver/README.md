# 37.Sudoku Solver

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Fill the Sudoku grid so every row, column, and `3 x 3` box is valid.

## Recognition Cues

- This is a constraint-satisfaction problem on a fixed grid.
- Empty cells must be filled from a small candidate set.
- Early pruning is essential because brute force is enormous.

## Baseline Idea

For every empty cell, try all digits and check the whole board each time. That is correct but wastes work on repeated validity checks.

## Core Insight

Track used digits for each row, column, and box in sets, then backtrack only over empty cells while checking those sets in `O(1)`.

## Invariant / State

- `rows[r]`, `cols[c]`, and `boxes[b]` store the digits already used in that row, column, or box.
- `empties[index]` is the next cell to fill.

## Walkthrough

For an empty cell `(r, c)`:
- Compute its box index.
- Try digits `1..9` that are absent from the row, column, and box sets.
- Place one digit, recurse, then undo the choice if the branch fails.

## Complexity

- Time: exponential in the number of empty cells, heavily pruned
- Space: `O(number of empty cells)` recursion depth plus constraint sets

## Edge Cases

- Nearly solved board
- Multiple forced cells in a row
- Boards where many choices are invalid immediately

## Common Mistakes

- Forgetting to undo a digit in all three constraint sets
- Computing the wrong box index
- Advancing without writing the digit to the board

## Pattern Transfer

- N-Queens
- Constraint backtracking with auxiliary sets
- Exact-cover style search

## Self-Check

- What information do the three constraint collections store?
- Why is undoing state critical here?
- How is this different from naive board-wide validation?

## Function

```python
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
```

## Run tests

```bash
pytest modules/dsa/backtracking/37-sudoku-solver/python -q
```
