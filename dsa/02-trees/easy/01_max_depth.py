"""
LeetCode 104 - Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
Maximum depth = number of nodes along the longest path from root
to the farthest leaf.

Example 1:
    Input:  root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input:  root = [1,null,2]
    Output: 2

Constraints:
    - Number of nodes is in [0, 10^4].
    - -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    pass


# Test cases
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_depth(root1))  # Expected: 3

root2 = TreeNode(1, None, TreeNode(2))
print(max_depth(root2))  # Expected: 2

print(max_depth(None))   # Expected: 0
