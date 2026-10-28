"""
LeetCode 39 - Combination Sum

Given an array of distinct integers candidates and a target integer,
return all unique combinations of candidates where the chosen numbers
sum to target. You may use the same number unlimited times.

Example 1:
    Input:  candidates = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]

Example 2:
    Input:  candidates = [2, 3, 5], target = 8
    Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

Constraints:
    - 1 <= len(candidates) <= 30
    - All candidates are distinct.
    - 1 <= target <= 40

Hint: Backtrack. At each step, either include the current candidate
      again or move to the next one.
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    pass


print(combination_sum([2, 3, 6, 7], 7))  # Expected: [[2,2,3],[7]]
print(combination_sum([2, 3, 5], 8))       # Expected: [[2,2,2,2],[2,3,3],[3,5]]
