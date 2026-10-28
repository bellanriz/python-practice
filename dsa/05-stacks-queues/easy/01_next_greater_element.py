"""
LeetCode 496 - Next Greater Element I

Given two arrays nums1 (subset of nums2), for each element in nums1,
find the next greater element in nums2 (to its right). Return -1 if
no greater element exists.

Example 1:
    Input:  nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]

Example 2:
    Input:  nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]

Constraints:
    - All integers in nums1 and nums2 are unique.
    - All integers of nums1 also appear in nums2.

Hint: Use a monotonic stack on nums2 to precompute next greater for
      each element. Store results in a hash map.
"""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    pass


print(next_greater_element([4,1,2], [1,3,4,2]))  # Expected: [-1,3,-1]
print(next_greater_element([2,4], [1,2,3,4]))     # Expected: [3,-1]
