"""
LeetCode 622 - Design Circular Queue

Design a circular queue with these operations:
    - MyCircularQueue(k)  -> Constructor, set size to k.
    - enQueue(value)      -> Insert element. Return True if success.
    - deQueue()           -> Delete element. Return True if success.
    - Front()             -> Get the front item. Return -1 if empty.
    - Rear()              -> Get the last item. Return -1 if empty.
    - isEmpty()           -> Check whether queue is empty.
    - isFull()            -> Check whether queue is full.

Example:
    q = MyCircularQueue(3)
    q.enQueue(1)    # True
    q.enQueue(2)    # True
    q.enQueue(3)    # True
    q.enQueue(4)    # False (full)
    q.Rear()        # 3
    q.isFull()      # True
    q.deQueue()     # True
    q.enQueue(4)    # True
    q.Rear()        # 4

Constraints:
    - 1 <= k <= 1000
    - 0 <= value <= 1000

Hint: Use a fixed-size array with head/tail pointers and a count.
"""


class MyCircularQueue:

    def __init__(self, k: int):
        pass

    def enQueue(self, value: int) -> bool:
        pass

    def deQueue(self) -> bool:
        pass

    def Front(self) -> int:
        pass

    def Rear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass


q = MyCircularQueue(3)
print(q.enQueue(1))  # True
print(q.enQueue(2))  # True
print(q.enQueue(3))  # True
print(q.enQueue(4))  # False
print(q.Rear())      # 3
print(q.isFull())    # True
print(q.deQueue())   # True
print(q.enQueue(4))  # True
print(q.Rear())      # 4
