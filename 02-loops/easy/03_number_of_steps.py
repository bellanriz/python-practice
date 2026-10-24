"""
LeetCode 1342 - Number of Steps to Reduce a Number to Zero

Given an integer num, return the number of steps to reduce it to zero.
In one step:
    - If the current number is even, divide it by 2.
    - If the current number is odd, subtract 1 from it.

Example 1:
    Input:  num = 14
    Output: 6
    Explanation:
        Step 1: 14 is even -> 14 / 2 = 7
        Step 2: 7 is odd  -> 7 - 1  = 6
        Step 3: 6 is even -> 6 / 2  = 3
        Step 4: 3 is odd  -> 3 - 1  = 2
        Step 5: 2 is even -> 2 / 2  = 1
        Step 6: 1 is odd  -> 1 - 1  = 0

Example 2:
    Input:  num = 8
    Output: 4
    Explanation: 8 -> 4 -> 2 -> 1 -> 0

Example 3:
    Input:  num = 123
    Output: 12

Constraints:
    - 0 <= num <= 10^6
"""


def number_of_steps(num: int) -> int:
    pass


# Test cases
print(number_of_steps(14))   # Expected: 6
print(number_of_steps(8))    # Expected: 4
print(number_of_steps(123))  # Expected: 12
