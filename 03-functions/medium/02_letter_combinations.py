"""
LeetCode 17 - Letter Combinations of a Phone Number

Given a string containing digits from 2-9, return all possible letter
combinations that the number could represent. Return the answer in
any order.

Phone mapping (like telephone buttons):
    2 -> "abc"    3 -> "def"    4 -> "ghi"
    5 -> "jkl"    6 -> "mno"    7 -> "pqrs"
    8 -> "tuv"    9 -> "wxyz"

Example 1:
    Input:  digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input:  digits = ""
    Output: []

Example 3:
    Input:  digits = "2"
    Output: ["a", "b", "c"]

Constraints:
    - 0 <= len(digits) <= 4
    - digits[i] is a digit in the range ['2', '9'].

Hint: This is a classic backtracking problem. Build combinations
      one digit at a time using recursion.
"""


def letter_combinations(digits: str) -> list[str]:
    pass


# Test cases
print(letter_combinations("23"))  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combinations(""))    # Expected: []
print(letter_combinations("2"))   # Expected: ["a", "b", "c"]
