"""
LeetCode 32 - Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the
length of the longest valid (well-formed) parentheses substring.

Example 1:
    Input:  s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".

Example 2:
    Input:  s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".

Example 3:
    Input:  s = ""
    Output: 0

Constraints:
    - 0 <= len(s) <= 3 * 10^4
    - s[i] is '(' or ')'.

Hint: Multiple approaches work here:
      1. Stack-based: push indices onto a stack.
      2. Dynamic programming: dp[i] = length of longest valid
         substring ending at index i.
      3. Two-pass with counters (no extra space).
"""


def longest_valid_parentheses(s: str) -> int:
    pass


# Test cases
print(longest_valid_parentheses("(()"))      # Expected: 2
print(longest_valid_parentheses(")()())"))   # Expected: 4
print(longest_valid_parentheses(""))          # Expected: 0
