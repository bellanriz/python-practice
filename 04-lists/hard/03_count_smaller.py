"""
LeetCode 315 - Count of Smaller Numbers After Self

Given an integer array nums, return a list counts where counts[i] is
the number of smaller elements to the right of nums[i].

Example 1:
    Input:  nums = [5, 2, 6, 1]
    Output: [2, 1, 1, 0]
    Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there are 0 smaller elements.

Example 2:
    Input:  nums = [-1]
    Output: [0]

Example 3:
    Input:  nums = [-1, -1]
    Output: [0, 0]

Constraints:
    - 1 <= len(nums) <= 10^5
    - -10^4 <= nums[i] <= 10^4

Hint: A brute-force O(n^2) is too slow. Consider:
      - Merge sort with index tracking
      - Binary Indexed Tree (BIT / Fenwick Tree)
      - Balanced BST approach
"""


def count_smaller(nums: list[int]) -> list[int]:
    pass


# Test cases
print(count_smaller([5, 2, 6, 1]))   # Expected: [2, 1, 1, 0]
print(count_smaller([-1]))            # Expected: [0]
print(count_smaller([-1, -1]))        # Expected: [0, 0]
