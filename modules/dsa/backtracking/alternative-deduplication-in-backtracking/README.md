# Alternative Deduplication in Backtracking

> Track: `dsa` | Topic: `backtracking`

## Concept

Use a local set at each depth to skip duplicate choices.

## Function

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
```
