"""
LeetCode 506 - Relative Ranks

Given an array score where score[i] is the score of the ith athlete,
return an array of ranks:
    - 1st place -> "Gold Medal"
    - 2nd place -> "Silver Medal"
    - 3rd place -> "Bronze Medal"
    - 4th+      -> rank number as string ("4", "5", etc.)

Example 1:
    Input:  score = [5, 4, 3, 2, 1]
    Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Example 2:
    Input:  score = [10, 3, 8, 9, 4]
    Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

Constraints:
    - 1 <= len(score) <= 10^4
    - All scores are unique.

Hint: Sort indices by score descending, then assign ranks.
      A heap can also be used.
"""


def find_relative_ranks(score: list[int]) -> list[str]:
    pass


print(find_relative_ranks([5, 4, 3, 2, 1]))
# Expected: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

print(find_relative_ranks([10, 3, 8, 9, 4]))
# Expected: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
