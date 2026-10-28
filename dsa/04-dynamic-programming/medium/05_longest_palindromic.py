"""
LeetCode 5 - Longest Palindromic Substring

Given a string s, return the longest palindromic substring.

Example 1:
    Input:  s = "babad"
    Output: "bab" (or "aba")

Example 2:
    Input:  s = "cbbd"
    Output: "bb"

Constraints:
    - 1 <= len(s) <= 1000

Hint: Expand around center for each index (both odd and even length).
      Or use 2D DP: dp[i][j] = True if s[i..j] is palindrome.
"""


def longest_palindrome(s: str) -> str:
    pass


print(longest_palindrome("babad"))  # Expected: "bab" or "aba"
print(longest_palindrome("cbbd"))   # Expected: "bb"
