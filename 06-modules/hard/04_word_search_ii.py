"""
LeetCode 212 - Word Search II

Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent
cells, where adjacent cells are horizontally or vertically neighboring.
The same cell may not be used more than once in a word.

Example 1:
    Input:  board = [
                ["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]
            ]
            words = ["oath","pea","eat","rain"]
    Output: ["eat", "oath"]

Example 2:
    Input:  board = [["a","b"],["c","d"]]
            words = ["abcb"]
    Output: []

Constraints:
    - m == len(board), n == len(board[i])
    - 1 <= m, n <= 12
    - board[i][j] is a lowercase English letter.
    - 1 <= len(words) <= 3 * 10^4
    - 1 <= len(words[i]) <= 10
    - words[i] consists of lowercase English letters.
    - All strings in words are unique.

Module hint: Build a Trie (using nested dicts or collections.defaultdict)
             from the word list, then DFS from each cell on the board.
             This avoids redundant searches compared to checking each
             word individually.
"""

# You may use: from collections import defaultdict


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    pass


# Test cases
board1 = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
print(find_words(board1, ["oath","pea","eat","rain"]))
# Expected: ["eat", "oath"] (order may vary)

board2 = [["a","b"],["c","d"]]
print(find_words(board2, ["abcb"]))
# Expected: []
