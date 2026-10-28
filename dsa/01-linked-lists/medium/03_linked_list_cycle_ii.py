"""
LeetCode 142 - Linked List Cycle II

Given the head of a linked list, return the node where the cycle
begins. If there is no cycle, return None.

Example 1:
    Input:  head = [3,2,0,-4], tail connects to index 1
    Output: node with val 2

Example 2:
    Input:  head = [1], no cycle
    Output: None

Constraints:
    - Number of nodes is in [0, 10^4].

Hint: After Floyd's detection, reset one pointer to head. Move both
      one step at a time — they meet at the cycle start.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head: ListNode) -> ListNode:
    pass


n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
result = detect_cycle(n1)
print(result.val if result else None)  # Expected: 2
print(detect_cycle(ListNode(1)))        # Expected: None
