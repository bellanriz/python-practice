"""
LeetCode 131 - Palindrome Partitioning

Given a string s, partition s such that every substring of the
partition is a palindrome. Return all possible palindrome partitionings.

Example 1:
    Input:  s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input:  s = "a"
    Output: [["a"]]

Constraints:
    - 1 <= len(s) <= 16

Hint: Backtracking. At each position, try all substrings starting
      there. If it's a palindrome, recurse on the remainder.
"""


def partition(s: str) -> list[list[str]]:
    pass


print(partition("aab"))  # Expected: [["a","a","b"],["aa","b"]]
print(partition("a"))     # Expected: [["a"]]
