"""
LeetCode 2558 - Take Gifts From the Richest Pile

Given gifts (array of pile sizes) and k seconds, each second:
    - Pick the pile with the most gifts.
    - Leave behind floor(sqrt(gifts)) in that pile.

Return the total number of gifts remaining after k seconds.

Example 1:
    Input:  gifts = [25, 64, 9, 4, 100], k = 4
    Output: 29

Example 2:
    Input:  gifts = [1, 1, 1, 1], k = 4
    Output: 4

Constraints:
    - 1 <= len(gifts) <= 10^3
    - 1 <= k <= 10^3

Hint: Use a max-heap. Each step, pop the max, push floor(sqrt(max)).
"""

import heapq
import math


def pick_gifts(gifts: list[int], k: int) -> int:
    pass


print(pick_gifts([25, 64, 9, 4, 100], 4))  # Expected: 29
print(pick_gifts([1, 1, 1, 1], 4))          # Expected: 4
