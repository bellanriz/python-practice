# Python Practice — LeetCode Style

A structured collection of 90 LeetCode problems organized by Python topic and difficulty level. Each file contains a problem description, function/class stub, and test cases — no answers included.

## Structure

```
python-practice/
├── 01-variables/       Variables, strings, type manipulation
├── 02-loops/           For loops, while loops, iteration patterns
├── 03-functions/       Function design, recursion, backtracking
├── 04-lists/           Array/list manipulation, sorting, partitioning
├── 05-classes/         OOP design — build classes with methods
└── 06-modules/         Problems using Python's standard library
```

Each topic has three difficulty levels with 5 problems each:

| Level    | Description                              |
|----------|------------------------------------------|
| `easy/`  | Fundamentals, good for warming up        |
| `medium/`| Requires combining multiple concepts     |
| `hard/`  | Advanced algorithms and data structures  |

## Problem List

### 01-variables
| #  | Easy                          | Medium                     | Hard                          |
|----|-------------------------------|----------------------------|-------------------------------|
| 01 | Final Value After Ops (2011)  | Integer to Roman (12)      | Valid Number (65)             |
| 02 | Goal Parser (1678)            | Roman to Integer (13)      | Integer to English (273)      |
| 03 | To Lower Case (709)           | String to Integer (8)      | Basic Calculator (224)        |
| 04 | Defanging IP (1108)           | Reverse Integer (7)        | Number of Atoms (726)         |
| 05 | Convert Temperature (2469)    | Reverse Words (151)        | Closest Palindrome (564)      |

### 02-loops
| #  | Easy                          | Medium                     | Hard                          |
|----|-------------------------------|----------------------------|-------------------------------|
| 01 | Running Sum (1480)            | Rotate Array (189)         | Trapping Rain Water (42)      |
| 02 | Fizz Buzz (412)               | Product Except Self (238)  | First Missing Positive (41)   |
| 03 | Number of Steps (1342)        | Spiral Matrix (54)         | Sliding Window Max (239)      |
| 04 | Palindrome Number (9)         | Find Duplicates (442)      | Candy (135)                   |
| 05 | Richest Customer (1672)       | Set Matrix Zeroes (73)     | Text Justification (68)       |

### 03-functions
| #  | Easy                          | Medium                     | Hard                          |
|----|-------------------------------|----------------------------|-------------------------------|
| 01 | Two Sum (1)                   | 3Sum (15)                  | Regex Matching (10)           |
| 02 | Remove Duplicates (26)        | Letter Combinations (17)   | Longest Valid Parens (32)     |
| 03 | Remove Element (27)           | Permutations (46)          | N-Queens (51)                 |
| 04 | Search Insert (35)            | Generate Parentheses (22)  | Sudoku Solver (37)            |
| 05 | Length of Last Word (58)      | Pow(x, n) (50)             | Largest Rectangle (84)        |

### 04-lists
| #  | Easy                          | Medium                     | Hard                          |
|----|-------------------------------|----------------------------|-------------------------------|
| 01 | Concatenation of Array (1929) | Merge Intervals (56)       | Median Two Sorted (4)         |
| 02 | Kids With Candies (1431)      | Sort Colors (75)           | Skyline Problem (218)         |
| 03 | Shuffle the Array (1470)      | Longest Consecutive (128)  | Count Smaller (315)           |
| 04 | Smaller Than Current (1365)   | Top K Frequent (347)       | Median from Stream (295)      |
| 05 | Even Number of Digits (1295)  | Rotate Image (48)          | Patching Array (330)          |

### 05-classes
| #  | Easy                          | Medium                     | Hard                          |
|----|-------------------------------|----------------------------|-------------------------------|
| 01 | Stack Using Queues (225)      | LRU Cache (146)            | LFU Cache (460)               |
| 02 | Queue Using Stacks (232)      | Insert Delete Random (380) | All O'one (432)               |
| 03 | Min Stack (155)               | Implement Trie (208)       | In-Memory File System (588)   |
| 04 | Range Sum Query (303)         | Design Twitter (355)       | Max Frequency Stack (895)     |
| 05 | Design HashMap (706)          | Shuffle an Array (384)     | Snapshot Array (1146)         |

### 06-modules
| #  | Easy                          | Medium                     | Hard                          |
|----|-------------------------------|----------------------------|-------------------------------|
| 01 | Valid Anagram (242)           | Top K Frequent Words (692) | Palindrome Pairs (336)        |
| 02 | Valid Parentheses (20)        | Simplify Path (71)         | Tag Validator (591)           |
| 03 | First Unique Char (387)       | Decode String (394)        | Concatenated Words (472)      |
| 04 | Majority Element (169)        | Find Duplicate Files (609) | Word Search II (212)          |
| 05 | Summary Ranges (228)          | Find All Anagrams (438)    | Word Ladder II (126)          |

## How to Use

1. Pick a topic and difficulty level
2. Open the file and read the problem description
3. Write your solution where it says `pass`
4. Run the file to check against the test cases:
   ```bash
   python 01-variables/easy/01_final_value_after_operations.py
   ```
5. Compare your output with the expected output in the comments

## Recommended Order

Start with **easy** across all topics, then move to **medium**, then **hard**:

```
01-variables/easy → 02-loops/easy → 03-functions/easy → 04-lists/easy → 05-classes/easy → 06-modules/easy
       ↓                 ↓                 ↓                 ↓                ↓                 ↓
    medium            medium            medium            medium           medium            medium
       ↓                 ↓                 ↓                 ↓                ↓                 ↓
     hard              hard              hard              hard             hard              hard
```

## Stats

- **Total problems:** 90
- **Easy:** 30 | **Medium:** 30 | **Hard:** 30
- **Topics:** 6
- **Source:** [LeetCode](https://leetcode.com) (numbers in parentheses are problem IDs)
