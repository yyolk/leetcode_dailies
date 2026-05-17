# https://leetcode.com/problems/move-pieces-to-obtain-a-string/


class Solution:
    """2337. Move Pieces to Obtain a String

    You are given two strings `start` and `target`, both of length `n`. Each string
    consists **only** of the characters `"L"`, `"R"`, and `"_"` where:

    * The characters `"L"` and `"R"` represent pieces, where a piece `"L"` can move to
    the **left** only if there is a **blank** space directly to its left, and a piece
    `"R"` can move to the **right** only if there is a **blank** space directly to its
    right.

    * The character `"_"` represents a blank space that can be occupied by **any** of
    the `"L"` or `"R"` pieces.

    Return `true` *if it is possible to obtain the string* `target` *by moving the
    pieces of the string* `start` ***any** number of times*. Otherwise, return `false`.
    """

    def can_change(self, start: str, target: str) -> bool:
        # Check if strings have same length and same count of blank spaces
        if len(start) != len(target) or start.count("_") != target.count("_"):
            return False

        # Create lists of non-blank characters with their indices for start string
        start_non_blanks = [
            (char, index) for index, char in enumerate(start) if char != "_"
        ]

        # Create lists of non-blank characters with their indices for target string
        target_non_blanks = [
            (char, index) for index, char in enumerate(target) if char != "_"
        ]

        # Iterate through both lists simultaneously
        for start_tuple, target_tuple in zip(start_non_blanks, target_non_blanks):
            # Unpack tuples for clarity
            start_char, start_index = start_tuple
            target_char, target_index = target_tuple

            # If characters do not match, transformation is not possible
            if start_char != target_char:
                return False

            # Check if "L" can move left (start_index should not be less than target_index)
            if start_char == "L" and start_index < target_index:
                return False

            # Check if "R" can move right (start_index should not be greater than target_index)
            if start_char == "R" and start_index > target_index:
                return False

        # If all checks pass, transformation is possible
        return True

    canChange = can_change
