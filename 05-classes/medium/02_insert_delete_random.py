"""
LeetCode 380 - Insert Delete GetRandom O(1)

Implement the RandomizedSet class:
    - RandomizedSet()    -> Initializes the object.
    - insert(val)        -> Inserts val if not present. Returns True
                            if it was not present, False otherwise.
    - remove(val)        -> Removes val if present. Returns True if
                            it was present, False otherwise.
    - get_random()       -> Returns a random element from the current
                            set. Each element must have the same
                            probability of being returned.

Each function must run in O(1) average time.

Example:
    rs = RandomizedSet()
    rs.insert(1)         # -> True
    rs.remove(2)         # -> False (2 not in set)
    rs.insert(2)         # -> True
    rs.get_random()      # -> 1 or 2 randomly
    rs.remove(1)         # -> True
    rs.insert(2)         # -> False (2 already in set)
    rs.get_random()      # -> 2

Constraints:
    - -2^31 <= val <= 2^31 - 1
    - At most 2 * 10^5 calls total.
    - There will be at least one element when get_random is called.

Hint: Use a list for O(1) random access + a dict mapping values to
      their indices. On removal, swap the target with the last element.
"""

import random


class RandomizedSet:

    def __init__(self):
        pass

    def insert(self, val: int) -> bool:
        pass

    def remove(self, val: int) -> bool:
        pass

    def get_random(self) -> int:
        pass


# Test cases
rs = RandomizedSet()
print(rs.insert(1))      # Expected: True
print(rs.remove(2))      # Expected: False
print(rs.insert(2))      # Expected: True
print(rs.get_random())   # Expected: 1 or 2
print(rs.remove(1))      # Expected: True
print(rs.insert(2))      # Expected: False
print(rs.get_random())   # Expected: 2
