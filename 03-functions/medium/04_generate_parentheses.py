"""
LeetCode 22 - Generate Parentheses

Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

Example 1:
    Input:  n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input:  n = 1
    Output: ["()"]

Constraints:
    - 1 <= n <= 8

Hint: Use backtracking. Track the count of open and close parentheses.
      You can add '(' if open_count < n.
      You can add ')' if close_count < open_count.
"""


def generate_parenthesis(n: int) -> list[str]:
    pass


# Test cases
print(generate_parenthesis(3))  # Expected: ["((()))","(()())","(())()","()(())","()()()"]
print(generate_parenthesis(1))  # Expected: ["()"]
