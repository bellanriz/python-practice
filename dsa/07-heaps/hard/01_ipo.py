"""
LeetCode 502 - IPO

You have initial capital w and can pick at most k projects. Each project
has a profit[i] and minimum capital[i] required. After finishing a
project, your capital increases by its profit. Maximize your final capital.

Example 1:
    Input:  k=2, w=0, profits=[1,2,3], capital=[0,1,1]
    Output: 4  (pick project 0 (profit 1, capital becomes 1),
                then project 2 (profit 3, capital becomes 4))

Example 2:
    Input:  k=3, w=0, profits=[1,2,3], capital=[0,1,2]
    Output: 6

Constraints:
    - 1 <= k <= 10^5
    - 0 <= w <= 10^9

Hint: Sort projects by capital. Use a max-heap of profits for
      affordable projects. Greedily pick the most profitable.
"""

import heapq


def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    pass


print(find_maximized_capital(2, 0, [1,2,3], [0,1,1]))  # Expected: 4
print(find_maximized_capital(3, 0, [1,2,3], [0,1,2]))  # Expected: 6
