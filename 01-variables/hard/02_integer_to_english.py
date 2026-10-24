"""
LeetCode 273 - Integer to English Words

Convert a non-negative integer num to its English words representation.

Example 1:
    Input:  num = 123
    Output: "One Hundred Twenty Three"

Example 2:
    Input:  num = 12345
    Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
    Input:  num = 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
    Input:  num = 0
    Output: "Zero"

Constraints:
    - 0 <= num <= 2^31 - 1

Hint: Break the number into groups of three digits (thousands,
      millions, billions) and handle each group separately.
"""


def number_to_words(num: int) -> str:
    pass


# Test cases
print(number_to_words(123))       # Expected: "One Hundred Twenty Three"
print(number_to_words(12345))     # Expected: "Twelve Thousand Three Hundred Forty Five"
print(number_to_words(1234567))   # Expected: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print(number_to_words(0))         # Expected: "Zero"
