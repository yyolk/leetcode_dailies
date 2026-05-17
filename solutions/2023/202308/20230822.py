# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    """168. Excel Sheet Column Title

    Given an integer columnNumber, return its corresponding column title as it appears
    in an Excel sheet.

    For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...

    """

    def convertToTitle(self, columnNumber: int) -> str:
        """Converts an input column number to it's title.

        Proposed solution, using ord() & chr().
        Column titles are computable by mapping dividing by mapping units of 26 to
        repeating letters A-Z.

        Args:
            columnNumber (int): the requested column number

        Returns:
            str: the column number's title
        """
        result = ""
        ordA = ord("A")
        while columnNumber > 0:
            # Subtract 1 to handle 1-based indexing
            columnNumber -= 1
            # Get the remainder after dividing by 26 to determine the letter
            letter = chr(columnNumber % 26 + ordA)
            # Append the letter to the result
            result = letter + result
            # Divide the columnNumber by 26 to move to the next digit
            columnNumber //= 26
        return result
