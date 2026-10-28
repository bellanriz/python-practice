"""
LeetCode 236 - Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two
given nodes p and q.

The LCA is the lowest node that has both p and q as descendants
(a node can be a descendant of itself).

Example 1:
    Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3

Example 2:
    Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5

Constraints:
    - Number of nodes is in [2, 10^5].
    - All Node.val are unique.
    - p != q, both exist in the tree.

Hint: Recurse left and right. If both sides return non-null,
      current node is the LCA. Otherwise return whichever is non-null.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass


# Build tree: [3,5,1,6,2,0,8,null,null,7,4]
n7, n4 = TreeNode(7), TreeNode(4)
n6, n2 = TreeNode(6), TreeNode(2, n7, n4)
n0, n8 = TreeNode(0), TreeNode(8)
n5 = TreeNode(5, n6, n2)
n1 = TreeNode(1, n0, n8)
root = TreeNode(3, n5, n1)

print(lowest_common_ancestor(root, n5, n1).val)  # Expected: 3
print(lowest_common_ancestor(root, n5, n4).val)  # Expected: 5
