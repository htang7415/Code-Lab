# 332.Reconstruct Itinerary

> Track: `dsa` | Topic: `backtracking`

## Problem in One Line

Reconstruct the itinerary that uses every ticket exactly once and is lexicographically smallest.

## Recognition Cues

- Every ticket must be used exactly once.
- The route is an Eulerian-path style traversal over flights.
- Lexicographic order matters when multiple valid next stops exist.

## Baseline Idea

Try all ticket orderings with naive backtracking and keep the first valid lexicographically smallest route. That works in principle, but it explores far too many branches.

## Core Insight

Sort destinations in reverse lexicographic order and build the route with Hierholzer-style DFS, popping the smallest available destination last so the reversed route is lexicographically smallest.

## Invariant / State

- `graph[src]` stores the unused outgoing destinations from `src`.
- `visit(airport)` consumes all outgoing edges from that airport before appending it to the route.

## Walkthrough

For tickets `JFK -> MUC -> LHR -> SFO -> SJC`:
- Start at `JFK`.
- Follow and consume outgoing edges until no flight remains.
- Append airports on the way back and reverse the collected route.

## Complexity

- Time: `O(E log E)` due to sorting tickets
- Space: `O(E)` for the graph and route

## Edge Cases

- Only one ticket
- A cycle in the route
- Multiple lexicographically valid next airports

## Common Mistakes

- Using greedy local choice without Eulerian traversal logic
- Forgetting to reverse the route at the end
- Sorting in the wrong direction before popping

## Pattern Transfer

- Eulerian path reconstruction
- Postorder route building
- Graph traversal with lexicographic tie-breaking

## Self-Check

- Why is the route built in reverse?
- Why are destinations sorted in reverse before popping?
- What does it mean that every ticket is an edge used exactly once?

## Function

```python
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
```

## Run tests

```bash
pytest modules/dsa/backtracking/332-reconstruct-itinerary/python -q
```
