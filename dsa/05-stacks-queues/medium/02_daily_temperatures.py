"""
LeetCode 739 - Daily Temperatures

Given an array of daily temperatures, return an array where answer[i]
is the number of days you have to wait after day i to get a warmer
temperature. If no warmer day, answer[i] = 0.

Example 1:
    Input:  temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Example 2:
    Input:  temperatures = [30,40,50,60]
    Output: [1,1,1,0]

Constraints:
    - 1 <= len(temperatures) <= 10^5

Hint: Use a monotonic decreasing stack storing indices.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    pass


print(daily_temperatures([73,74,75,71,69,72,76,73]))  # Expected: [1,1,4,2,1,1,0,0]
print(daily_temperatures([30,40,50,60]))                # Expected: [1,1,1,0]
