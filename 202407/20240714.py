# https://leetcode.com/problems/number-of-atoms/
import collections


class Solution:
    """726. Number of Atoms

    Given a string `formula` representing a chemical formula, return *the count of each
    atom*.

    The atomic element always starts with an uppercase character, then zero or more
    lowercase letters, representing the name.

    One or more digits representing that element"s count may follow if the count is
    greater than `1`. If the count is `1`, no digits will follow.

    * For example, `"H2O"` and `"H2O2"` are possible, but `"H1O2"` is impossible.

    Two formulas are concatenated together to produce another formula.

    * For example, `"H2O2He3Mg4"` is also a formula.

    A formula placed in parentheses, and a count (optionally added) is also a formula.

    * For example, `"(H2O2)"` and `"(H2O2)3"` are formulas.

    Return the count of all elements as a string in the following form: the first name
    (in sorted order), followed by its count (if that count is more than `1`), followed
    by the second name (in sorted order), followed by its count (if that count is more
    than `1`), and so on.

    The test cases are generated so that all the values in the output fit in a
    **32-bit** integer.

    """

    def count_of_atoms(self, formula: str) -> str:
        stack = [collections.defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == "(":
                # Push a new dict to the stack when encountering "("
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ")":
                # Process the closing parenthesis
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                
                # Pop the top dict and merge it into the previous one with the multiplier
                top = stack.pop()
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplier
            else:
                # Read the element name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]
                
                # Read the count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                
                # Add the element count to the top dict
                stack[-1][elem] += count
        
        # The result is in the first dictionary
        result = stack.pop()
        # Sort the elements by name and format the result string
        return "".join(f"{elem}{(count if count > 1 else '')}" for elem, count in sorted(result.items()))

    countOfAtoms = count_of_atoms
