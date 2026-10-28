"""
LeetCode 188 - Best Time to Buy and Sell Stock IV

Given an array of prices and an integer k, find the maximum profit
with at most k transactions.

Example 1:
    Input:  k = 2, prices = [2, 4, 1]
    Output: 2  (buy at 2, sell at 4)

Example 2:
    Input:  k = 2, prices = [3, 2, 6, 5, 0, 3]
    Output: 7  (buy at 2 sell at 6, buy at 0 sell at 3)

Constraints:
    - 1 <= k <= 100
    - 1 <= len(prices) <= 1000

Hint: dp[j][0] = max profit with j transactions done, not holding.
      dp[j][1] = max profit with j transactions done, holding stock.
"""


def max_profit(k: int, prices: list[int]) -> int:
    pass


print(max_profit(2, [2, 4, 1]))            # Expected: 2
print(max_profit(2, [3, 2, 6, 5, 0, 3]))  # Expected: 7
