"""
LeetCode 23 - Merge k Sorted Lists

Given an array of k sorted linked lists, merge them into one sorted list.

Example 1:
    Input:  lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

Example 2:
    Input:  lists = []
    Output: []

Constraints:
    - 0 <= k <= 10^4
    - 0 <= len(lists[i]) <= 500
    - lists[i] is sorted ascending.

Hint: Use a min-heap or divide-and-conquer to merge pairs.
"""

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list) -> ListNode:
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

lists = [build([1,4,5]), build([1,3,4]), build([2,6])]
print(show(merge_k_lists(lists)))  # Expected: [1,1,2,3,4,4,5,6]
