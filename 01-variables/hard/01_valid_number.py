"""
LeetCode 65 - Valid Number

Given a string s, return whether s is a valid number.

A valid number can be split into these components (in order):
    1. (Optional) A sign character ('+' or '-').
    2. One of the following:
       a. One or more digits, optionally followed by a '.' and
          zero or more digits.
       b. A '.' followed by one or more digits.
    3. (Optional) An 'e' or 'E', followed by an optional sign and
       one or more digits.

Examples of VALID numbers:
    "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
    "3e+7", "+6e-1", "53.5e93", "-123.456e789"

Examples of INVALID numbers:
    "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"

Example 1:
    Input:  s = "0"
    Output: True

Example 2:
    Input:  s = "e"
    Output: False

Example 3:
    Input:  s = "."
    Output: False

Constraints:
    - 1 <= len(s) <= 20
    - s consists of only English letters, digits, '+', '-', and '.'

Hint: Think about tracking state variables — has a digit appeared?
      Has a dot appeared? Has an 'e' appeared? Walk through the string
      character by character and validate transitions.
"""


def is_number(s: str) -> bool:
    pass


# Test cases
print(is_number("0"))             # Expected: True
print(is_number("e"))             # Expected: False
print(is_number("."))             # Expected: False
print(is_number("2e10"))          # Expected: True
print(is_number("-123.456e789"))  # Expected: True
print(is_number("99e2.5"))        # Expected: False
print(is_number("1a"))            # Expected: False
