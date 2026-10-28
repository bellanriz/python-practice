"""
LeetCode 338 - Counting Bits

Given an integer n, return an array ans of length n+1 where ans[i]
is the number of 1's in the binary representation of i.

Example 1:
    Input:  n = 2
    Output: [0, 1, 1]

Example 2:
    Input:  n = 5
    Output: [0, 1, 1, 2, 1, 2]

Constraints:
    - 0 <= n <= 10^5

Hint: dp[i] = dp[i >> 1] + (i & 1). Or dp[i] = dp[i & (i-1)] + 1.
"""


def count_bits(n: int) -> list[int]:
    pass


print(count_bits(2))   # Expected: [0, 1, 1]
print(count_bits(5))   # Expected: [0, 1, 1, 2, 1, 2]
