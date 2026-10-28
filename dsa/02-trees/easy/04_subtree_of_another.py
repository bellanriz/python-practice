"""
LeetCode 572 - Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return True if
there is a subtree of root with the same structure and node values
as subRoot.

Example 1:
    Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: True

Example 2:
    Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: False

Constraints:
    - Nodes in root: [1, 2000]
    - Nodes in subRoot: [1, 1000]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: TreeNode, subRoot: TreeNode) -> bool:
    pass


# Test cases
root1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub1 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root1, sub1))  # Expected: True

root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
sub2 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root2, sub2))  # Expected: False
