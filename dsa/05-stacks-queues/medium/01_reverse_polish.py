"""
LeetCode 150 - Evaluate Reverse Polish Notation

Evaluate an arithmetic expression in Reverse Polish Notation (postfix).
Valid operators are +, -, *, /. Division truncates toward zero.

Example 1:
    Input:  tokens = ["2","1","+","3","*"]
    Output: 9  ((2+1)*3)

Example 2:
    Input:  tokens = ["4","13","5","/","+"]
    Output: 6  (4+(13/5) = 4+2)

Example 3:
    Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22

Constraints:
    - 1 <= len(tokens) <= 10^4

Hint: Use a stack. Push numbers, pop two when you see an operator.
"""


def eval_rpn(tokens: list[str]) -> int:
    pass


print(eval_rpn(["2","1","+","3","*"]))       # Expected: 9
print(eval_rpn(["4","13","5","/","+"]))      # Expected: 6
print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Expected: 22
