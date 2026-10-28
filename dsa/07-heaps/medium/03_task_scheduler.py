"""
LeetCode 621 - Task Scheduler

Given a list of tasks (characters) and a cooldown interval n, return
the minimum number of intervals the CPU needs to finish all tasks.
Same tasks must be separated by at least n intervals.

Example 1:
    Input:  tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8  (A->B->idle->A->B->idle->A->B)

Example 2:
    Input:  tasks = ["A","C","A","B","D","B"], n = 1
    Output: 6  (no idle needed)

Example 3:
    Input:  tasks = ["A","A","A","B","B","B"], n = 0
    Output: 6

Constraints:
    - 1 <= len(tasks) <= 10^4
    - 0 <= n <= 100

Hint: The most frequent task determines the frame. Use a max-heap
      and simulate, or use the formula approach with max frequency.
"""

import heapq
from collections import Counter


def least_interval(tasks: list[str], n: int) -> int:
    pass


print(least_interval(["A","A","A","B","B","B"], 2))    # Expected: 8
print(least_interval(["A","C","A","B","D","B"], 1))    # Expected: 6
print(least_interval(["A","A","A","B","B","B"], 0))    # Expected: 6
