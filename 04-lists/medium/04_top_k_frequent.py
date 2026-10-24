"""
LeetCode 347 - Top K Frequent Elements

Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.

Example 1:
    Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Example 2:
    Input:  nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= len(nums) <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, number of unique elements in nums].
    - It is guaranteed that the answer is unique.

Hint: Count frequencies first. Then either:
      - Use a heap to get the top k elements in O(n log k)
      - Use bucket sort for O(n) — create buckets indexed by frequency
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    pass


# Test cases
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # Expected: [1, 2]
print(top_k_frequent([1], 1))                    # Expected: [1]
