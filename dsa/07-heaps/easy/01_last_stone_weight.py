"""
LeetCode 1046 - Last Stone Weight

We have a collection of stones with positive integer weights. Each
turn, take the two heaviest stones and smash them:
    - If equal, both destroyed.
    - Otherwise, the lighter is destroyed and the heavier loses the
      lighter's weight.

Return the weight of the last remaining stone, or 0 if none.

Example 1:
    Input:  stones = [2, 7, 4, 1, 8, 1]
    Output: 1

Constraints:
    - 1 <= len(stones) <= 30

Hint: Use a max-heap. Python's heapq is a min-heap, so negate values.
"""

import heapq


def last_stone_weight(stones: list[int]) -> int:
    pass


print(last_stone_weight([2, 7, 4, 1, 8, 1]))  # Expected: 1
