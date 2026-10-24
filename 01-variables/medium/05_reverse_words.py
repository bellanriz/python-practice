"""
LeetCode 151 - Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is a sequence of non-space characters. The words in s are
separated by at least one space.

Return a string of the words in reverse order concatenated by a
single space. The result should not contain leading or trailing
spaces and should have only a single space between words.

Example 1:
    Input:  s = "the sky is blue"
    Output: "blue is sky the"

Example 2:
    Input:  s = "  hello world  "
    Output: "world hello"
    Explanation: Reversed string should not have leading/trailing spaces.

Example 3:
    Input:  s = "a good   example"
    Output: "example good a"
    Explanation: Multiple spaces reduced to a single space.

Constraints:
    - 1 <= len(s) <= 10^4
    - s contains English letters (upper and lower), digits, and spaces ' '.
    - There is at least one word in s.

Challenge: Can you solve it in O(1) extra space (in-place)?
"""


def reverse_words(s: str) -> str:
    pass


# Test cases
print(reverse_words("the sky is blue"))    # Expected: "blue is sky the"
print(reverse_words("  hello world  "))    # Expected: "world hello"
print(reverse_words("a good   example"))   # Expected: "example good a"
