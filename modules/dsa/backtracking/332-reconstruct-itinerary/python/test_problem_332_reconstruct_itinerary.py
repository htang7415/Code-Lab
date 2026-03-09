from problem_332_reconstruct_itinerary import Solution


def test_itinerary_example():
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert Solution().findItinerary(tickets) == ["JFK", "MUC", "LHR", "SFO", "SJC"]


def test_itinerary_edge_single_ticket():
    assert Solution().findItinerary([["JFK", "SFO"]]) == ["JFK", "SFO"]


def test_itinerary_tricky_lex_order():
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    assert Solution().findItinerary(tickets) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
