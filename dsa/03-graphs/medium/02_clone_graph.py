"""
LeetCode 133 - Clone Graph

Given a reference of a node in a connected undirected graph, return
a deep copy of the graph. Each node has a val and a list of neighbors.

Example 1:
    Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    (a deep copy of the same graph)

Constraints:
    - Number of nodes is in [0, 100].
    - 1 <= Node.val <= 100
    - No repeated edges or self-loops.

Hint: Use a hash map {original_node: cloned_node} and BFS or DFS.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    pass


# Test case
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

clone = clone_graph(n1)
print(clone.val)                                      # Expected: 1
print([n.val for n in clone.neighbors])               # Expected: [2, 4]
print(clone is not n1)                                 # Expected: True (deep copy)
