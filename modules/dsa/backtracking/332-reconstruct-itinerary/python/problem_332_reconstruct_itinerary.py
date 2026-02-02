from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph: dict[str, list[str]] = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        route: list[str] = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]
