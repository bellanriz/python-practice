"""
LeetCode 746 - Min Cost Climbing Stairs

Given an array cost where cost[i] is the cost of step i, you can
start from step 0 or step 1. Each time, climb 1 or 2 steps.
Return the minimum cost to reach the top (past the last step).

Example 1:
    Input:  cost = [10, 15, 20]
    Output: 15  (start at index 1, pay 15, climb 2 steps to top)

Example 2:
    Input:  cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6

Constraints:
    - 2 <= len(cost) <= 1000

Hint: dp[i] = cost[i] + min(dp[i-1], dp[i-2])
"""


def min_cost_climbing_stairs(cost: list[int]) -> int:
    pass


print(min_cost_climbing_stairs([10, 15, 20]))                       # Expected: 15
print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Expected: 6
