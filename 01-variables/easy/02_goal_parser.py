"""
LeetCode 1678 - Goal Parser Interpretation

You own a Goal Parser that can interpret a string command.
The command consists of an alphabet of "G", "()" and/or "(al)":
    - "G"    -> "G"
    - "()"   -> "o"
    - "(al)" -> "al"

Given the string command, return the Goal Parser's interpretation.

Example 1:
    Input:  command = "G()(al)"
    Output: "Goal"
    Explanation: G -> G, () -> o, (al) -> al

Example 2:
    Input:  command = "G()()()()(al)"
    Output: "Gooooal"

Example 3:
    Input:  command = "(al)G(al)()()G"
    Output: "alGalooG"

Constraints:
    - 1 <= len(command) <= 100
    - command consists of "G", "()", and/or "(al)" in some order.
"""


def interpret(command: str) -> str:
    pass


# Test cases
print(interpret("G()(al)"))            # Expected: "Goal"
print(interpret("G()()()()(al)"))      # Expected: "Gooooal"
print(interpret("(al)G(al)()()G"))     # Expected: "alGalooG"
