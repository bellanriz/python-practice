"""
LeetCode 101 - Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of
itself (symmetric around its center).

Example 1:
    Input:  root = [1,2,2,3,4,4,3]
    Output: True

Example 2:
    Input:  root = [1,2,2,null,3,null,3]
    Output: False

Constraints:
    - Number of nodes is in [1, 1000].

Hint: Recursively compare left.left with right.right and
      left.right with right.left.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    pass


root1 = TreeNode(1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3))
)
print(is_symmetric(root1))  # Expected: True

root2 = TreeNode(1,
    TreeNode(2, None, TreeNode(3)),
    TreeNode(2, None, TreeNode(3))
)
print(is_symmetric(root2))  # Expected: False
