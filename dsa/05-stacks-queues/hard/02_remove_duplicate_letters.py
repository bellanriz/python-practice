"""
LeetCode 316 - Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter
appears once and only once. The result must be the smallest in
lexicographical order among all possible results.

Example 1:
    Input:  s = "bcabc"
    Output: "abc"

Example 2:
    Input:  s = "cbacdcbc"
    Output: "acdb"

Constraints:
    - 1 <= len(s) <= 10^4
    - s consists of lowercase English letters.

Hint: Use a monotonic stack. For each character, pop from stack if
      stack top is greater AND appears later in the string.
"""


def remove_duplicate_letters(s: str) -> str:
    pass


print(remove_duplicate_letters("bcabc"))     # Expected: "abc"
print(remove_duplicate_letters("cbacdcbc"))  # Expected: "acdb"
