"""
LeetCode 231 - Power of Two

Given an integer n, return True if it is a power of two, else False.

Example 1:
    Input:  n = 1
    Output: True  (2^0)

Example 2:
    Input:  n = 16
    Output: True  (2^4)

Example 3:
    Input:  n = 3
    Output: False

Constraints:
    - -2^31 <= n <= 2^31 - 1

Challenge: Solve recursively (divide by 2 until base case).
           Also try: n > 0 and n & (n-1) == 0.
"""


def is_power_of_two(n: int) -> bool:
    pass


print(is_power_of_two(1))    # Expected: True
print(is_power_of_two(16))   # Expected: True
print(is_power_of_two(3))    # Expected: False
print(is_power_of_two(0))    # Expected: False
