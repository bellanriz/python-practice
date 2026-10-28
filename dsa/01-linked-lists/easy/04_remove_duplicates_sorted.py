"""
LeetCode 83 - Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such
that each element appears only once. Return the sorted list.

Example 1:
    Input:  head = [1, 1, 2]
    Output: [1, 2]

Example 2:
    Input:  head = [1, 1, 2, 3, 3]
    Output: [1, 2, 3]

Constraints:
    - Number of nodes is in [0, 300].
    - -100 <= Node.val <= 100
    - List is sorted in ascending order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode) -> ListNode:
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

print(show(delete_duplicates(build([1, 1, 2]))))        # Expected: [1, 2]
print(show(delete_duplicates(build([1, 1, 2, 3, 3]))))  # Expected: [1, 2, 3]
