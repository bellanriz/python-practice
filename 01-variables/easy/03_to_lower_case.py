"""
LeetCode 709 - To Lower Case

Given a string s, return the string after replacing every uppercase
letter with the same lowercase letter.

Solve this WITHOUT using the built-in .lower() method.

Example 1:
    Input:  s = "Hello"
    Output: "hello"

Example 2:
    Input:  s = "here"
    Output: "here"

Example 3:
    Input:  s = "LOVELY"
    Output: "lovely"

Constraints:
    - 1 <= len(s) <= 100
    - s consists of printable ASCII characters.

Hint: Think about ASCII values. 'A' is 65, 'a' is 97. The difference
      is 32 for every letter.
"""


def to_lower_case(s: str) -> str:
    pass


# Test cases
print(to_lower_case("Hello"))   # Expected: "hello"
print(to_lower_case("here"))    # Expected: "here"
print(to_lower_case("LOVELY"))  # Expected: "lovely"
