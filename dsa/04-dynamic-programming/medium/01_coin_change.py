"""
LeetCode 322 - Coin Change

Given coins of different denominations and a total amount, return the
fewest number of coins needed to make that amount. If it cannot be
made, return -1.

Example 1:
    Input:  coins = [1, 5, 11], amount = 11
    Output: 1

Example 2:
    Input:  coins = [2], amount = 3
    Output: -1

Example 3:
    Input:  coins = [1, 2, 5], amount = 11
    Output: 3  (5+5+1)

Constraints:
    - 1 <= len(coins) <= 12
    - 0 <= amount <= 10^4

Hint: dp[i] = min coins to make amount i.
      dp[i] = min(dp[i - coin] + 1) for each coin.
"""


def coin_change(coins: list[int], amount: int) -> int:
    pass


print(coin_change([1, 5, 11], 11))  # Expected: 1
print(coin_change([2], 3))           # Expected: -1
print(coin_change([1, 2, 5], 11))   # Expected: 3
