"""
LeetCode 543 - Diameter of Binary Tree

The diameter of a binary tree is the length of the longest path
between any two nodes. This path may or may not pass through the root.
The length is measured by the number of edges.

Example 1:
    Input:  root = [1,2,3,4,5]
    Output: 3  (path: 4->2->1->3 or 5->2->1->3)

Example 2:
    Input:  root = [1,2]
    Output: 1

Constraints:
    - Number of nodes is in [1, 10^4].
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode) -> int:
    pass


root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(diameter_of_binary_tree(root1))  # Expected: 3

root2 = TreeNode(1, TreeNode(2))
print(diameter_of_binary_tree(root2))  # Expected: 1
