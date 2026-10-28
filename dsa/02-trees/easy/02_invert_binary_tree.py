"""
LeetCode 226 - Invert Binary Tree

Given the root of a binary tree, invert the tree (mirror it) and
return its root.

Example 1:
    Input:      4                Output:     4
              /   \\                        /   \\
             2     7                      7     2
            / \\   / \\                    / \\   / \\
           1   3 6   9                  9   6 3   1

Example 2:
    Input:  root = [2,1,3]
    Output: [2,3,1]

Constraints:
    - Number of nodes is in [0, 100].
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    pass


def to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
print(to_list(invert_tree(root)))  # Expected: [4, 7, 2, 9, 6, 3, 1]
