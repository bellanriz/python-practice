"""
LeetCode 12 - Integer to Roman

Roman numerals use seven symbols: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.

Special subtraction rules:
    - I before V (5) or X (10) -> 4 or 9
    - X before L (50) or C (100) -> 40 or 90
    - C before D (500) or M (1000) -> 400 or 900

Given an integer, convert it to a roman numeral.

Example 1:
    Input:  num = 3749
    Output: "MMMDCCXLIX"
    Explanation: 3000=MMM, 700=DCC, 40=XL, 9=IX

Example 2:
    Input:  num = 58
    Output: "LVIII"
    Explanation: 50=L, 5=V, 3=III

Example 3:
    Input:  num = 1994
    Output: "MCMXCIV"
    Explanation: 1000=M, 900=CM, 90=XC, 4=IV

Constraints:
    - 1 <= num <= 3999
"""


def int_to_roman(num: int) -> str:
    pass


# Test cases
print(int_to_roman(3749))  # Expected: "MMMDCCXLIX"
print(int_to_roman(58))    # Expected: "LVIII"
print(int_to_roman(1994))  # Expected: "MCMXCIV"
