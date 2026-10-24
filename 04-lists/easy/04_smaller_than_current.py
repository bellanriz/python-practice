"""
LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in
the array are smaller than it. Return the counts as an array.

Example 1:
    Input:  nums = [8, 1, 2, 2, 3]
    Output: [4, 0, 1, 1, 3]
    Explanation:
        For nums[0]=8, there are 4 smaller numbers (1, 2, 2, 3).
        For nums[1]=1, there are 0 smaller numbers.
        For nums[2]=2, there is 1 smaller number (1).
        For nums[3]=2, there is 1 smaller number (1).
        For nums[4]=3, there are 3 smaller numbers (1, 2, 2).

Example 2:
    Input:  nums = [6, 5, 4, 8]
    Output: [2, 1, 0, 3]

Example 3:
    Input:  nums = [7, 7, 7, 7]
    Output: [0, 0, 0, 0]

Constraints:
    - 2 <= len(nums) <= 500
    - 0 <= nums[i] <= 100

Hint: A brute-force is O(n^2). Can you do better by sorting first?
"""


def smaller_numbers_than_current(nums: list[int]) -> list[int]:
    pass


# Test cases
print(smaller_numbers_than_current([8, 1, 2, 2, 3]))  # Expected: [4, 0, 1, 1, 3]
print(smaller_numbers_than_current([6, 5, 4, 8]))      # Expected: [2, 1, 0, 3]
print(smaller_numbers_than_current([7, 7, 7, 7]))      # Expected: [0, 0, 0, 0]
