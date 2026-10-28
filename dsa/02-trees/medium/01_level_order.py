"""
LeetCode 102 - Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal
(values grouped by level, left to right).

Example 1:
    Input:  root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input:  root = [1]
    Output: [[1]]

Constraints:
    - Number of nodes is in [0, 2000].

Hint: Use BFS with a queue (collections.deque).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> list[list[int]]:
    pass


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(root))   # Expected: [[3],[9,20],[15,7]]
print(level_order(None))   # Expected: []
