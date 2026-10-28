"""
LeetCode 98 - Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid BST.

A valid BST:
    - Left subtree contains only nodes with keys < node's key
    - Right subtree contains only nodes with keys > node's key
    - Both subtrees are also valid BSTs.

Example 1:
    Input:  root = [2,1,3]
    Output: True

Example 2:
    Input:  root = [5,1,4,null,null,3,6]
    Output: False (4 is in the right subtree of 5 but 4 < 5... wait,
            actually 3 is in right subtree but 3 < 5)

Constraints:
    - Number of nodes is in [1, 10^4].

Hint: Use recursion with min/max bounds, or do an inorder traversal
      and check that values are strictly increasing.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    pass


root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_valid_bst(root1))  # Expected: True

root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(is_valid_bst(root2))  # Expected: False
