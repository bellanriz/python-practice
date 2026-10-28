"""
LeetCode 857 - Minimum Cost to Hire K Workers

There are n workers. Worker i has quality[i] and wage[i] (minimum
expected wage). You need to hire exactly k workers such that:
    - Every hired worker is paid proportional to their quality.
    - Every hired worker receives at least their minimum wage.

Return the least amount of money needed.

Example 1:
    Input:  quality=[10,20,5], wage=[70,50,30], k=2
    Output: 105.0

Example 2:
    Input:  quality=[3,1,10,10,1], wage=[4,8,2,2,7], k=3
    Output: 30.66667

Constraints:
    - n == len(quality) == len(wage)
    - 1 <= k <= n <= 10^4

Hint: Sort by wage/quality ratio. For each worker as the "rate setter",
      pick the k-1 workers with smallest quality among those with
      lower ratio. Use a max-heap to track qualities.
"""

import heapq


def mincost_to_hire_workers(quality: list[int], wage: list[int], k: int) -> float:
    pass


print(mincost_to_hire_workers([10,20,5], [70,50,30], 2))        # Expected: 105.0
print(f"{mincost_to_hire_workers([3,1,10,10,1], [4,8,2,2,7], 3):.5f}")  # Expected: ~30.66667
