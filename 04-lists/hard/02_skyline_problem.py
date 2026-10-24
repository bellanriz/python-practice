"""
LeetCode 218 - The Skyline Problem

A city's skyline is the outer contour formed by all the buildings
when viewed from a distance.

Given the locations and heights of all the buildings as
buildings[i] = [left_i, right_i, height_i], return the skyline
as a list of "key points" [x, height] sorted by x-coordinate.

A key point is where the skyline changes height.

Example 1:
    Input:  buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Example 2:
    Input:  buildings = [[0,2,3],[2,5,3]]
    Output: [[0,3],[5,0]]

Constraints:
    - 1 <= len(buildings) <= 10^4
    - 0 <= left_i < right_i <= 2^31 - 1
    - 1 <= height_i <= 2^31 - 1

Hint: Process events (building start and end) from left to right.
      Use a max-heap to track the tallest active building. A key
      point occurs when the max height changes.
"""

import heapq


def get_skyline(buildings: list[list[int]]) -> list[list[int]]:
    pass


# Test cases
print(get_skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# Expected: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

print(get_skyline([[0,2,3],[2,5,3]]))
# Expected: [[0,3],[5,0]]
