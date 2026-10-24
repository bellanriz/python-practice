"""
LeetCode 295 - Find Median from Data Stream

The median is the middle value in an ordered integer list. If the list
has an even number of elements, the median is the average of the two
middle values.

Implement the MedianFinder class:
    - MedianFinder()     -> initializes the object.
    - add_num(num: int)  -> adds the integer num to the data structure.
    - find_median()      -> returns the median of all elements so far.

Example:
    mf = MedianFinder()
    mf.add_num(1)        # list: [1]
    mf.add_num(2)        # list: [1, 2]
    mf.find_median()     # -> 1.5
    mf.add_num(3)        # list: [1, 2, 3]
    mf.find_median()     # -> 2.0

Constraints:
    - -10^5 <= num <= 10^5
    - There will be at least one element before calling find_median.
    - At most 5 * 10^4 calls total to add_num and find_median.

Hint: Use two heaps — a max-heap for the lower half and a min-heap
      for the upper half. Keep them balanced so the median is always
      at the top of one or both heaps.
"""

import heapq


class MedianFinder:

    def __init__(self):
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


# Test cases
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())   # Expected: 1.5
mf.add_num(3)
print(mf.find_median())   # Expected: 2.0
