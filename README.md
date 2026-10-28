# Python Practice — LeetCode Style

A structured collection of **210 LeetCode problems** organized by Python fundamentals and DSA topics, each with easy/medium/hard levels. Every file contains a problem description, function/class stub, and test cases — no answers included.

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

---

## DSA Section

```
dsa/
├── 01-linked-lists/         Singly/doubly linked list operations
├── 02-trees/                Binary trees, BSTs, traversals
├── 03-graphs/               DFS, BFS, topological sort, shortest paths
├── 04-dynamic-programming/  Memoization, tabulation, classic DP
├── 05-stacks-queues/        Monotonic stacks, queues, design problems
├── 06-sorting-searching/    Binary search, merge sort, quick sort
├── 07-heaps/                Min/max heaps, priority queues, greedy
└── 08-recursion/            Backtracking, divide & conquer, combinatorics
```

### 01-linked-lists
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Reverse Linked List (206)       | Add Two Numbers (2)          | Merge k Sorted Lists (23)       |
| 02 | Merge Two Sorted (21)           | Remove Nth From End (19)     | Reverse k-Group (25)            |
| 03 | Linked List Cycle (141)         | Cycle II (142)               | Copy Random Pointer (138)       |
| 04 | Remove Duplicates Sorted (83)   | Reorder List (143)           | Sort List (148)                 |
| 05 | Middle of List (876)            | Swap Nodes in Pairs (24)     | Remove Zero Sum (1171)          |

### 02-trees
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Max Depth (104)                 | Level Order (102)            | Max Path Sum (124)              |
| 02 | Invert Binary Tree (226)        | Validate BST (98)            | Serialize & Deserialize (297)   |
| 03 | Same Tree (100)                 | Kth Smallest BST (230)       | Binary Tree Cameras (968)       |
| 04 | Subtree of Another (572)        | Build from Preorder (105)    | Vertical Order (987)            |
| 05 | Diameter (543)                  | Lowest Common Ancestor (236) | Recover from Preorder (1028)    |

### 03-graphs
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Flood Fill (733)                | Number of Islands (200)      | Word Ladder (127)               |
| 02 | Island Perimeter (463)          | Clone Graph (133)            | Reconstruct Itinerary (332)     |
| 03 | Find Town Judge (997)           | Course Schedule (207)        | Longest Increasing Path (329)   |
| 04 | Find Center (1791)              | Rotting Oranges (994)        | Swim in Rising Water (778)      |
| 05 | Path Exists (1971)              | Pacific Atlantic (417)       | Shortest Path All Nodes (847)   |

### 04-dynamic-programming
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Climbing Stairs (70)            | Coin Change (322)            | Edit Distance (72)              |
| 02 | Best Time Stock (121)           | Longest Increasing Sub (300) | Burst Balloons (312)            |
| 03 | Min Cost Stairs (746)           | Unique Paths (62)            | Distinct Subsequences (115)     |
| 04 | Counting Bits (338)             | House Robber (198)           | Stock IV (188)                  |
| 05 | Is Subsequence (392)            | Longest Palindromic (5)      | Dungeon Game (174)              |

### 05-stacks-queues
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Next Greater Element (496)      | Reverse Polish (150)         | Maximal Rectangle (85)          |
| 02 | Remove Adjacent Dups (1047)     | Daily Temperatures (739)     | Remove Duplicate Letters (316)  |
| 03 | Recent Calls (933)              | Next Greater II (503)        | Remove K Digits (402)           |
| 04 | Backspace Compare (844)         | Validate Stack Seq (946)     | Shortest Subarray Sum K (862)   |
| 05 | Baseball Game (682)             | Circular Queue (622)         | Create Max Number (321)         |

### 06-sorting-searching
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Binary Search (704)             | First & Last Position (34)   | Find Min Rotated II (154)       |
| 02 | First Bad Version (278)         | Search Rotated (33)          | Reverse Pairs (493)             |
| 03 | Contains Duplicate (217)        | Kth Largest (215)            | Count Range Sum (327)           |
| 04 | Missing Number (268)            | Sort an Array (912)          | Data Stream Disjoint (352)      |
| 05 | Intersection Arrays (349)       | Find Duplicate Number (287)  | Split Array Largest (410)       |

### 07-heaps
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Last Stone Weight (1046)        | K Closest Points (973)       | IPO (502)                       |
| 02 | Kth Largest Stream (703)        | Kth Smallest Matrix (378)    | Smallest Range K Lists (632)    |
| 03 | Relative Ranks (506)            | Task Scheduler (621)         | Min Cost Hire Workers (857)     |
| 04 | Take Gifts (2558)               | Reorganize String (767)      | Max Events Attended (1353)      |
| 05 | Max Product Two (1464)          | Max Eaten Apples (1705)      | Max Subsequence Score (2542)    |

### 08-recursion
| #  | Easy                            | Medium                       | Hard                            |
|----|---------------------------------|------------------------------|---------------------------------|
| 01 | Fibonacci (509)                 | Subsets (78)                 | N-Queens II (52)                |
| 02 | Power of Two (231)              | Combination Sum (39)         | Remove Invalid Parens (301)     |
| 03 | Reverse String (344)            | Permutations II (47)         | Zuma Game (488)                 |
| 04 | Palindrome Linked List (234)    | Palindrome Partition (131)   | Expression Add Ops (282)        |
| 05 | Symmetric Tree (101)            | Word Search (79)             | Wildcard Matching (44)          |

---

## How to Use

1. Pick a topic and difficulty level
2. Open the file and read the problem description
3. Write your solution where it says `pass`
4. Run the file to check against the test cases:
   ```bash
   python dsa/01-linked-lists/easy/01_reverse_linked_list.py
   ```
5. Compare your output with the expected output in the comments

## Recommended Order

**Python fundamentals first**, then DSA:

```
01-variables → 02-loops → 03-functions → 04-lists → 05-classes → 06-modules
                                    ↓
              dsa/01-linked-lists → 02-trees → 03-graphs → 04-dp
                                    ↓
              dsa/05-stacks-queues → 06-sorting → 07-heaps → 08-recursion
```

Within each topic: easy → medium → hard.

## Stats

- **Total problems:** 210
- **Python fundamentals:** 90 (6 topics × 15)
- **DSA:** 120 (8 topics × 15)
- **Easy:** 70 | **Medium:** 70 | **Hard:** 70
- **Source:** [LeetCode](https://leetcode.com) (numbers in parentheses are problem IDs)
