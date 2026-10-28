"""
LeetCode 278 - First Bad Version

You have n versions [1, 2, ..., n]. One version is bad, and all
subsequent versions are bad. Given an API is_bad(version), find the
first bad version. Minimize API calls.

Example 1:
    Input:  n = 5, bad = 4
    Output: 4

Example 2:
    Input:  n = 1, bad = 1
    Output: 1

Constraints:
    - 1 <= bad <= n <= 2^31 - 1

Hint: Binary search. If mid is bad, search left half. Otherwise right.
"""

# Simulated API
BAD = 4
def is_bad(version: int) -> bool:
    return version >= BAD


def first_bad_version(n: int) -> int:
    pass


BAD = 4
print(first_bad_version(5))  # Expected: 4
BAD = 1
print(first_bad_version(1))  # Expected: 1
