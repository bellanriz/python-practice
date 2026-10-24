"""
LeetCode 10 - Regular Expression Matching

Given an input string s and a pattern p, implement regular expression
matching with support for '.' and '*' where:
    - '.' matches any single character.
    - '*' matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
    Input:  s = "aa", p = "a"
    Output: False
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input:  s = "aa", p = "a*"
    Output: True
    Explanation: '*' means zero or more of 'a'. "a*" -> "aa".

Example 3:
    Input:  s = "ab", p = ".*"
    Output: True
    Explanation: ".*" means zero or more of any character.

Example 4:
    Input:  s = "aab", p = "c*a*b"
    Output: True
    Explanation: c* = "", a* = "aa", b = "b" -> "aab"

Constraints:
    - 1 <= len(s) <= 20
    - 1 <= len(p) <= 20
    - s contains only lowercase English letters.
    - p contains only lowercase English letters, '.', and '*'.
    - It is guaranteed for each '*', there is a previous valid character to match.

Hint: Use dynamic programming or recursion with memoization.
      dp[i][j] = does s[0:i] match p[0:j]?
"""


def is_match(s: str, p: str) -> bool:
    pass


# Test cases
print(is_match("aa", "a"))      # Expected: False
print(is_match("aa", "a*"))     # Expected: True
print(is_match("ab", ".*"))     # Expected: True
print(is_match("aab", "c*a*b")) # Expected: True
