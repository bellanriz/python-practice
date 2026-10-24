"""
LeetCode 895 - Maximum Frequency Stack

Design a stack-like data structure that pushes elements and pops the
most frequent element. If there is a tie for most frequent, the
element closest to the top of the stack is popped.

Implement the FreqStack class:
    - FreqStack()   -> Initializes the object.
    - push(val)     -> Pushes val onto the stack.
    - pop()         -> Removes and returns the most frequent element.
                       If there is a tie, the element closest to the
                       top of the stack is removed and returned.

Example:
    fs = FreqStack()
    fs.push(5)   # stack: [5]
    fs.push(7)   # stack: [5, 7]
    fs.push(5)   # stack: [5, 7, 5]
    fs.push(7)   # stack: [5, 7, 5, 7]
    fs.push(4)   # stack: [5, 7, 5, 7, 4]
    fs.push(5)   # stack: [5, 7, 5, 7, 4, 5]
    fs.pop()     # -> 5 (freq 3, most frequent)
    fs.pop()     # -> 7 (freq 2, tie with 5 but 7 was pushed later)
    fs.pop()     # -> 5 (freq 2)
    fs.pop()     # -> 4 (freq 1, most recent among freq 1)

Constraints:
    - 0 <= val <= 10^9
    - At most 2 * 10^4 calls total to push and pop.
    - There will be at least one element when pop is called.

Hint: Use a frequency map and a dict of stacks keyed by frequency.
      Track the current max frequency. When popping, pop from the
      stack at max frequency.
"""

from collections import defaultdict


class FreqStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass


# Test cases
fs = FreqStack()
fs.push(5)
fs.push(7)
fs.push(5)
fs.push(7)
fs.push(4)
fs.push(5)
print(fs.pop())  # Expected: 5
print(fs.pop())  # Expected: 7
print(fs.pop())  # Expected: 5
print(fs.pop())  # Expected: 4
