"""
LeetCode 692 - Top K Frequent Words

Given an array of strings words and an integer k, return the k most
frequent strings. Return the answer sorted by frequency from highest
to lowest. If two words have the same frequency, sort them in
alphabetical order.

Example 1:
    Input:  words = ["i","love","leetcode","i","love","coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
                 "i" comes before "love" due to alphabetical order.

Example 2:
    Input:  words = ["the","day","is","sunny","the","the","the",
                     "sunny","is","is"], k = 4
    Output: ["the", "is", "sunny", "day"]

Constraints:
    - 1 <= len(words) <= 500
    - 1 <= len(words[i]) <= 10
    - words[i] consists of lowercase English letters.
    - k is in range [1, number of unique words].

Module hint: Use collections.Counter for counting and heapq.nsmallest
             or heapq.nlargest with a custom key for efficient top-k.
"""

# You may use: from collections import Counter
# You may use: import heapq


def top_k_frequent(words: list[str], k: int) -> list[str]:
    pass


# Test cases
print(top_k_frequent(["i","love","leetcode","i","love","coding"], 2))
# Expected: ["i", "love"]

print(top_k_frequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
# Expected: ["the", "is", "sunny", "day"]
