"""
LeetCode 1028 - Recover a Tree From Preorder Traversal

We run a preorder DFS on a binary tree. In the output, each node's
value is preceded by a number of dashes equal to its depth.

Given this traversal string, recover the tree and return its root.

Example 1:
    Input:  traversal = "1-2--3--4-5--6--7"
    Output: [1,2,5,3,4,6,7]

Example 2:
    Input:  traversal = "1-2--3---4-5--6---7"
    Output: [1,2,5,3,null,6,null,4,null,7]

Constraints:
    - Number of nodes is in [1, 1000].
    - 1 <= Node.val <= 10^9

Hint: Use a stack. Parse depth (count dashes) and value (digits).
      Pop stack until its size equals depth, then attach the node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recover_from_preorder(traversal: str) -> TreeNode:
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

print(to_list(recover_from_preorder("1-2--3--4-5--6--7")))
# Expected: [1, 2, 5, 3, 4, 6, 7]
