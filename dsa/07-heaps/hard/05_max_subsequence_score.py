"""
LeetCode 2542 - Maximum Subsequence Score

Given two integer arrays nums1 and nums2 of equal length n, and a
positive integer k, choose a subsequence of indices of length k.
The score is: sum(nums1[i] for i in chosen) * min(nums2[i] for i in chosen).

Return the maximum possible score.

Example 1:
    Input:  nums1=[1,3,3,2], nums2=[2,1,3,4], k=3
    Output: 12  (indices 0,2,3: (1+3+2)*min(2,3,4) = 6*2 = 12)

Example 2:
    Input:  nums1=[4,2,3,1,1], nums2=[7,5,10,9,6], k=1
    Output: 30  (index 2: 3*10)

Constraints:
    - n == len(nums1) == len(nums2)
    - 1 <= k <= n <= 10^5

Hint: Sort pairs by nums2 descending. Use a min-heap of size k for
      nums1 values. For each new element, the current nums2 is the
      minimum. Track the running sum of nums1 in the heap.
"""

import heapq


def max_score(nums1: list[int], nums2: list[int], k: int) -> int:
    pass


print(max_score([1,3,3,2], [2,1,3,4], 3))        # Expected: 12
print(max_score([4,2,3,1,1], [7,5,10,9,6], 1))   # Expected: 30
