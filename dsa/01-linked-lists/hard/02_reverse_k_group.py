"""
LeetCode 25 - Reverse Nodes in k-Group

Reverse the nodes of a linked list k at a time. If remaining nodes
are fewer than k, leave them as-is.

Example 1:
    Input:  head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input:  head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    - 1 <= k <= n <= 5000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: ListNode, k: int) -> ListNode:
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

print(show(reverse_k_group(build([1,2,3,4,5]), 2)))  # Expected: [2,1,4,3,5]
print(show(reverse_k_group(build([1,2,3,4,5]), 3)))  # Expected: [3,2,1,4,5]
