"""
LeetCode 208 - Implement Trie (Prefix Tree)

A trie (prefix tree) is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings.

Implement the Trie class:
    - Trie()              -> Initializes the trie object.
    - insert(word)        -> Inserts the string word into the trie.
    - search(word)        -> Returns True if the string word is in
                             the trie (was inserted before), False otherwise.
    - starts_with(prefix) -> Returns True if there is a previously
                             inserted string that has the prefix, False otherwise.

Example:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")       # -> True
    trie.search("app")         # -> False
    trie.starts_with("app")    # -> True
    trie.insert("app")
    trie.search("app")         # -> True

Constraints:
    - 1 <= len(word), len(prefix) <= 2000
    - word and prefix consist only of lowercase English letters.
    - At most 3 * 10^4 calls total.

Hint: Each node has a dictionary of children (one per character) and
      a boolean flag indicating if it's the end of a word.
"""


class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass


# Test cases
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))      # Expected: True
print(trie.search("app"))        # Expected: False
print(trie.starts_with("app"))   # Expected: True
trie.insert("app")
print(trie.search("app"))        # Expected: True
