# https://leetcode.com/problems/longest-ideal-subsequence/


class Solution:
    """2370. Longest Ideal Subsequence

    You are given a string `s` consisting of lowercase letters and an integer `k`. We
    call a string `t` **ideal** if the following conditions are satisfied:

    * `t` is a **subsequence** of the string `s`.

    * The absolute difference in the alphabet order of every two **adjacent** letters in
    `t` is less than or equal to `k`.

    Return *the length of the **longest** ideal string*.

    A **subsequence** is a string that can be derived from another string by deleting
    some or no characters without changing the order of the remaining characters.

    **Note** that the alphabet order is not cyclic. For example, the absolute difference
    in the alphabet order of `'a'` and `'z'` is `25`, not `1`.

    """

    def longest_ideal_string(self, s: str, k: int) -> int:
        # Initialize an array to store the length of the longest ideal subsequence ending at each character
        lengths = [0] * 128  # Using 128 as the ASCII range for lowercase letters

        # Iterate through each character in the input string
        for c in s:
            # Calculate the ASCII value of the current character
            ascii_val = ord(c)
            
            # Update the length of the longest ideal subsequence ending at the current character
            lengths[ascii_val] = max(lengths[ascii_val - k : ascii_val + k + 1]) + 1

        # Return the maximum length of an ideal subsequence
        return max(lengths)

    longestIdealString = longest_ideal_string
