"""
LeetCode 987 - Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, return its vertical order traversal.

For each node at position (row, col):
    - Left child is at (row+1, col-1)
    - Right child is at (row+1, col+1)

Sort by column, then by row, then by value.

Example 1:
    Input:  root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]

Example 2:
    Input:  root = [1,2,3,4,5,6,7]
    Output: [[4],[2],[1,5,6],[3],[7]]

Constraints:
    - Number of nodes is in [1, 1000].

Hint: BFS/DFS tracking (row, col). Use a sorted dict or sort tuples.
"""

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root: TreeNode) -> list[list[int]]:
    pass


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(vertical_traversal(root))  # Expected: [[9],[3,15],[20],[7]]
