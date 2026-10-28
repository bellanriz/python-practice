"""
LeetCode 1705 - Maximum Number of Eaten Apples

On day i, a tree grows apples[i] apples that rot after days[i] days
(i.e., they rot on day i + days[i]). You can eat at most 1 apple/day,
and you can eat past day n-1 as long as you have apples.

Return the maximum number of apples you can eat.

Example 1:
    Input:  apples = [1,2,3,5,2], days = [3,2,1,4,2]
    Output: 7

Example 2:
    Input:  apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
    Output: 5

Constraints:
    - len(apples) == len(days) == n
    - 1 <= n <= 2 * 10^4

Hint: Use a min-heap sorted by expiration day. Each day, eat the
      apple that expires soonest (greedy). Remove expired apples.
"""

import heapq


def eaten_apples(apples: list[int], days: list[int]) -> int:
    pass


print(eaten_apples([1,2,3,5,2], [3,2,1,4,2]))     # Expected: 7
print(eaten_apples([3,0,0,0,0,2], [3,0,0,0,0,2]))  # Expected: 5
