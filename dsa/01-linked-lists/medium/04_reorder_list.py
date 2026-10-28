"""
LeetCode 143 - Reorder List

Given: L0 -> L1 -> ... -> Ln-1 -> Ln
Reorder to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

Do not modify values — only change node pointers.

Example 1:
    Input:  [1, 2, 3, 4]
    Output: [1, 4, 2, 3]

Example 2:
    Input:  [1, 2, 3, 4, 5]
    Output: [1, 5, 2, 4, 3]

Constraints:
    - Number of nodes is in [1, 5 * 10^4].

Hint: 1) Find middle  2) Reverse second half  3) Merge alternately
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: ListNode) -> None:
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

h1 = build([1,2,3,4]); reorder_list(h1); print(show(h1))    # Expected: [1,4,2,3]
h2 = build([1,2,3,4,5]); reorder_list(h2); print(show(h2))  # Expected: [1,5,2,4,3]
