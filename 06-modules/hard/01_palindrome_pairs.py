"""
LeetCode 336 - Palindrome Pairs

You are given a list of unique strings words. Return all the pairs of
distinct indices (i, j) such that the concatenation of words[i] + words[j]
is a palindrome.

Example 1:
    Input:  words = ["abcd", "dcba", "lls", "s", "sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation:
        "abcd" + "dcba" = "abcddcba" (palindrome)
        "dcba" + "abcd" = "dcbaabcd" (palindrome)
        "s" + "lls"     = "slls"     (palindrome)
        "lls" + "sssll" = "llssssll" (palindrome)

Example 2:
    Input:  words = ["bat", "tab", "cat"]
    Output: [[0,1],[1,0]]

Example 3:
    Input:  words = ["a", ""]
    Output: [[0,1],[1,0]]

Constraints:
    - 1 <= len(words) <= 5000
    - 0 <= len(words[i]) <= 300
    - words[i] consists of lowercase English letters.

Module hint: Use a dictionary (or collections.defaultdict) to map
             reversed words to their indices. For each word, check
             all possible splits where one part is a palindrome.
"""

# You may use: from collections import defaultdict


def palindrome_pairs(words: list[str]) -> list[list[int]]:
    pass


# Test cases
print(palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"]))
# Expected: [[0,1],[1,0],[3,2],[2,4]] (order may vary)

print(palindrome_pairs(["bat", "tab", "cat"]))
# Expected: [[0,1],[1,0]]

print(palindrome_pairs(["a", ""]))
# Expected: [[0,1],[1,0]]
