"""
LeetCode 706 - Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
    - MyHashMap()        -> initializes with an empty map.
    - put(key, value)    -> inserts a (key, value) pair. If the key
                            already exists, update the value.
    - get(key)           -> returns the value mapped to key, or -1
                            if the key doesn't exist.
    - remove(key)        -> removes the key and its value if it exists.

Example:
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    hm.get(1)       # -> 1
    hm.get(3)       # -> -1
    hm.put(2, 1)    # update key 2's value to 1
    hm.get(2)       # -> 1
    hm.remove(2)
    hm.get(2)       # -> -1

Constraints:
    - 0 <= key, value <= 10^6
    - At most 10^4 calls will be made.

Hint: Use an array of buckets with chaining (linked list or list)
      to handle collisions. Choose a reasonable bucket size.
"""


class MyHashMap:

    def __init__(self):
        pass

    def put(self, key: int, value: int) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def remove(self, key: int) -> None:
        pass


# Test cases
hm = MyHashMap()
hm.put(1, 1)
hm.put(2, 2)
print(hm.get(1))    # Expected: 1
print(hm.get(3))    # Expected: -1
hm.put(2, 1)
print(hm.get(2))    # Expected: 1
hm.remove(2)
print(hm.get(2))    # Expected: -1
