"""
LeetCode 1353 - Maximum Number of Events That Can Be Attended

Given an array of events where events[i] = [startDay, endDay],
you can attend an event on any day d where startDay <= d <= endDay.
You can only attend one event per day.

Return the maximum number of events you can attend.

Example 1:
    Input:  events = [[1,2],[2,3],[3,4]]
    Output: 3

Example 2:
    Input:  events = [[1,2],[2,3],[3,4],[1,2]]
    Output: 4

Constraints:
    - 1 <= len(events) <= 10^5
    - 1 <= startDay <= endDay <= 10^5

Hint: Sort by start day. For each day, add all events starting that
      day to a min-heap (by end day). Attend the event that ends
      soonest. Remove expired events.
"""

import heapq


def max_events(events: list[list[int]]) -> int:
    pass


print(max_events([[1,2],[2,3],[3,4]]))        # Expected: 3
print(max_events([[1,2],[2,3],[3,4],[1,2]]))  # Expected: 4
