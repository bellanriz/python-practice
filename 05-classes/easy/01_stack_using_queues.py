"""
LeetCode 225 - Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues.

The implemented stack should support:
    - push(x)  -> Pushes element x to the top of the stack.
    - pop()    -> Removes and returns the element on the top.
    - top()    -> Returns the element on the top.
    - empty()  -> Returns True if the stack is empty, False otherwise.

You must use ONLY standard queue operations:
    push to back, peek/pop from front, size, and is empty.

Example:
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.top()     # -> 2
    stack.pop()     # -> 2
    stack.empty()   # -> False

Constraints:
    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, top, and empty.
    - All calls to pop and top are valid (stack is not empty).
"""

from collections import deque


class MyStack:

    def __init__(self):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def empty(self) -> bool:
        pass


# Test cases
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Expected: 2
print(stack.pop())    # Expected: 2
print(stack.empty())  # Expected: False
