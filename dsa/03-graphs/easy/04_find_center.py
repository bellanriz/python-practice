"""
LeetCode 1791 - Find Center of Star Graph

A star graph has n nodes (1..n) where one center node is connected
to every other node. Given the edges, find the center.

Example 1:
    Input:  edges = [[1,2],[2,3],[4,2]]
    Output: 2

Example 2:
    Input:  edges = [[1,2],[5,1],[1,3],[1,4]]
    Output: 1

Constraints:
    - 3 <= n <= 10^5
    - edges.length == n - 1

Hint: The center appears in every edge. Check the first two edges.
"""


def find_center(edges: list[list[int]]) -> int:
    pass


print(find_center([[1,2],[2,3],[4,2]]))        # Expected: 2
print(find_center([[1,2],[5,1],[1,3],[1,4]]))  # Expected: 1
