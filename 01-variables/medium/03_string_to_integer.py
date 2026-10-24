"""
LeetCode 8 - String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a
32-bit signed integer.

The algorithm:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character is '-' or '+'. Read it if it is.
       This determines if the final result is negative or positive.
       Assume positive if neither is present.
    3. Read in the next characters until a non-digit character is
       reached or end of input. Ignore the rest of the string.
    4. Convert these digits into an integer. If no digits were read,
       the integer is 0.
    5. Clamp the integer to the 32-bit signed range:
       [-2^31, 2^31 - 1]. That is [-2147483648, 2147483647].

Example 1:
    Input:  s = "42"
    Output: 42

Example 2:
    Input:  s = "   -042"
    Output: -42

Example 3:
    Input:  s = "1337c0d3"
    Output: 1337

Example 4:
    Input:  s = "0-1"
    Output: 0
    Explanation: Reading stops at '-' since it's not a digit.

Example 5:
    Input:  s = "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', not a digit.

Constraints:
    - 0 <= len(s) <= 200
    - s consists of English letters, digits, ' ', '+', '-', '.'
"""


def my_atoi(s: str) -> int:
    pass


# Test cases
print(my_atoi("42"))            # Expected: 42
print(my_atoi("   -042"))       # Expected: -42
print(my_atoi("1337c0d3"))      # Expected: 1337
print(my_atoi("0-1"))           # Expected: 0
print(my_atoi("words and 987")) # Expected: 0
