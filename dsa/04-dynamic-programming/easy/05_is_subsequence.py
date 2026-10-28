"""
LeetCode 392 - Is Subsequence

Given two strings s and t, return True if s is a subsequence of t.
A subsequence is formed by deleting some (or no) characters without
changing the relative order.

Example 1:
    Input:  s = "abc", t = "ahbgdc"
    Output: True

Example 2:
    Input:  s = "axc", t = "ahbgdc"
    Output: False

Constraints:
    - 0 <= len(s) <= 100
    - 0 <= len(t) <= 10^4

Hint: Two pointers — one for s, one for t. Advance both when matched,
      only t's pointer when not matched.
"""


def is_subsequence(s: str, t: str) -> bool:
    pass


print(is_subsequence("abc", "ahbgdc"))  # Expected: True
print(is_subsequence("axc", "ahbgdc"))  # Expected: False
