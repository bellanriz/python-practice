"""
LeetCode 234 - Palindrome Linked List

Given the head of a singly linked list, return True if it is a
palindrome.

Example 1:
    Input:  head = [1, 2, 2, 1]
    Output: True

Example 2:
    Input:  head = [1, 2]
    Output: False

Constraints:
    - Number of nodes is in [1, 10^5].

Challenge: Solve using recursion. The recursive approach compares
           from outside-in by using the call stack.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    pass


def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

print(is_palindrome(build([1, 2, 2, 1])))  # Expected: True
print(is_palindrome(build([1, 2])))          # Expected: False
