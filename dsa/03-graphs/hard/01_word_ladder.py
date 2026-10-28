"""
LeetCode 127 - Word Ladder

Given beginWord, endWord, and a wordList, find the length of the
shortest transformation sequence from beginWord to endWord.
Each transformation changes exactly one letter and must be in wordList.

Return 0 if no such sequence exists.

Example 1:
    Input:  beginWord="hit", endWord="cog",
            wordList=["hot","dot","dog","lot","log","cog"]
    Output: 5 ("hit"->"hot"->"dot"->"dog"->"cog")

Example 2:
    Input:  beginWord="hit", endWord="cog",
            wordList=["hot","dot","dog","lot","log"]
    Output: 0

Constraints:
    - 1 <= len(beginWord) <= 10
    - All words have the same length.

Hint: BFS. Use wildcard patterns (e.g., "h*t") to find neighbors efficiently.
"""

from collections import deque, defaultdict


def ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
    pass


print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Expected: 5
print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]))         # Expected: 0
