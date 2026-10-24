"""
LeetCode 7 - Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-2^31, 2^31 - 1], then return 0.

Solve this WITHOUT converting the integer to a string.

Example 1:
    Input:  x = 123
    Output: 321

Example 2:
    Input:  x = -123
    Output: -321

Example 3:
    Input:  x = 120
    Output: 21

Example 4:
    Input:  x = 0
    Output: 0

Constraints:
    - -2^31 <= x <= 2^31 - 1

Hint: Use modulo (%) to extract digits and multiplication to build
      the reversed number. Be careful with negative numbers in Python
      since % behaves differently than in some other languages.
"""


def reverse(x: int) -> int:
    pass


# Test cases
print(reverse(123))   # Expected: 321
print(reverse(-123))  # Expected: -321
print(reverse(120))   # Expected: 21
print(reverse(0))     # Expected: 0
