"""
LeetCode 20 - Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

A string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.
    3. Every close bracket has a corresponding open bracket.

Example 1:
    Input:  s = "()"
    Output: True

Example 2:
    Input:  s = "()[]{}"
    Output: True

Example 3:
    Input:  s = "(]"
    Output: False

Example 4:
    Input:  s = "([])"
    Output: True

Constraints:
    - 1 <= len(s) <= 10^4
    - s consists of parentheses only: '()[]{}' 

Module hint: Consider using collections.deque as a stack for efficient
             append/pop operations.
"""

# You may use: from collections import deque


def is_valid(s: str) -> bool:
    pass


# Test cases
print(is_valid("()"))      # Expected: True
print(is_valid("()[]{}"))  # Expected: True
print(is_valid("(]"))      # Expected: False
print(is_valid("([])"))    # Expected: True
