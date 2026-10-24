"""
LeetCode 224 - Basic Calculator

Given a string s representing a valid expression, implement a basic
calculator to evaluate it, and return the result of the evaluation.

The expression string may contain:
    - '+' and '-' operators
    - '(' and ')' parentheses
    - ' ' spaces
    - Non-negative integers

Note: You are NOT allowed to use any built-in function which evaluates
strings as mathematical expressions, such as eval().

Example 1:
    Input:  s = "1 + 1"
    Output: 2

Example 2:
    Input:  s = " 2-1 + 2 "
    Output: 3

Example 3:
    Input:  s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

Constraints:
    - 1 <= len(s) <= 3 * 10^5
    - s consists of digits, '+', '-', '(', ')', and ' '.
    - s represents a valid expression.
    - '+' is NOT used as a unary operation (i.e., "+1" won't appear)
    - '-' CAN be used as a unary operation (i.e., "-1" is valid)
    - No two consecutive operators in the input.

Hint: Use a stack to handle parentheses. Track the current sign.
"""


def calculate(s: str) -> int:
    pass


# Test cases
print(calculate("1 + 1"))                    # Expected: 2
print(calculate(" 2-1 + 2 "))               # Expected: 3
print(calculate("(1+(4+5+2)-3)+(6+8)"))     # Expected: 23
