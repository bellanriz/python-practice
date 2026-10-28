"""
LeetCode 332 - Reconstruct Itinerary

Given a list of airline tickets [from, to], reconstruct the itinerary
starting from "JFK". If multiple valid itineraries exist, return the
one with the smallest lexical order.

You must use all tickets exactly once.

Example 1:
    Input:  tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
    Input:  tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Constraints:
    - 1 <= len(tickets) <= 300

Hint: This is an Eulerian path problem. Use Hierholzer's algorithm
      with a sorted adjacency list (use a heap or sorted list).
"""

from collections import defaultdict


def find_itinerary(tickets: list[list[str]]) -> list[str]:
    pass


print(find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# Expected: ["JFK","MUC","LHR","SFO","SJC"]

print(find_itinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# Expected: ["JFK","ATL","JFK","SFO","ATL","SFO"]
