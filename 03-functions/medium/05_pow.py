"""
LeetCode 50 - Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (x^n).

Do NOT use Python's built-in ** operator or pow() function.

Example 1:
    Input:  x = 2.00000, n = 10
    Output: 1024.00000

Example 2:
    Input:  x = 2.10000, n = 3
    Output: 9.26100

Example 3:
    Input:  x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2^(-2) = 1 / (2^2) = 1/4 = 0.25

Constraints:
    - -100.0 < x < 100.0
    - -2^31 <= n <= 2^31 - 1
    - n is an integer.
    - Either x is not zero or n > 0.
    - -10^4 <= x^n <= 10^4

Hint: A naive loop would be O(n) and too slow for large n. Use
      "exponentiation by squaring" for O(log n):
      x^n = (x^(n/2))^2  if n is even
      x^n = x * x^(n-1)  if n is odd
"""


def my_pow(x: float, n: int) -> float:
    pass


# Test cases
print(my_pow(2.00000, 10))   # Expected: 1024.0
print(my_pow(2.10000, 3))    # Expected: 9.261
print(my_pow(2.00000, -2))   # Expected: 0.25
