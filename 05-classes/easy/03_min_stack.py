"""
LeetCode 155 - Min Stack

Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time.

Implement the MinStack class:
    - MinStack()   -> initializes the stack object.
    - push(val)    -> pushes the element val onto the stack.
    - pop()        -> removes the element on the top of the stack.
    - top()        -> gets the top element of the stack.
    - get_min()    -> retrieves the minimum element in the stack.

Each function must run in O(1) time.

Example:
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    ms.get_min()   # -> -3
    ms.pop()
    ms.top()       # -> 0
    ms.get_min()   # -> -2

Constraints:
    - -2^31 <= val <= 2^31 - 1
    - pop, top, and get_min will always be called on non-empty stacks.
    - At most 3 * 10^4 calls will be made.

Hint: Use an auxiliary stack that tracks the current minimum at each level.
"""


class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass


# Test cases
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.get_min())  # Expected: -3
ms.pop()
print(ms.top())      # Expected: 0
print(ms.get_min())  # Expected: -2
