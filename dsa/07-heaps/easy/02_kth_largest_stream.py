"""
LeetCode 703 - Kth Largest Element in a Stream

Design a class that finds the kth largest element in a stream.

    - KthLargest(k, nums)  -> Initialize with k and initial array.
    - add(val)             -> Add val to the stream and return the
                              kth largest element.

Example:
    kl = KthLargest(3, [4, 5, 8, 2])
    kl.add(3)   # -> 4
    kl.add(5)   # -> 5
    kl.add(10)  # -> 5
    kl.add(9)   # -> 8
    kl.add(4)   # -> 8

Constraints:
    - 1 <= k <= 10^4

Hint: Maintain a min-heap of size k. The heap top is the kth largest.
"""

import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        pass

    def add(self, val: int) -> int:
        pass


kl = KthLargest(3, [4, 5, 8, 2])
print(kl.add(3))   # Expected: 4
print(kl.add(5))   # Expected: 5
print(kl.add(10))  # Expected: 5
print(kl.add(9))   # Expected: 8
print(kl.add(4))   # Expected: 8
