"""
LeetCode 564 - Find the Closest Palindrome

Given a string n representing an integer, return the closest integer
(not including itself) which is a palindrome. If there is a tie,
return the smaller one.

The closest is defined as the absolute difference minimized between
two integers.

Example 1:
    Input:  n = "123"
    Output: "121"

Example 2:
    Input:  n = "1"
    Output: "0"

Example 3:
    Input:  n = "1000"
    Output: "999"

Constraints:
    - 1 <= len(n) <= 18
    - n does not have leading zeros.
    - n represents an integer in range [1, 10^18 - 1].

Hint: The closest palindrome is likely formed by mirroring the first
      half of the number. Consider candidates from mirroring (first half),
      (first half + 1), and (first half - 1). Also consider edge cases
      like 10...0 -> 9...9 and 9...9 -> 10...01.
"""


def nearest_palindromic(n: str) -> str:
    pass


# Test cases
print(nearest_palindromic("123"))   # Expected: "121"
print(nearest_palindromic("1"))     # Expected: "0"
print(nearest_palindromic("1000"))  # Expected: "999"
