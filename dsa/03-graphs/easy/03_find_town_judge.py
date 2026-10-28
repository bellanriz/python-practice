"""
LeetCode 997 - Find the Town Judge

In a town of n people (labeled 1..n), there may be a town judge.
The judge trusts nobody and everybody else trusts the judge.

Given trust[i] = [a, b] meaning person a trusts person b, return
the judge's label. If no judge exists, return -1.

Example 1:
    Input:  n = 2, trust = [[1,2]]
    Output: 2

Example 2:
    Input:  n = 3, trust = [[1,3],[2,3]]
    Output: 3

Example 3:
    Input:  n = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Constraints:
    - 1 <= n <= 1000

Hint: The judge has in-degree n-1 and out-degree 0. Track trust counts.
"""


def find_judge(n: int, trust: list[list[int]]) -> int:
    pass


print(find_judge(2, [[1,2]]))                  # Expected: 2
print(find_judge(3, [[1,3],[2,3]]))            # Expected: 3
print(find_judge(3, [[1,3],[2,3],[3,1]]))      # Expected: -1
