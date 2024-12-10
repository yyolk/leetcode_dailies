# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/
from collections import Counter


class Solution:
    """2981. Find Longest Special Substring That Occurs Thrice I

    You are given a string `s` that consists of lowercase English letters.

    A string is called **special** if it is made up of only a single character. For
    example, the string `"abc"` is not special, whereas the strings `"ddd"`, `"zz"`, and
    `"f"` are special.

    Return *the length of the **longest special substring** of* `s` *which occurs **at
    least thrice***, *or* `-1` *if no special substring occurs at least thrice*.

    A **substring** is a contiguous **non-empty** sequence of characters within a
    string."""

    def maximum_length(self, s: str) -> int:
        # List to store all special substrings encountered
        special_substrings = []

        # Iterate through each character in the string
        for i in range(len(s)):
            # Start index for the current special substring
            current_index = i
            # Continue while we're within string bounds and characters match
            while current_index < len(s) and s[current_index] == s[i]:
                # Append the special substring from 'i' to 'current_index + 1'
                special_substrings.append(s[i:current_index + 1])
                current_index += 1

        # Count occurrences of each special substring
        substring_counter = Counter(special_substrings)
        # Variable to keep track of the maximum length of special substrings appearing thrice or more
        maximum_length_found = 0

        # Iterate through the counted substrings
        for substring, count in substring_counter.items():
            # Check if the substring occurs at least three times
            if count >= 3:
                # Update maximum_length_found if this substring's length is greater
                if len(substring) > maximum_length_found:
                    maximum_length_found = len(substring)

        # If no special substring occurs at least thrice
        if maximum_length_found == 0:
            return -1

        # Return the maximum length found
        return maximum_length_found

    maximumLength = maximum_length
