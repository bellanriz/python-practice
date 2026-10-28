"""
LeetCode 344 - Reverse String

Write a function that reverses a string in-place. The input is given
as a list of characters. You must do this with O(1) extra memory.

Example 1:
    Input:  s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input:  s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Constraints:
    - 1 <= len(s) <= 10^5

Challenge: Solve recursively using two-pointer approach.
"""


def reverse_string(s: list[str]) -> None:
    pass


s1 = ["h","e","l","l","o"]
reverse_string(s1)
print(s1)  # Expected: ["o","l","l","e","h"]

s2 = ["H","a","n","n","a","h"]
reverse_string(s2)
print(s2)  # Expected: ["h","a","n","n","a","H"]
