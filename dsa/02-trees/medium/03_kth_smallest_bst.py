"""
LeetCode 230 - Kth Smallest Element in a BST

Given the root of a BST and an integer k, return the kth smallest
value (1-indexed) of all node values in the BST.

Example 1:
    Input:  root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:
    Input:  root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

Constraints:
    - Number of nodes is n, 1 <= k <= n <= 10^4.

Hint: Inorder traversal of a BST gives values in sorted order.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode, k: int) -> int:
    pass


root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kth_smallest(root1, 1))  # Expected: 1

root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(kth_smallest(root2, 3))  # Expected: 3
