"""
LeetCode 591 - Tag Validator

Given a string representing a code snippet, implement a tag validator
to parse the code and return whether it is valid.

Rules:
    1. The code must be wrapped in a valid closed tag.
    2. A closed tag has the form <TAG_NAME>TAG_CONTENT</TAG_NAME>.
    3. TAG_NAME is uppercase letters only, length 1-9.
    4. TAG_CONTENT can contain other valid closed tags, cdata, and
       any characters EXCEPT unmatched <.
    5. A cdata has the form <![CDATA[CDATA_CONTENT]]>. CDATA_CONTENT
       can contain ANY characters (including < and unmatched tags).

Example 1:
    Input:  code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
    Output: True

Example 2:
    Input:  code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
    Output: True

Example 3:
    Input:  code = "<A>  <B> </A>   </B>"
    Output: False
    Explanation: Tags are not correctly nested.

Constraints:
    - 1 <= len(code) <= 500

Module hint: Use the re module for matching CDATA sections and tag patterns.
             A stack-based approach helps validate proper nesting.
"""

# You may use: import re


def is_valid(code: str) -> bool:
    pass


# Test cases
print(is_valid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))
# Expected: True

print(is_valid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))
# Expected: True

print(is_valid("<A>  <B> </A>   </B>"))
# Expected: False
