"""
LeetCode 1672 - Richest Customer Wealth

You are given an m x n integer grid 'accounts' where accounts[i][j]
is the amount of money the i-th customer has in the j-th bank.

Return the wealth that the richest customer has.

A customer's wealth is the sum of money in all their bank accounts.

Example 1:
    Input:  accounts = [[1, 2, 3], [3, 2, 1]]
    Output: 6
    Explanation:
        Customer 0 wealth = 1 + 2 + 3 = 6
        Customer 1 wealth = 3 + 2 + 1 = 6
        Both have wealth 6, so return 6.

Example 2:
    Input:  accounts = [[1, 5], [7, 3], [3, 5]]
    Output: 10
    Explanation:
        Customer 0 wealth = 6
        Customer 1 wealth = 10
        Customer 2 wealth = 8
        The richest customer has wealth 10.

Example 3:
    Input:  accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    Output: 17

Constraints:
    - m == len(accounts)
    - n == len(accounts[i])
    - 1 <= m, n <= 50
    - 1 <= accounts[i][j] <= 100
"""


def maximum_wealth(accounts: list[list[int]]) -> int:
    pass


# Test cases
print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))              # Expected: 6
print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))            # Expected: 10
print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))  # Expected: 17
