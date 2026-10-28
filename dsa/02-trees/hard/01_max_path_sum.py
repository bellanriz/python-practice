"""
LeetCode 124 - Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of
adjacent nodes has an edge. A node can only appear once in the path.
The path does not need to pass through the root.

Return the maximum path sum of any non-empty path.

Example 1:
    Input:  root = [1,2,3]
    Output: 6  (path: 2->1->3)

Example 2:
    Input:  root = [-10,9,20,null,null,15,7]
    Output: 42  (path: 15->20->7)

Constraints:
    - Number of nodes is in [1, 3 * 10^4].
    - -1000 <= Node.val <= 1000

Hint: At each node, compute the max sum using that node as the
      "turning point". Track a global max. Return the max single-branch
      sum upward.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    pass


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(max_path_sum(root1))  # Expected: 6

root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_path_sum(root2))  # Expected: 42
