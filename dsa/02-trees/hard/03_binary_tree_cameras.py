"""
LeetCode 968 - Binary Tree Cameras

You are installing cameras on tree nodes. Each camera monitors its
parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes.

Example 1:
    Input:  root = [0,0,null,0,0]
    Output: 1
    Explanation: One camera at the root's left child covers all nodes.

Example 2:
    Input:  root = [0,0,null,0,null,0,null,null,0]
    Output: 2

Constraints:
    - Number of nodes is in [1, 1000].

Hint: Use a greedy post-order DFS. Each node is in one of three states:
      0 = needs coverage, 1 = has camera, 2 = covered (no camera).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_camera_cover(root: TreeNode) -> int:
    pass


# [0,0,null,0,0]
root1 = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)))
print(min_camera_cover(root1))  # Expected: 1

# [0,0,null,0,null,0,null,null,0]
root2 = TreeNode(0, TreeNode(0, TreeNode(0, None, TreeNode(0)), None))
print(min_camera_cover(root2))  # Expected: 2
