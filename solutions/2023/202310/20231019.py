# https://leetcode.com/problems/backspace-string-compare/
from itertools import groupby


class Solution:
    """844. Backspace String Compare

    Given two strings `s` and `t`, return `true` *if they are equal when both are typed
    into empty text editors*. `'#'` means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.
    """

    def backspace_compare(self, s: str, t: str) -> bool:
        """Simulate input strings being typed with backspaces and compare them.

        Proposed solution simulating the typing in both editors.

        Args:
            s (str): Input string one.
            t (str): Input string two.

        Returns:
            bool: True if the strings, after backspaces are accounted for, are the same.
        """

        def process_string(string: str) -> list[str]:
            """Process a String by applying backspaces.

            Args:
                string (str): The input string to process.
            Returns:
                list of str: A list of characters representing the final string after
                    backspace processing.
            """

            def generate_characters():
                # Group characters in the input string, including "#",
                # then calculate their count.
                for char, group in groupby(string):
                    if char == "#":
                        # Use negative count for backspaces.
                        yield char, -sum(1 for _ in group)
                    else:
                        yield char, sum(1 for _ in group)

            result = []
            for char, count in generate_characters():
                if count < 0:
                    # Apply backspace by removing characters from the result.
                    result = result[:count]
                else:
                    # Add characters to the result based on their count.
                    result.extend([char] * count)

            return result

        # Compare the processed strings for equality.
        return process_string(s) == process_string(t)

    backspaceCompare = backspace_compare
