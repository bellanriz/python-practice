"""
LeetCode 115 - Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences
of s which equals t.

Example 1:
    Input:  s = "rabbbit", t = "rabbit"
    Output: 3

Example 2:
    Input:  s = "babgbag", t = "bag"
    Output: 5

Constraints:
    - 1 <= len(s), len(t) <= 1000

Hint: dp[i][j] = number of ways s[0:i] has subsequence t[0:j].
      If s[i-1]==t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
      Else: dp[i][j] = dp[i-1][j]
"""


def num_distinct(s: str, t: str) -> int:
    pass


print(num_distinct("rabbbit", "rabbit"))  # Expected: 3
print(num_distinct("babgbag", "bag"))     # Expected: 5
