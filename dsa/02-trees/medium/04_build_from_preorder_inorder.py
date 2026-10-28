"""
LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder, construct and return
the binary tree.

Example 1:
    Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

Example 2:
    Input:  preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    - 1 <= len(preorder) <= 3000
    - preorder and inorder consist of unique values.

Hint: First element of preorder is the root. Find it in inorder to
      split left and right subtrees. Recurse.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    pass


def to_list(root):
    if not root: return []
    res, q = [], [root]
    while q:
        n = q.pop(0)
        if n:
            res.append(n.val); q.append(n.left); q.append(n.right)
        else:
            res.append(None)
    while res and res[-1] is None: res.pop()
    return res

print(to_list(build_tree([3,9,20,15,7], [9,3,15,20,7])))  # Expected: [3,9,20,None,None,15,7]
