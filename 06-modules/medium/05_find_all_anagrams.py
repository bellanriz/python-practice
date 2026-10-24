"""
LeetCode 438 - Find All Anagrams in a String

Given two strings s and p, return a list of all the start indices of
p's anagrams in s. You may return the answer in any order.

An anagram is a rearrangement of all characters of a word.

Example 1:
    Input:  s = "cbaebabacd", p = "abc"
    Output: [0, 6]
    Explanation:
        Index 0: "cba" is an anagram of "abc"
        Index 6: "bac" is an anagram of "abc"

Example 2:
    Input:  s = "abab", p = "ab"
    Output: [0, 1, 2]
    Explanation:
        Index 0: "ab" is an anagram of "ab"
        Index 1: "ba" is an anagram of "ab"
        Index 2: "ab" is an anagram of "ab"

Constraints:
    - 1 <= len(s), len(p) <= 3 * 10^4
    - s and p consist of lowercase English letters.

Module hint: Use collections.Counter to count character frequencies.
             Use a sliding window of size len(p) and compare counters
             as you slide across s.
"""

# You may use: from collections import Counter


def find_anagrams(s: str, p: str) -> list[int]:
    pass


# Test cases
print(find_anagrams("cbaebabacd", "abc"))  # Expected: [0, 6]
print(find_anagrams("abab", "ab"))          # Expected: [0, 1, 2]
