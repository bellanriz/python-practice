"""
LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, repeatedly remove consecutive
sequences of nodes that sum to 0 until no such sequences exist.

Example 1:
    Input:  head = [1, 2, -3, 3, 1]
    Output: [3, 1]  (1+2+(-3) = 0 removed, leaving [3, 1])

Example 2:
    Input:  head = [1, 2, 3, -3, 4]
    Output: [1, 2, 4]

Example 3:
    Input:  head = [1, 2, 3, -3, -2]
    Output: [1]

Constraints:
    - 1 <= number of nodes <= 1000
    - -1000 <= Node.val <= 1000

Hint: Use prefix sums. If the same prefix sum appears twice, all
      nodes between those two points sum to zero and can be removed.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_zero_sum_sublists(head: ListNode) -> ListNode:
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

print(show(remove_zero_sum_sublists(build([1,2,-3,3,1]))))   # Expected: [3,1]
print(show(remove_zero_sum_sublists(build([1,2,3,-3,4]))))    # Expected: [1,2,4]
print(show(remove_zero_sum_sublists(build([1,2,3,-3,-2]))))   # Expected: [1]
