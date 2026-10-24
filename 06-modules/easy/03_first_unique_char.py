"""
LeetCode 387 - First Unique Character in a String

Given a string s, find the first non-repeating character in it and
return its index. If it does not exist, return -1.

Example 1:
    Input:  s = "leetcode"
    Output: 0
    Explanation: 'l' is the first character that appears only once.

Example 2:
    Input:  s = "loveleetcode"
    Output: 2
    Explanation: 'v' is the first unique character, at index 2.

Example 3:
    Input:  s = "aabb"
    Output: -1

Constraints:
    - 1 <= len(s) <= 10^5
    - s consists of only lowercase English letters.

Module hint: Use collections.Counter to count character frequencies
             in one pass, then scan again for the first with count 1.
"""

# You may use: from collections import Counter


def first_uniq_char(s: str) -> int:
    pass


# Test cases
print(first_uniq_char("leetcode"))       # Expected: 0
print(first_uniq_char("loveleetcode"))   # Expected: 2
print(first_uniq_char("aabb"))           # Expected: -1
