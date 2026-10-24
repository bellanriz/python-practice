"""
LeetCode 1146 - Snapshot Array

Implement a SnapshotArray that supports the following interface:
    - SnapshotArray(length)  -> Initializes with the given length.
                                Initially all elements are 0.
    - set(index, val)        -> Sets the element at index to val.
    - snap()                 -> Takes a snapshot and returns the
                                snap_id (number of times snap was
                                called minus 1).
    - get(index, snap_id)    -> Returns the value at index at the
                                time the snapshot with snap_id was taken.

Example:
    sa = SnapshotArray(3)   # [0, 0, 0]
    sa.set(0, 5)            # [5, 0, 0]
    sa.snap()               # -> 0 (snap_id = 0)
    sa.set(0, 6)            # [6, 0, 0]
    sa.get(0, 0)            # -> 5 (value at snap_id 0)

Constraints:
    - 1 <= length <= 5 * 10^4
    - 0 <= index < length
    - 0 <= val <= 10^9
    - 0 <= snap_id < (number of times snap() was called)
    - At most 5 * 10^4 calls total.

Hint: Don't copy the entire array on every snap (too slow). Instead,
      for each index, store a list of (snap_id, value) pairs. Use
      binary search on get() to find the correct snapshot.
"""

import bisect


class SnapshotArray:

    def __init__(self, length: int):
        pass

    def set(self, index: int, val: int) -> None:
        pass

    def snap(self) -> int:
        pass

    def get(self, index: int, snap_id: int) -> int:
        pass


# Test cases
sa = SnapshotArray(3)
sa.set(0, 5)
print(sa.snap())       # Expected: 0
sa.set(0, 6)
print(sa.get(0, 0))   # Expected: 5
