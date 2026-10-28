"""
LeetCode 301 - Remove Invalid Parentheses

Given a string s containing parentheses and letters, remove the
minimum number of invalid parentheses to make it valid. Return all
possible results (no duplicates).

Example 1:
    Input:  s = "()())()"
    Output: ["(())()","()()()"]

Example 2:
    Input:  s = "(a)())()"
    Output: ["(a())()","(a)()()"]

Example 3:
    Input:  s = ")("
    Output: [""]

Constraints:
    - 1 <= len(s) <= 25

Hint: Count minimum removals needed (extra open/close). Then
      backtrack, trying to remove each '(' or ')' and pruning
      duplicates. Or use BFS level-by-level.
"""


def remove_invalid_parentheses(s: str) -> list[str]:
    pass


print(remove_invalid_parentheses("()())()"))    # Expected: ["(())()","()()()"]
print(remove_invalid_parentheses("(a)())()"))   # Expected: ["(a())()","(a)()()"]
print(remove_invalid_parentheses(")("))          # Expected: [""]
