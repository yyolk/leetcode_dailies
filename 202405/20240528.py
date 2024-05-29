# https://leetcode.com/problems/get-equal-substrings-within-budget/


class Solution:
    """1208. Get Equal Substrings Within Budget

    You are given two strings `s` and `t` of the same length and an integer `max_cost`.

    You want to change `s` to `t`. Changing the `ith` character of `s` to `ith`
    character of `t` costs `|s[i] - t[i]|` (i.e., the absolute difference between the
    ASCII values of the characters).

    Return *the maximum length of a substring of* `s` *that can be changed to be the
    same as the corresponding substring of* `t` *with a cost less than or equal to*
    `max_cost`. If there is no substring from `s` that can be changed to its
    corresponding substring from `t`, return `0`.

    """

    def equal_substring(self, s: str, t: str, max_cost: int) -> int:
        # Initialize variables for the sliding window
        start = 0
        max_len = 0
        current_cost = 0

        # Iterate over the string `s`
        for end in range(len(s)):
            # Calculate the cost of changing s[end] to t[end]
            current_cost += abs(ord(s[end]) - ord(t[end]))

            # If the current cost exceeds the maximum allowed cost
            while current_cost > max_cost:
                # Move the start of the window to the right
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            # Update the maximum length of the valid window
            max_len = max(max_len, end - start + 1)

        return max_len

    equalSubstring = equal_substring
