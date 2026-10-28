"""
LeetCode 282 - Expression Add Operators

Given a string num (digits only) and an integer target, add the
binary operators +, -, or * between the digits so that the
expression evaluates to target. Return all such expressions.

Example 1:
    Input:  num = "123", target = 6
    Output: ["1+2+3","1*2*3"]

Example 2:
    Input:  num = "232", target = 8
    Output: ["2+3*2","2*3+2"]

Example 3:
    Input:  num = "3456237490", target = 9191
    Output: []

Constraints:
    - 1 <= len(num) <= 10
    - -2^31 <= target <= 2^31 - 1

Hint: Backtrack at each position, try all splits. Track the last
      operand for correct multiplication precedence.
"""


def add_operators(num: str, target: int) -> list[str]:
    pass


print(add_operators("123", 6))           # Expected: ["1+2+3","1*2*3"]
print(add_operators("232", 8))           # Expected: ["2+3*2","2*3+2"]
print(add_operators("3456237490", 9191)) # Expected: []
