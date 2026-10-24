"""
LeetCode 588 - Design In-Memory File System

Design a file system that provides the following functions:

Implement the FileSystem class:
    - FileSystem()           -> Initializes the object.
    - ls(path)               -> If path is a file path, returns a list
                                containing only this file's name. If path
                                is a directory, returns the list of file
                                and directory names in this directory,
                                sorted in lexicographic order.
    - mkdir(path)            -> Makes a new directory according to the
                                given path. Creates intermediate dirs if
                                they don't exist.
    - add_content(filePath, content)
                             -> If filePath doesn't exist, creates a new
                                file with given content. If it exists,
                                appends content to the original content.
    - read_content(filePath) -> Returns the content in the file.

Example:
    fs = FileSystem()
    fs.ls("/")                                  # -> []
    fs.mkdir("/a/b/c")
    fs.add_content("/a/b/c/d", "hello")
    fs.ls("/")                                  # -> ["a"]
    fs.read_content("/a/b/c/d")                 # -> "hello"

Constraints:
    - 1 <= len(path) <= 100
    - All directory and file paths are absolute (begin with '/').
    - No concurrent operations.

Hint: Use a Trie-like structure where each node is a directory or file.
      Each node has a dict of children and optional file content.
"""


class FileSystem:

    def __init__(self):
        pass

    def ls(self, path: str) -> list[str]:
        pass

    def mkdir(self, path: str) -> None:
        pass

    def add_content(self, filePath: str, content: str) -> None:
        pass

    def read_content(self, filePath: str) -> str:
        pass


# Test cases
fs = FileSystem()
print(fs.ls("/"))                          # Expected: []
fs.mkdir("/a/b/c")
fs.add_content("/a/b/c/d", "hello")
print(fs.ls("/"))                          # Expected: ["a"]
print(fs.read_content("/a/b/c/d"))         # Expected: "hello"
fs.add_content("/a/b/c/d", " world")
print(fs.read_content("/a/b/c/d"))         # Expected: "hello world"
