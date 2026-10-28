"""
LeetCode 121 - Best Time to Buy and Sell Stock

Given an array prices where prices[i] is the stock price on day i,
find the maximum profit from one transaction (buy one day, sell later).
If no profit is possible, return 0.

Example 1:
    Input:  prices = [7, 1, 5, 3, 6, 4]
    Output: 5  (buy at 1, sell at 6)

Example 2:
    Input:  prices = [7, 6, 4, 3, 1]
    Output: 0  (prices only decrease)

Constraints:
    - 1 <= len(prices) <= 10^5

Hint: Track the minimum price seen so far and the max profit at each step.
"""


def max_profit(prices: list[int]) -> int:
    pass


print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(max_profit([7, 6, 4, 3, 1]))     # Expected: 0
