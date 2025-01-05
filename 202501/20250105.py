# https://leetcode.com/problems/shifting-letters-ii/


class Solution:
    """2381. Shifting Letters II

    You are given a string `s` of lowercase English letters and a 2D integer array
    `shifts` where `shifts[i] = [starti, endi, directioni]`. For every `i`, **shift**
    the characters in `s` from the index `starti` to the index `endi` (**inclusive**)
    forward if `directioni = 1`, or shift the characters backward if `directioni = 0`.

    Shifting a character **forward** means replacing it with the **next** letter in the
    alphabet (wrapping around so that `"z"` becomes `"a"`). Similarly, shifting a
    character **backward** means replacing it with the **previous** letter in the
    alphabet (wrapping around so that `"a"` becomes `"z"`).

    Return *the final string after all such shifts to* `s` *are applied*."""

    def shifting_letters(self, s: str, shifts: list[list[int]]) -> str:
        # Convert string to list for mutation
        chars = list(s)
        n = len(chars)
        
        # Create an array to keep track of shifts for each character
        shift_counts = [0] * n
        
        # Process each shift operation
        for start, end, direction in shifts:
            shift_counts[start] += 1 if direction else -1
            if end + 1 < n:  # If end is not the last index
                shift_counts[end + 1] -= 1 if direction else -1
        
        # Apply cumulative sum to get the total shift for each character
        for i in range(1, n):
            shift_counts[i] += shift_counts[i - 1]
        
        # Apply shifts to characters
        for i in range(n):
            shift = shift_counts[i]
            # Convert char to its ASCII value, apply shift, then wrap around if necessary
            chars[i] = chr((ord(chars[i]) - ord("a") + shift) % 26 + ord("a"))
        
        return "".join(chars)

    shiftingLetters = shifting_letters
