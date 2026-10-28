"""
LeetCode 72 - Edit Distance

Given two strings word1 and word2, return the minimum number of
operations required to convert word1 into word2.
Operations: insert, delete, or replace a character.

Example 1:
    Input:  word1 = "horse", word2 = "ros"
    Output: 3  (horse->rorse->rose->ros)

Example 2:
    Input:  word1 = "intention", word2 = "execution"
    Output: 5

Constraints:
    - 0 <= len(word1), len(word2) <= 500

Hint: 2D DP. dp[i][j] = min operations for word1[0:i] -> word2[0:j].
"""


def min_distance(word1: str, word2: str) -> int:
    pass


print(min_distance("horse", "ros"))            # Expected: 3
print(min_distance("intention", "execution"))  # Expected: 5
