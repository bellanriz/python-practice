"""
LeetCode 488 - Zuma Game

In the Zuma game, there is a row of colored balls on a board. You
have balls in your hand. Insert a ball at any position — if 3+ same-
colored balls are consecutive, they are removed. This can chain.

Return the minimum number of balls from your hand to insert to clear
all balls. Return -1 if not possible.

Example 1:
    Input:  board = "WRRBBW", hand = "RB"
    Output: -1

Example 2:
    Input:  board = "WWRRBBWW", hand = "WRBRW"
    Output: 2

Example 3:
    Input:  board = "G", hand = "GGGGG"
    Output: 2

Constraints:
    - 1 <= len(board) <= 16
    - 1 <= len(hand) <= 5

Hint: DFS/BFS with memoization. Try inserting each hand ball at
      each position. After insertion, collapse consecutive groups
      of 3+. Prune states.
"""

from functools import lru_cache


def find_min_step(board: str, hand: str) -> int:
    pass


print(find_min_step("WRRBBW", "RB"))       # Expected: -1
print(find_min_step("WWRRBBWW", "WRBRW"))  # Expected: 2
print(find_min_step("G", "GGGGG"))          # Expected: 2
