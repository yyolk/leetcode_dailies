# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/


class Solution:
    """2486. Append Characters to String to Make Subsequence

    You are given two strings `s` and `t` consisting of only lowercase English letters.

    Return *the minimum number of characters that need to be appended to the end of* `s`
    *so that* `t` *becomes a **subsequence** of* `s`.

    A **subsequence** is a string that can be derived from another string by deleting
    some or no characters without changing the order of the remaining characters.

    """

    def append_characters(self, s: str, t: str) -> int:
        # Initialize a pointer for t
        t_pointer = 0
        # Iterate through each character in s
        for char in s:
            # If the current character in s matches the current character in t,
            # move the pointer in t to the next character
            if t_pointer < len(t) and char == t[t_pointer]:
                t_pointer += 1
        # The number of characters to be appended to s is the remaining characters in t
        return len(t) - t_pointer

    appendCharacters = append_characters
