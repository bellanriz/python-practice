"""
LeetCode 100 - Same Tree

Given the roots of two binary trees p and q, check if they are the
same (structurally identical with same node values).

Example 1:
    Input:  p = [1,2,3], q = [1,2,3]
    Output: True

Example 2:
    Input:  p = [1,2], q = [1,null,2]
    Output: False

Example 3:
    Input:  p = [1,2,1], q = [1,1,2]
    Output: False

Constraints:
    - Number of nodes is in [0, 100].
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    pass


# Test cases
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_same_tree(p1, q1))  # Expected: True

p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print(is_same_tree(p2, q2))  # Expected: False
