"""
LeetCode 48 - Rotate Image

You are given an n x n 2D matrix representing an image. Rotate the
image by 90 degrees clockwise. You must do this in-place.

Example 1:
    Input:  matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
    Output: [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]
            ]

Example 2:
    Input:  matrix = [
                [ 5,  1,  9, 11],
                [ 2,  4,  8, 10],
                [13,  3,  6,  7],
                [15, 14, 12, 16]
            ]
    Output: [
                [15, 13,  2,  5],
                [14,  3,  4,  1],
                [12,  6,  8,  9],
                [16,  7, 10, 11]
            ]

Constraints:
    - n == len(matrix) == len(matrix[i])
    - 1 <= n <= 20
    - -1000 <= matrix[i][j] <= 1000

Hint: A 90-degree clockwise rotation can be done in two steps:
      1. Transpose the matrix (swap rows and columns)
      2. Reverse each row
"""


def rotate(matrix: list[list[int]]) -> None:
    pass


# Test cases
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(m1)
print(m1)  # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(m2)
print(m2)  # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
