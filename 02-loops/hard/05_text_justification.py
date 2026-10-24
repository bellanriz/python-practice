"""
LeetCode 68 - Text Justification

Given an array of strings 'words' and a width 'maxWidth', format the
text such that each line has exactly maxWidth characters and is
fully (left and right) justified.

Rules:
    - Pack as many words as you can in each line.
    - Pad extra spaces between words when necessary so each line has
      exactly maxWidth characters.
    - Extra spaces should be distributed as evenly as possible. If
      the spaces do not divide evenly, the left slots get more spaces
      than the right slots.
    - The last line should be left-justified with no extra spacing
      between words.

Example 1:
    Input:  words = ["This", "is", "an", "example", "of", "text",
                     "justification."]
            maxWidth = 16
    Output: [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]

Example 2:
    Input:  words = ["What", "must", "be", "acknowledgment", "shall", "be"]
            maxWidth = 16
    Output: [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]

Example 3:
    Input:  words = ["Science", "is", "what", "we", "understand",
                     "well", "enough", "to", "explain", "to", "a",
                     "computer.", "Art", "is", "everything", "else",
                     "we", "do"]
            maxWidth = 20
    Output: [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]

Constraints:
    - 1 <= len(words) <= 300
    - 1 <= len(words[i]) <= 20
    - words[i] consists of only English letters and symbols.
    - 1 <= maxWidth <= 100
    - len(words[i]) <= maxWidth
"""


def full_justify(words: list[str], maxWidth: int) -> list[str]:
    pass


# Test cases
result1 = full_justify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16
)
for line in result1:
    print(f"|{line}|")
# Expected:
# |This    is    an|
# |example  of text|
# |justification.  |

print()

result2 = full_justify(
    ["What", "must", "be", "acknowledgment", "shall", "be"], 16
)
for line in result2:
    print(f"|{line}|")
# Expected:
# |What   must   be|
# |acknowledgment  |
# |shall be        |
