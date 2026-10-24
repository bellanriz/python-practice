"""
LeetCode 472 - Concatenated Words

Given an array of strings words (without duplicates), return all the
concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely
of at least two shorter words from the given array.

Example 1:
    Input:  words = ["cat","cats","catsdogcats","dog","dogcatsdog",
                     "hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation:
        "catsdogcats" = "cats" + "dog" + "cats"
        "dogcatsdog"  = "dog" + "cats" + "dog"
        "ratcatdogcat"= "rat" + "cat" + "dog" + "cat"

Example 2:
    Input:  words = ["cat", "dog", "catdog"]
    Output: ["catdog"]

Constraints:
    - 1 <= len(words) <= 10^4
    - 1 <= len(words[i]) <= 30
    - words[i] consists of only lowercase English letters.
    - All strings in words are unique.
    - 1 <= sum(len(words[i])) <= 10^5

Module hint: Use a set for O(1) word lookups. Use functools.lru_cache
             for memoized recursion, or dynamic programming to check
             if a word can be broken into parts from the set.
"""

# You may use: from functools import lru_cache


def find_all_concatenated_words(words: list[str]) -> list[str]:
    pass


# Test cases
print(find_all_concatenated_words(
    ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
))
# Expected: ["catsdogcats","dogcatsdog","ratcatdogcat"]

print(find_all_concatenated_words(["cat", "dog", "catdog"]))
# Expected: ["catdog"]
