"""
LeetCode 847 - Shortest Path Visiting All Nodes

Given an undirected connected graph of n nodes (0..n-1), return the
length of the shortest path that visits every node. You may start
and stop at any node and revisit nodes/edges.

Example 1:
    Input:  graph = [[1,2,3],[0],[0],[0]]
    Output: 4

Example 2:
    Input:  graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    Output: 4

Constraints:
    - 1 <= n <= 12

Hint: BFS with bitmask. State = (current_node, visited_bitmask).
      Start BFS from all nodes simultaneously. Goal: all bits set.
"""

from collections import deque


def shortest_path_length(graph: list[list[int]]) -> int:
    pass


print(shortest_path_length([[1,2,3],[0],[0],[0]]))          # Expected: 4
print(shortest_path_length([[1],[0,2,4],[1,3,4],[2],[1,2]]))  # Expected: 4
