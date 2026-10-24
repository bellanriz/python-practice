"""
LeetCode 126 - Word Ladder II

Given two words beginWord and endWord, and a dictionary wordList,
return all the shortest transformation sequences from beginWord
to endWord.

Each transformation changes exactly one letter at a time, and every
transformed word must exist in the wordList.

Return [] if there is no such transformation sequence.

Example 1:
    Input:  beginWord = "hit"
            endWord = "cog"
            wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
    ]

Example 2:
    Input:  beginWord = "hit"
            endWord = "cog"
            wordList = ["hot","dot","dog","lot","log"]
    Output: []
    Explanation: endWord "cog" is not in wordList.

Constraints:
    - 1 <= len(beginWord) <= 5
    - endWord.length == beginWord.length
    - 1 <= len(wordList) <= 500
    - All words have the same length.
    - All words consist of lowercase English letters.
    - beginWord, endWord, and all words in wordList are unique.

Module hint: Use collections.deque for BFS and collections.defaultdict
             to build a graph of word patterns (e.g., "h*t" -> ["hit","hot"]).
             First BFS to find shortest distance, then backtrack to find
             all shortest paths.
"""

# You may use: from collections import deque, defaultdict


def find_ladders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    pass


# Test cases
print(find_ladders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Expected: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

print(find_ladders("hit", "cog", ["hot","dot","dog","lot","log"]))
# Expected: []
