"""
LeetCode 352 - Data Stream as Disjoint Intervals

Given a data stream of integers, implement a class that:
    - add_num(value) -> adds the integer to the stream.
    - get_intervals() -> returns a summary of the integers seen so far
                         as a list of disjoint intervals [start, end],
                         sorted by start.

Example:
    ds = SummaryRanges()
    ds.add_num(1)      -> [[1,1]]
    ds.add_num(3)      -> [[1,1],[3,3]]
    ds.add_num(7)      -> [[1,1],[3,3],[7,7]]
    ds.add_num(2)      -> [[1,3],[7,7]]
    ds.add_num(6)      -> [[1,3],[6,7]]

Constraints:
    - 0 <= value <= 10^4
    - At most 3 * 10^4 calls total.

Hint: Use a sorted set/list or BST to maintain intervals. On add,
      check if the value merges with adjacent intervals.
"""


class SummaryRanges:

    def __init__(self):
        pass

    def add_num(self, value: int) -> None:
        pass

    def get_intervals(self) -> list[list[int]]:
        pass


ds = SummaryRanges()
ds.add_num(1); print(ds.get_intervals())   # Expected: [[1,1]]
ds.add_num(3); print(ds.get_intervals())   # Expected: [[1,1],[3,3]]
ds.add_num(7); print(ds.get_intervals())   # Expected: [[1,1],[3,3],[7,7]]
ds.add_num(2); print(ds.get_intervals())   # Expected: [[1,3],[7,7]]
ds.add_num(6); print(ds.get_intervals())   # Expected: [[1,3],[6,7]]
