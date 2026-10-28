"""
LeetCode 19 - Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end
and return its head.

Example 1:
    Input:  head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input:  head = [1], n = 1
    Output: []

Example 3:
    Input:  head = [1,2], n = 1
    Output: [1]

Constraints:
    - 1 <= sz <= 30
    - 1 <= n <= sz

Hint: Use two pointers spaced n nodes apart.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
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

print(show(remove_nth_from_end(build([1,2,3,4,5]), 2)))  # Expected: [1,2,3,5]
print(show(remove_nth_from_end(build([1]), 1)))            # Expected: []
