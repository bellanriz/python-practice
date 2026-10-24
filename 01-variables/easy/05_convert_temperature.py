"""
LeetCode 2469 - Convert the Temperature

You are given a non-negative floating point number rounded to two
decimal places celsius, that denotes the temperature in Celsius.

Convert Celsius into Kelvin and Fahrenheit and return it as a list
[kelvin, fahrenheit].

Formulas:
    Kelvin     = Celsius + 273.15
    Fahrenheit = Celsius * 1.80 + 32.00

Answers within 10^-5 of the actual answer will be accepted.

Example 1:
    Input:  celsius = 36.50
    Output: [309.65, 97.70]

Example 2:
    Input:  celsius = 122.11
    Output: [395.26, 251.798]

Constraints:
    - 0 <= celsius <= 1000
"""


def convert_temperature(celsius: float) -> list[float]:
    pass


# Test cases
print(convert_temperature(36.50))    # Expected: [309.65, 97.7]
print(convert_temperature(122.11))   # Expected: [395.26, 251.798]
