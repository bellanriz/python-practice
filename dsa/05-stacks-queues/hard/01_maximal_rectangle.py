"""
LeetCode 85 - Maximal Rectangle

Given a rows x cols binary matrix filled with '0's and '1's, find
the largest rectangle containing only '1's and return its area.

Example 1:
    Input:  matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
                      ["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 6

Example 2:
    Input:  matrix = [["0"]]
    Output: 0

Constraints:
    - 1 <= rows, cols <= 200

Hint: Build a histogram for each row and apply "Largest Rectangle
      in Histogram" (monotonic stack) on each row.
"""


def maximal_rectangle(matrix: list[list[str]]) -> int:
    pass


print(maximal_rectangle([
    ["1","0","1","0","0"],["1","0","1","1","1"],
    ["1","1","1","1","1"],["1","0","0","1","0"]
]))  # Expected: 6
print(maximal_rectangle([["0"]]))  # Expected: 0
