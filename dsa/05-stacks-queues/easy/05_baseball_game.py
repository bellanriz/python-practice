"""
LeetCode 682 - Baseball Game

You are keeping score with these operations:
    - An integer x: record a new score of x.
    - "+": record a score that is the sum of the previous two scores.
    - "D": record a score that is double the previous score.
    - "C": invalidate (remove) the previous score.

Return the sum of all scores after all operations.

Example 1:
    Input:  ops = ["5","2","C","D","+"]
    Output: 30
    Explanation:
        "5" -> [5]
        "2" -> [5,2]
        "C" -> [5] (remove 2)
        "D" -> [5,10] (double 5)
        "+" -> [5,10,15] (5+10)
        Sum = 30

Example 2:
    Input:  ops = ["5","-2","4","C","D","9","+","+"]
    Output: 27

Constraints:
    - 1 <= len(ops) <= 1000
"""


def cal_points(operations: list[str]) -> int:
    pass


print(cal_points(["5","2","C","D","+"]))              # Expected: 30
print(cal_points(["5","-2","4","C","D","9","+","+"]))  # Expected: 27
