"""
LeetCode 844 - Backspace String Compare

Given two strings s and t, return True if they are equal when both
are typed into empty text editors. '#' means a backspace character.

Example 1:
    Input:  s = "ab#c", t = "ad#c"
    Output: True  (both become "ac")

Example 2:
    Input:  s = "ab##", t = "c#d#"
    Output: True  (both become "")

Example 3:
    Input:  s = "a#c", t = "b"
    Output: False

Constraints:
    - 1 <= len(s), len(t) <= 200

Challenge: Can you solve it in O(1) space? (Walk backwards with two pointers)
"""


def backspace_compare(s: str, t: str) -> bool:
    pass


print(backspace_compare("ab#c", "ad#c"))  # Expected: True
print(backspace_compare("ab##", "c#d#"))  # Expected: True
print(backspace_compare("a#c", "b"))       # Expected: False
