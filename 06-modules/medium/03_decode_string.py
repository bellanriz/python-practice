"""
LeetCode 394 - Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times.

You may assume the input is always valid (no extra spaces, brackets
are well-formed, etc.).

Example 1:
    Input:  s = "3[a]2[bc]"
    Output: "aaabcbc"

Example 2:
    Input:  s = "3[a2[c]]"
    Output: "accaccacc"

Example 3:
    Input:  s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

Constraints:
    - 1 <= len(s) <= 30
    - s consists of lowercase English letters, digits, '[', and ']'.
    - s is guaranteed to be a valid input.
    - 1 <= k <= 300

Module hint: Use a stack (collections.deque) to handle nested brackets.
             Alternatively, consider using re (regex) to repeatedly
             process innermost brackets.
"""

# You may use: from collections import deque
# You may use: import re


def decode_string(s: str) -> str:
    pass


# Test cases
print(decode_string("3[a]2[bc]"))      # Expected: "aaabcbc"
print(decode_string("3[a2[c]]"))       # Expected: "accaccacc"
print(decode_string("2[abc]3[cd]ef"))  # Expected: "abcabccdcdcdef"
