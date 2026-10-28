"""
LeetCode 1047 - Remove All Adjacent Duplicates In String

Given a string s, repeatedly remove pairs of adjacent equal letters.
Return the final string after all such removals.

Example 1:
    Input:  s = "abbaca"
    Output: "ca"
    Explanation: "abbaca" -> "aaca" -> "ca"

Example 2:
    Input:  s = "azxxzy"
    Output: "ay"

Constraints:
    - 1 <= len(s) <= 10^5
    - s consists of lowercase English letters.

Hint: Use a stack. Push characters, pop when top matches current.
"""


def remove_duplicates(s: str) -> str:
    pass


print(remove_duplicates("abbaca"))  # Expected: "ca"
print(remove_duplicates("azxxzy"))  # Expected: "ay"
