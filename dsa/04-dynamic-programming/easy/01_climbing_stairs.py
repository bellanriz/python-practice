"""
LeetCode 70 - Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

Example 1:
    Input:  n = 2
    Output: 2  (1+1 or 2)

Example 2:
    Input:  n = 3
    Output: 3  (1+1+1, 1+2, 2+1)

Constraints:
    - 1 <= n <= 45

Hint: dp[i] = dp[i-1] + dp[i-2]. This is the Fibonacci sequence.
"""


def climb_stairs(n: int) -> int:
    pass


print(climb_stairs(2))   # Expected: 2
print(climb_stairs(3))   # Expected: 3
print(climb_stairs(5))   # Expected: 8
