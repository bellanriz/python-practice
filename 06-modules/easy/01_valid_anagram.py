"""
LeetCode 242 - Valid Anagram

Given two strings s and t, return True if t is an anagram of s,
and False otherwise.

An anagram uses the exact same characters with the same frequencies.

Example 1:
    Input:  s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input:  s = "rat", t = "car"
    Output: False

Constraints:
    - 1 <= len(s), len(t) <= 5 * 10^4
    - s and t consist of lowercase English letters.

Module hint: Consider using collections.Counter or collections.defaultdict.

Challenge: Can you solve it using only a fixed-size array (26 letters)?
"""

# You may use: from collections import Counter, defaultdict


def is_anagram(s: str, t: str) -> bool:
    pass


# Test cases
print(is_anagram("anagram", "nagaram"))  # Expected: True
print(is_anagram("rat", "car"))          # Expected: False
