"""
LeetCode 146 - LRU Cache

Design a data structure that follows the constraints of a Least
Recently Used (LRU) cache.

Implement the LRUCache class:
    - LRUCache(capacity)  -> Initialize with positive capacity.
    - get(key)            -> Return the value of key if it exists,
                             otherwise return -1.
    - put(key, value)     -> Update or insert the value. If the
                             number of keys exceeds the capacity,
                             evict the least recently used key.

Both get and put must run in O(1) average time.

Example:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # -> 1
    cache.put(3, 3)    # evicts key 2
    cache.get(2)       # -> -1
    cache.put(4, 4)    # evicts key 1
    cache.get(1)       # -> -1
    cache.get(3)       # -> 3
    cache.get(4)       # -> 4

Constraints:
    - 1 <= capacity <= 3000
    - 0 <= key <= 10^4
    - 0 <= value <= 10^5
    - At most 2 * 10^5 calls will be made.

Hint: Use a dictionary + doubly linked list. The dict gives O(1)
      lookup, and the linked list gives O(1) insertion/removal for
      maintaining access order.
"""


class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# Test cases
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # Expected: 1
cache.put(3, 3)
print(cache.get(2))    # Expected: -1
cache.put(4, 4)
print(cache.get(1))    # Expected: -1
print(cache.get(3))    # Expected: 3
print(cache.get(4))    # Expected: 4
