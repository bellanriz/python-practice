"""
LeetCode 21 - Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list.

Example 1:
    Input:  list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input:  list1 = [], list2 = []
    Output: []

Example 3:
    Input:  list1 = [], list2 = [0]
    Output: [0]

Constraints:
    - Both lists are sorted in non-decreasing order.
    - Number of nodes in both lists is in [0, 50].
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
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

print(show(merge_two_lists(build([1,2,4]), build([1,3,4]))))  # Expected: [1,1,2,3,4,4]
print(show(merge_two_lists(build([]), build([0]))))             # Expected: [0]
