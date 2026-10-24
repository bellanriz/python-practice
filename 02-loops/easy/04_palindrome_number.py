"""
LeetCode 9 - Palindrome Number

Given an integer x, return True if x is a palindrome, and False otherwise.
A palindrome reads the same forward and backward.

Solve this using a loop (do NOT convert to string).

Example 1:
    Input:  x = 121
    Output: True
    Explanation: 121 reads as 121 from left to right and right to left.

Example 2:
    Input:  x = -121
    Output: False
    Explanation: From left to right it reads -121. From right to left
                 it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input:  x = 10
    Output: False
    Explanation: Reads 01 from right to left. Not a palindrome.

Constraints:
    - -2^31 <= x <= 2^31 - 1
"""


def is_palindrome(x: int) -> bool:
    pass


# Test cases
print(is_palindrome(121))    # Expected: True
print(is_palindrome(-121))   # Expected: False
print(is_palindrome(10))     # Expected: False
