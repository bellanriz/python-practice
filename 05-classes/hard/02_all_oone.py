"""
LeetCode 432 - All O`one Data Structure

Design a data structure to store the count of strings.

Implement the AllOne class:
    - AllOne()       -> Initializes the object.
    - inc(key)       -> Increments the count of string key by 1. If
                        key doesn't exist, insert it with count 1.
    - dec(key)       -> Decrements the count of string key by 1. If
                        the count reaches 0, remove it.
    - get_max_key()  -> Returns one of the keys with the maximal count.
                        If no element exists, return "".
    - get_min_key()  -> Returns one of the keys with the minimal count.
                        If no element exists, return "".

Each function must run in O(1) average time.

Example:
    ao = AllOne()
    ao.inc("hello")
    ao.inc("hello")
    ao.get_max_key()   # -> "hello"
    ao.get_min_key()   # -> "hello"
    ao.inc("leet")
    ao.get_max_key()   # -> "hello"
    ao.get_min_key()   # -> "leet"

Constraints:
    - 1 <= len(key) <= 10
    - key consists of lowercase English letters.
    - It is guaranteed that dec is called on an existing key.
    - At most 5 * 10^4 calls total.

Hint: Use a doubly-linked list of "buckets" (each bucket holds a count
      and the set of keys with that count) + a dict from key to its
      bucket node.
"""


class AllOne:

    def __init__(self):
        pass

    def inc(self, key: str) -> None:
        pass

    def dec(self, key: str) -> None:
        pass

    def get_max_key(self) -> str:
        pass

    def get_min_key(self) -> str:
        pass


# Test cases
ao = AllOne()
ao.inc("hello")
ao.inc("hello")
print(ao.get_max_key())  # Expected: "hello"
print(ao.get_min_key())  # Expected: "hello"
ao.inc("leet")
print(ao.get_max_key())  # Expected: "hello"
print(ao.get_min_key())  # Expected: "leet"
