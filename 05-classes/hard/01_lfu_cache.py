"""
LeetCode 460 - LFU Cache

Design and implement a data structure for a Least Frequently Used
(LFU) cache.

Implement the LFUCache class:
    - LFUCache(capacity)  -> Initialize with positive capacity.
    - get(key)            -> Get the value of key if it exists,
                             otherwise return -1.
    - put(key, value)     -> Update or insert the value. When the
                             cache reaches capacity, invalidate and
                             remove the least frequently used key
                             before inserting. If there is a tie
                             (same frequency), the least recently
                             used key is evicted.

Both get and put must run in O(1) average time.

Example:
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # -> 1 (freq of key 1 increases to 2)
    cache.put(3, 3)    # evicts key 2 (freq 1, least recently used)
    cache.get(2)       # -> -1
    cache.get(3)       # -> 3
    cache.put(4, 4)    # evicts key 1 (freq 2) vs key 3 (freq 2)
                       # -> evicts key 3 (least recently used among freq 2)
    cache.get(1)       # -> -1 -- Wait, let me recalculate...
    # Actually: after get(3), key 1 has freq 2, key 3 has freq 2.
    # put(4,4) evicts the LRU among freq-2 keys. key 1 was used first -> evict key 1.
    cache.get(1)       # -> -1
    cache.get(3)       # -> -1 -- actually key 3 was used more recently... 
    # Let me just show the standard LC example:

    # Standard example:
    lfu = LFUCache(2)
    lfu.put(1, 1)      # cache: {1: 1}
    lfu.put(2, 2)      # cache: {1: 1, 2: 2}
    lfu.get(1)          # -> 1, cache: {1: 1, 2: 2} (freq1=2, freq2=1)
    lfu.put(3, 3)       # evicts key 2, cache: {1: 1, 3: 3}
    lfu.get(2)          # -> -1
    lfu.get(3)          # -> 3
    lfu.put(4, 4)       # evicts key 1, cache: {3: 3, 4: 4}
    lfu.get(1)          # -> -1
    lfu.get(3)          # -> 3
    lfu.get(4)          # -> 4

Constraints:
    - 1 <= capacity <= 10^4
    - 0 <= key <= 10^5
    - 0 <= value <= 10^9
    - At most 2 * 10^5 calls to get and put.

Hint: Use a dict for key->value, a dict for key->freq, and a dict
      mapping freq->OrderedDict (or doubly-linked-list). Track min_freq.
"""

from collections import OrderedDict, defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# Test cases
lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))    # Expected: 1
lfu.put(3, 3)
print(lfu.get(2))    # Expected: -1
print(lfu.get(3))    # Expected: 3
lfu.put(4, 4)
print(lfu.get(1))    # Expected: -1
print(lfu.get(3))    # Expected: 3
print(lfu.get(4))    # Expected: 4
