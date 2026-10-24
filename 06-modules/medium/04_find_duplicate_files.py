"""
LeetCode 609 - Find Duplicate File in System

Given a list of directory info strings, each containing a directory
path followed by one or more files with their contents, find all
groups of duplicate files (files with the same content).

Format of each input string:
    "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ..."

Return a list of groups of duplicate file paths.

Example 1:
    Input: paths = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)"
    ]
    Output: [
        ["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
        ["root/a/1.txt","root/c/3.txt"]
    ]

Example 2:
    Input: paths = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)"
    ]
    Output: [
        ["root/a/2.txt","root/c/d/4.txt"],
        ["root/a/1.txt","root/c/3.txt"]
    ]

Constraints:
    - 1 <= len(paths) <= 2 * 10^4
    - 1 <= len(paths[i]) <= 3000
    - File content characters are limited to lowercase/digits and spaces.

Module hint: Use collections.defaultdict(list) to group files by content.
             Parse each entry by splitting on spaces and extracting the
             content between parentheses.
"""

# You may use: from collections import defaultdict


def find_duplicate(paths: list[str]) -> list[list[str]]:
    pass


# Test cases
result = find_duplicate([
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)"
])
print(result)
# Expected (order may vary):
# [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
#  ["root/a/1.txt","root/c/3.txt"]]
