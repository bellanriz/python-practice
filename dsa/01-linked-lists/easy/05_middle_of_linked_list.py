"""
LeetCode 876 - Middle of the Linked List

Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.

Example 1:
    Input:  head = [1,2,3,4,5]
    Output: [3,4,5]   (middle is node 3)

Example 2:
    Input:  head = [1,2,3,4,5,6]
    Output: [4,5,6]   (second middle is node 4)

Constraints:
    - Number of nodes is in [1, 100].

Hint: Slow/fast pointer technique.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: ListNode) -> ListNode:
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

print(show(middle_node(build([1,2,3,4,5]))))    # Expected: [3,4,5]
print(show(middle_node(build([1,2,3,4,5,6]))))  # Expected: [4,5,6]
