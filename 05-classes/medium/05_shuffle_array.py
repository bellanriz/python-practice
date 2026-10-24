"""
LeetCode 384 - Shuffle an Array

Given an integer array nums, design an algorithm to randomly shuffle
the array. All permutations of the array should be equally likely.

Implement the Solution class:
    - Solution(nums)  -> Initializes the object with the integer array nums.
    - reset()         -> Resets the array to its original configuration
                         and returns it.
    - shuffle()       -> Returns a random shuffling of the array.

Example:
    sol = Solution([1, 2, 3])
    sol.shuffle()    # -> e.g. [3, 1, 2] (any permutation)
    sol.reset()      # -> [1, 2, 3]
    sol.shuffle()    # -> e.g. [1, 3, 2] (any permutation)

Constraints:
    - 1 <= len(nums) <= 50
    - -10^6 <= nums[i] <= 10^6
    - All elements of nums are unique.
    - At most 10^4 calls total will be made to reset and shuffle.

Hint: Use the Fisher-Yates (Knuth) shuffle algorithm for an unbiased
      random permutation. Iterate from the end, swapping each element
      with a random element at or before its position.
"""

import random


class Solution:

    def __init__(self, nums: list[int]):
        pass

    def reset(self) -> list[int]:
        pass

    def shuffle(self) -> list[int]:
        pass


# Test cases
sol = Solution([1, 2, 3])
print(sol.shuffle())  # Random permutation of [1, 2, 3]
print(sol.reset())    # Expected: [1, 2, 3]
print(sol.shuffle())  # Random permutation of [1, 2, 3]
