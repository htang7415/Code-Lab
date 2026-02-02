from problem_332_reconstruct_itinerary import Solution


def test_itinerary_basic():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert Solution().findItinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]


def test_itinerary_lex_order():
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    assert Solution().findItinerary(tickets) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
