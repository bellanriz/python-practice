"""
LeetCode 402 - Remove K Digits

Given string num representing a non-negative integer and integer k,
return the smallest possible integer after removing k digits.

Example 1:
    Input:  num = "1432219", k = 3
    Output: "1219"

Example 2:
    Input:  num = "10200", k = 1
    Output: "200"

Example 3:
    Input:  num = "10", k = 2
    Output: "0"

Constraints:
    - 1 <= k <= len(num) <= 10^5

Hint: Use a monotonic stack. Remove digits from the stack when the
      current digit is smaller than the stack top (greedy). Handle
      leading zeros at the end.
"""


def remove_kdigits(num: str, k: int) -> str:
    pass


print(remove_kdigits("1432219", 3))  # Expected: "1219"
print(remove_kdigits("10200", 1))    # Expected: "200"
print(remove_kdigits("10", 2))       # Expected: "0"
