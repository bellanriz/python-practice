"""
LeetCode 1971 - Find if Path Exists in Graph

Given n vertices (0..n-1) and edges, determine if there is a valid
path from source to destination.

Example 1:
    Input:  n=3, edges=[[0,1],[1,2],[2,0]], source=0, dest=2
    Output: True

Example 2:
    Input:  n=6, edges=[[0,1],[0,2],[3,5],[5,4],[4,3]], source=0, dest=5
    Output: False

Constraints:
    - 1 <= n <= 2 * 10^5

Hint: Use BFS, DFS, or Union-Find.
"""

from collections import deque, defaultdict


def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    pass


print(valid_path(3, [[0,1],[1,2],[2,0]], 0, 2))                          # Expected: True
print(valid_path(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))              # Expected: False
