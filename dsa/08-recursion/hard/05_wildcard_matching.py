"""
LeetCode 44 - Wildcard Matching

Given an input string s and a pattern p, implement wildcard matching:
    - '?' matches any single character.
    - '*' matches any sequence of characters (including empty).

The matching should cover the entire input string.

Example 1:
    Input:  s = "aa", p = "a"
    Output: False

Example 2:
    Input:  s = "aa", p = "*"
    Output: True

Example 3:
    Input:  s = "cb", p = "?a"
    Output: False

Example 4:
    Input:  s = "adceb", p = "*a*b"
    Output: True

Constraints:
    - 0 <= len(s), len(p) <= 2000

Hint: Recursion with memoization, or 2D DP.
      dp[i][j] = does s[0:i] match p[0:j]?
"""

from functools import lru_cache


def is_match(s: str, p: str) -> bool:
    pass


print(is_match("aa", "a"))       # Expected: False
print(is_match("aa", "*"))       # Expected: True
print(is_match("cb", "?a"))      # Expected: False
print(is_match("adceb", "*a*b")) # Expected: True
