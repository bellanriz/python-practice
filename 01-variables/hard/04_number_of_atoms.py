"""
LeetCode 726 - Number of Atoms

Given a string formula representing a chemical formula, return the
count of each atom sorted alphabetically.

Rules:
    - An atom starts with an uppercase letter, followed by zero or
      more lowercase letters.
    - A count (optional) follows an atom or closing parenthesis.
      If no count, the count is 1.
    - Parentheses group atoms and multiply counts.

Example 1:
    Input:  formula = "H2O"
    Output: "H2O"
    Explanation: H appears 2 times, O appears 1 time.

Example 2:
    Input:  formula = "Mg(OH)2"
    Output: "H2MgO2"
    Explanation: H->2, Mg->1, O->2 (sorted alphabetically)

Example 3:
    Input:  formula = "K4(ON(SO3)2)2"
    Output: "K4N2O14S4"
    Explanation: K->4, N->2, O->14, S->4

Constraints:
    - 1 <= len(formula) <= 1000
    - formula consists of English letters, digits, '(' and ')'.
    - formula is always valid.

Hint: Use a stack of dictionaries. Push a new dict when you see '(',
      and pop/merge when you see ')'.
"""


def count_of_atoms(formula: str) -> str:
    pass


# Test cases
print(count_of_atoms("H2O"))            # Expected: "H2O"
print(count_of_atoms("Mg(OH)2"))        # Expected: "H2MgO2"
print(count_of_atoms("K4(ON(SO3)2)2"))  # Expected: "K4N2O14S4"
