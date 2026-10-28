"""
LeetCode 206 - Reverse Linked List

Given the head of a singly linked list, reverse the list and return
the reversed list.

Example 1:
    Input:  head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Example 2:
    Input:  head = [1, 2]
    Output: [2, 1]

Example 3:
    Input:  head = []
    Output: []

Constraints:
    - The number of nodes is in range [0, 5000].
    - -5000 <= Node.val <= 5000

Challenge: Solve it both iteratively and recursively.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    pass


# Helpers
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

# Test cases
print(show(reverse_list(build([1, 2, 3, 4, 5]))))  # Expected: [5, 4, 3, 2, 1]
print(show(reverse_list(build([1, 2]))))             # Expected: [2, 1]
print(show(reverse_list(build([]))))                  # Expected: []
