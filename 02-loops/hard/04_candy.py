"""
LeetCode 135 - Candy

There are n children standing in a line. Each child has a rating value
given in the integer array ratings.

You are giving candies to these children with these rules:
    - Each child must have at least one candy.
    - Children with a higher rating than their neighbor get more
      candies than that neighbor.

Return the minimum number of candies you need to distribute.

Example 1:
    Input:  ratings = [1, 0, 2]
    Output: 5
    Explanation: You can give [2, 1, 2] candies respectively.

Example 2:
    Input:  ratings = [1, 2, 2]
    Output: 4
    Explanation: You can give [1, 2, 1] candies respectively.
                 The third child gets 1 because it only needs to
                 satisfy the condition relative to its neighbors.

Constraints:
    - n == len(ratings)
    - 1 <= n <= 2 * 10^4
    - 0 <= ratings[i] <= 2 * 10^4

Hint: Try two passes — one left-to-right and one right-to-left.
"""


def candy(ratings: list[int]) -> int:
    pass


# Test cases
print(candy([1, 0, 2]))  # Expected: 5
print(candy([1, 2, 2]))  # Expected: 4
