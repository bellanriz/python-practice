"""
LeetCode 56 - Merge Intervals

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals and return a list of non-overlapping
intervals that cover all the intervals in the input.

Example 1:
    Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: [1,3] and [2,6] overlap, so merge them into [1,6].

Example 2:
    Input:  intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: [1,4] and [4,5] are considered overlapping.

Constraints:
    - 1 <= len(intervals) <= 10^4
    - intervals[i].length == 2
    - 0 <= start_i <= end_i <= 10^4

Hint: Sort the intervals by their start time first, then iterate
      and merge when overlapping.
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    pass


# Test cases
print(merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected: [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                  # Expected: [[1,5]]
