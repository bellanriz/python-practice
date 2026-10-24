"""
LeetCode 2011 - Final Value of Variable After Performing Operations

There is a programming language with only four operations and one
variable X:
    - ++X and X++ increments the value of X by 1
    - --X and X-- decrements the value of X by 1

Given a list of operations, return the final value of X starting
from 0.

Example 1:
    Input:  operations = ["--X", "X++", "X++"]
    Output: 1
    Explanation: X starts at 0.
        --X: X = 0 - 1 = -1
        X++: X = -1 + 1 = 0
        X++: X = 0 + 1 = 1

Example 2:
    Input:  operations = ["++X", "++X", "X++"]
    Output: 3

Example 3:
    Input:  operations = ["X++", "++X", "--X", "X--"]
    Output: 0

Constraints:
    - 1 <= len(operations) <= 100
    - operations[i] will be either "++X", "X++", "--X", or "X--"
"""


def final_value_after_operations(operations: list[str]) -> int:
    pass


# Test cases
print(final_value_after_operations(["--X", "X++", "X++"]))          # Expected: 1
print(final_value_after_operations(["++X", "++X", "X++"]))          # Expected: 3
print(final_value_after_operations(["X++", "++X", "--X", "X--"]))   # Expected: 0
