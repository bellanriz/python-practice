"""
LeetCode 207 - Course Schedule

There are numCourses courses (0..numCourses-1). prerequisites[i] = [a,b]
means you must take course b before course a. Return True if you can
finish all courses.

Example 1:
    Input:  numCourses=2, prerequisites=[[1,0]]
    Output: True

Example 2:
    Input:  numCourses=2, prerequisites=[[1,0],[0,1]]
    Output: False (cycle)

Constraints:
    - 1 <= numCourses <= 2000

Hint: Detect cycles using topological sort (BFS with in-degree) or DFS.
"""

from collections import deque, defaultdict


def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pass


print(can_finish(2, [[1,0]]))          # Expected: True
print(can_finish(2, [[1,0],[0,1]]))    # Expected: False
