"""
LeetCode 141 - Linked List Cycle

Given head, determine if the linked list has a cycle in it.
Return True if there is a cycle, False otherwise.

Example 1:
    Input:  head = [3,2,0,-4], tail connects to index 1
    Output: True

Example 2:
    Input:  head = [1], no cycle
    Output: False

Constraints:
    - Number of nodes is in [0, 10^4].
    - -10^5 <= Node.val <= 10^5

Hint: Floyd's Cycle Detection — slow pointer (1 step) and fast
      pointer (2 steps). If they meet, there's a cycle.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    pass


# Test cases
n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
print(has_cycle(n1))      # Expected: True
print(has_cycle(ListNode(1)))  # Expected: False
