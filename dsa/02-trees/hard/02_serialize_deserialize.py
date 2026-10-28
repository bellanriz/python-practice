"""
LeetCode 297 - Serialize and Deserialize Binary Tree

Design an algorithm to serialize a binary tree to a string and
deserialize that string back to the original tree structure.

Example 1:
    Input:  root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

Example 2:
    Input:  root = []
    Output: []

Constraints:
    - Number of nodes is in [0, 10^4].

Hint: Use BFS or preorder DFS. Represent null nodes with a sentinel
      like "N" or "#".
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: TreeNode) -> str:
        pass

    def deserialize(self, data: str) -> TreeNode:
        pass


def to_list(root):
    if not root: return []
    res, q = [], [root]
    while q:
        n = q.pop(0)
        if n:
            res.append(n.val); q.append(n.left); q.append(n.right)
        else:
            res.append(None)
    while res and res[-1] is None: res.pop()
    return res

codec = Codec()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
data = codec.serialize(root)
print(to_list(codec.deserialize(data)))  # Expected: [1, 2, 3, None, None, 4, 5]
