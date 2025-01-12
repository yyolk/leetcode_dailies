# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/


class Solution:
    """2116. Check if a Parentheses String Can Be Valid

    A parentheses string is a **non-empty** string consisting only of `'('` and `')'`.
    It is valid if **any** of the following conditions is **true**:

    * It is `()`.

    * It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid
    parentheses strings.

    * It can be written as `(A)`, where `A` is a valid parentheses string.

    You are given a parentheses string `s` and a string `locked`, both of length `n`.
    `locked` is a binary string consisting only of `'0'`s and `'1'`s. For **each** index
    `i` of `locked`,

    * If `locked[i]` is `'1'`, you **cannot** change `s[i]`.

    * But if `locked[i]` is `'0'`, you **can** change `s[i]` to either `'('` or `')'`.

    Return `true` *if you can make `s` a valid parentheses string*. Otherwise, return
    `false`."""

    def can_be_valid(self, s: str, locked: str) -> bool:
        # Get the length of the string
        string_length = len(s)
        
        # Check if the string length is odd, which cannot make a valid parentheses string
        if string_length % 2 == 1:
            return False

        # Lists to keep track of open parentheses and unlocked positions
        open_indices = []
        unlocked_indices = []

        # Iterate through each character in the string
        for i in range(string_length):
            if locked[i] == '0':  # If position is unlocked, add to unlocked_indices
                unlocked_indices.append(i)
            elif s[i] == '(':     # If character is '(', add its index to open_indices
                open_indices.append(i)
            elif s[i] == ')':     # If character is ')', match or use an unlocked position
                if open_indices:  # Try to match with an open parenthesis
                    open_indices.pop()
                elif unlocked_indices:  # Use an unlocked position if possible
                    unlocked_indices.pop()
                else:  # If no match possible, return False
                    return False

        # Match remaining open parentheses with unlocked positions
        while open_indices and unlocked_indices and open_indices[-1] < unlocked_indices[-1]:
            open_indices.pop()
            unlocked_indices.pop()

        # If no unmatched open parentheses remain:
        if not open_indices and unlocked_indices:
            # Check if the number of remaining unlocked positions is even
            return len(unlocked_indices) % 2 == 0

        # Return true if no unmatched open parentheses left
        return not open_indices

    canBeValid = can_be_valid
