"""
LeetCode 1431 - Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies,
where each candies[i] represents the number of candies the i-th kid
has, and an integer extraCandies.

Return a boolean list result where result[i] is True if, after giving
the i-th kid all the extraCandies, they will have the greatest number
of candies among all the kids, or False otherwise.

Note: multiple kids can have the greatest number of candies.

Example 1:
    Input:  candies = [2, 3, 5, 1, 3], extraCandies = 3
    Output: [True, True, True, False, True]
    Explanation:
        Kid 0: 2 + 3 = 5 >= 5 -> True
        Kid 1: 3 + 3 = 6 >= 5 -> True
        Kid 2: 5 + 3 = 8 >= 5 -> True
        Kid 3: 1 + 3 = 4 < 5  -> False
        Kid 4: 3 + 3 = 6 >= 5 -> True

Example 2:
    Input:  candies = [4, 2, 1, 1, 2], extraCandies = 1
    Output: [True, False, False, False, False]

Example 3:
    Input:  candies = [12, 1, 12], extraCandies = 10
    Output: [True, False, True]

Constraints:
    - n == len(candies)
    - 2 <= n <= 100
    - 1 <= candies[i] <= 100
    - 1 <= extraCandies <= 50
"""


def kids_with_candies(candies: list[int], extraCandies: int) -> list[bool]:
    pass


# Test cases
print(kids_with_candies([2, 3, 5, 1, 3], 3))   # Expected: [True, True, True, False, True]
print(kids_with_candies([4, 2, 1, 1, 2], 1))   # Expected: [True, False, False, False, False]
print(kids_with_candies([12, 1, 12], 10))       # Expected: [True, False, True]
