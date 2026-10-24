"""
LeetCode 73 - Set Matrix Zeroes

Given an m x n integer matrix, if an element is 0, set its entire
row and column to 0's. You must do it in-place.

Example 1:
    Input:  matrix = [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ]
    Output: [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]
            ]

Example 2:
    Input:  matrix = [
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]
            ]
    Output: [
                [0, 0, 0, 0],
                [0, 4, 5, 0],
                [0, 3, 1, 0]
            ]

Constraints:
    - m == len(matrix)
    - n == len(matrix[0])
    - 1 <= m, n <= 200
    - -2^31 <= matrix[i][j] <= 2^31 - 1

Challenge: Can you solve it using O(1) extra space?
Hint: Use the first row and first column as markers.
"""


def set_zeroes(matrix: list[list[int]]) -> None:
    pass


# Test cases
m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_zeroes(m1)
print(m1)  # Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
set_zeroes(m2)
print(m2)  # Expected: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
