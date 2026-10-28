"""
LeetCode 767 - Reorganize String

Given a string s, rearrange the characters so that no two adjacent
characters are the same. Return any valid rearrangement, or "" if
not possible.

Example 1:
    Input:  s = "aab"
    Output: "aba"

Example 2:
    Input:  s = "aaab"
    Output: ""

Constraints:
    - 1 <= len(s) <= 500

Hint: Use a max-heap. Always place the most frequent character that
      isn't the same as the last placed character.
"""

import heapq
from collections import Counter


def reorganize_string(s: str) -> str:
    pass


result1 = reorganize_string("aab")
print(result1)  # Expected: "aba" (or any valid arrangement)

result2 = reorganize_string("aaab")
print(result2)  # Expected: ""
