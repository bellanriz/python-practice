"""
LeetCode 138 - Copy List with Random Pointer

A linked list where each node has an additional random pointer that
could point to any node or null. Construct a deep copy of the list.

Each node has: val (int), next (Node), random (Node).

Example 1:
    Input:  head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    (Each pair is [val, random_index])

Example 2:
    Input:  head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]

Constraints:
    - 0 <= n <= 1000
    - -10^4 <= Node.val <= 10^4
    - Node.random is null or points to a node in the list.

Hint: Use a hash map mapping original -> copy. Or interleave copies
      between originals, set random pointers, then separate.
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    pass


# Test case
n1, n2, n3 = Node(7), Node(13), Node(11)
n1.next = n2; n2.next = n3
n1.random = None; n2.random = n1; n3.random = n1
copy = copy_random_list(n1)
cur = copy
while cur:
    r = cur.random.val if cur.random else None
    print(f"val={cur.val}, random={r}")
    cur = cur.next
# Expected: val=7 random=None, val=13 random=7, val=11 random=7
