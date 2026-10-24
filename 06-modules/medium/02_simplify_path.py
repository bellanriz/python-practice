"""
LeetCode 71 - Simplify Path

Given an absolute Unix-style file path, simplify it to its canonical form.

Rules:
    - A single period '.' refers to the current directory.
    - A double period '..' moves to the parent directory.
    - Multiple consecutive slashes '///' are treated as a single '/'.
    - Any other format of periods (e.g. '...') is treated as a
      file/directory name.
    - The canonical path starts with a single '/' and has no trailing '/'.
    - Directories are separated by a single '/'.

Example 1:
    Input:  path = "/home/"
    Output: "/home"

Example 2:
    Input:  path = "/home//foo/"
    Output: "/home/foo"

Example 3:
    Input:  path = "/home/user/Documents/../Pictures"
    Output: "/home/user/Pictures"

Example 4:
    Input:  path = "/../"
    Output: "/"

Example 5:
    Input:  path = "/.../a/../b/c/../d/./"
    Output: "/.../b/d"

Constraints:
    - 1 <= len(path) <= 3000
    - path consists of English letters, digits, '.', '/' or '_'.
    - path is a valid absolute Unix path.

Module hint: Split the path using str.split('/') and use a
             collections.deque as a stack for building the result.
"""

# You may use: from collections import deque


def simplify_path(path: str) -> str:
    pass


# Test cases
print(simplify_path("/home/"))                          # Expected: "/home"
print(simplify_path("/home//foo/"))                     # Expected: "/home/foo"
print(simplify_path("/home/user/Documents/../Pictures"))# Expected: "/home/user/Pictures"
print(simplify_path("/../"))                            # Expected: "/"
print(simplify_path("/.../a/../b/c/../d/./"))           # Expected: "/.../b/d"
