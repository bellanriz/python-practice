"""
LeetCode 148 - Sort List

Given the head of a linked list, sort it in ascending order.
You must do it in O(n log n) time and O(1) extra space.

Example 1:
    Input:  head = [4, 2, 1, 3]
    Output: [1, 2, 3, 4]

Example 2:
    Input:  head = [-1, 5, 3, 4, 0]
    Output: [-1, 0, 3, 4, 5]

Constraints:
    - Number of nodes is in [0, 5 * 10^4].

Hint: Use merge sort on linked list. Find middle with slow/fast,
      split, sort both halves recursively, then merge.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head: ListNode) -> ListNode:
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

print(show(sort_list(build([4, 2, 1, 3]))))       # Expected: [1, 2, 3, 4]
print(show(sort_list(build([-1, 5, 3, 4, 0]))))   # Expected: [-1, 0, 3, 4, 5]
