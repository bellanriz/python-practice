"""
LeetCode 13 - Roman to Integer

Roman numerals use seven symbols: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.

Special subtraction rules:
    - I before V or X -> subtract I (e.g. IV=4, IX=9)
    - X before L or C -> subtract X (e.g. XL=40, XC=90)
    - C before D or M -> subtract C (e.g. CD=400, CM=900)

Given a roman numeral string, convert it to an integer.

Example 1:
    Input:  s = "III"
    Output: 3

Example 2:
    Input:  s = "LVIII"
    Output: 58
    Explanation: L=50, V=5, III=3

Example 3:
    Input:  s = "MCMXCIV"
    Output: 1994
    Explanation: M=1000, CM=900, XC=90, IV=4

Constraints:
    - 1 <= len(s) <= 15
    - s contains only characters ('I','V','X','L','C','D','M')
    - It is guaranteed that s is a valid roman numeral in [1, 3999].
"""


def roman_to_int(s: str) -> int:
    pass


# Test cases
print(roman_to_int("III"))      # Expected: 3
print(roman_to_int("LVIII"))    # Expected: 58
print(roman_to_int("MCMXCIV"))  # Expected: 1994
