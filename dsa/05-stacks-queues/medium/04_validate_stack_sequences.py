"""
LeetCode 946 - Validate Stack Sequences

Given two integer arrays pushed and popped (both with distinct values),
return True if this could have been the result of push/pop operations
on an initially empty stack.

Example 1:
    Input:  pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: True
    Explanation: push(1,2,3,4), pop(4), push(5), pop(5,3,2,1)

Example 2:
    Input:  pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    Output: False

Constraints:
    - 1 <= len(pushed) <= 1000
    - pushed and popped are permutations of each other.

Hint: Simulate with a stack. Push elements, and pop whenever the stack
      top matches the next expected popped element.
"""


def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    pass


print(validate_stack_sequences([1,2,3,4,5], [4,5,3,2,1]))  # Expected: True
print(validate_stack_sequences([1,2,3,4,5], [4,3,5,1,2]))  # Expected: False
