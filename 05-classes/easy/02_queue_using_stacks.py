"""
LeetCode 232 - Implement Queue using Stacks

Implement a first-in-first-out (FIFO) queue using only two stacks.

The implemented queue should support:
    - push(x)  -> Pushes element x to the back of the queue.
    - pop()    -> Removes and returns the element from the front.
    - peek()   -> Returns the element at the front.
    - empty()  -> Returns True if the queue is empty, False otherwise.

You must use ONLY standard stack operations:
    push to top, peek/pop from top, size, and is empty.

Example:
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.peek()    # -> 1
    queue.pop()     # -> 1
    queue.empty()   # -> False

Constraints:
    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, peek, and empty.
    - All calls to pop and peek are valid (queue is not empty).

Hint: Use one stack for pushing and another for popping. Transfer
      elements between them when needed.
"""


class MyQueue:

    def __init__(self):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        pass


# Test cases
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())   # Expected: 1
print(queue.pop())    # Expected: 1
print(queue.empty())  # Expected: False
