"""
LeetCode 24 - Swap Nodes in Pairs

Swap every two adjacent nodes and return the head.
Do not modify values — only change nodes.

Example 1:
    Input:  [1, 2, 3, 4]
    Output: [2, 1, 4, 3]

Example 2:
    Input:  [1]
    Output: [1]

Constraints:
    - Number of nodes is in [0, 100].
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head: ListNode) -> ListNode:
    pass


def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def show(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

print(show(swap_pairs(build([1,2,3,4]))))  # Expected: [2,1,4,3]
print(show(swap_pairs(build([1]))))         # Expected: [1]
