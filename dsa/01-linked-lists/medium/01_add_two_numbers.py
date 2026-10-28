"""
LeetCode 2 - Add Two Numbers

Two non-empty linked lists represent two non-negative integers.
Digits are stored in reverse order. Add the two numbers and return
the sum as a linked list.

Example 1:
    Input:  l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807

Example 2:
    Input:  l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    - Number of nodes in each list is in [1, 100].
    - 0 <= Node.val <= 9
    - No leading zeros except the number 0 itself.

Hint: Traverse both lists simultaneously, tracking the carry.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
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

print(show(add_two_numbers(build([2,4,3]), build([5,6,4]))))          # Expected: [7,0,8]
print(show(add_two_numbers(build([9,9,9,9,9,9,9]), build([9,9,9,9]))))  # Expected: [8,9,9,9,0,0,0,1]
