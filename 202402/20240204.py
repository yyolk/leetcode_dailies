# https://leetcode.com/problems/minimum-window-substring/
from collections import Counter


class Solution:
    """76. Minimum Window Substring

    Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the
    **minimum window*** ***substring*** *of* `s` *such that every character in* `t`
    *(**including duplicates**) is included in the window*. If there is no such
    substring, return *the empty string* `""`.

    The testcases will be generated such that the answer is **unique**.

    """

    def min_window(self, s: str, t: str) -> str:
        # Check if t is longer than s
        if len(s) < len(t):
            return ""

        # Initialize pointers and variables
        left, right = 0, 0
        min_len = float("inf")
        min_window = ""

        # Counter for characters in t
        t_count = Counter(t)

        # Count of characters in the current window
        current_window_count = Counter()

        # Number of unique characters in t
        required_chars = len(t_count)

        # Number of unique characters in the current window that match those in t
        formed_chars = 0

        while right < len(s):
            # Expand the window
            current_window_count[s[right]] += 1
            if (
                s[right] in t_count
                and current_window_count[s[right]] == t_count[s[right]]
            ):
                formed_chars += 1

            # Contract the window
            while formed_chars == required_chars:
                # Update the minimum window substring
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left : right + 1]

                # Contract the window from the left
                current_window_count[s[left]] -= 1
                if (
                    s[left] in t_count
                    and current_window_count[s[left]] < t_count[s[left]]
                ):
                    formed_chars -= 1

                left += 1

            # Move the right pointer to expand the window
            right += 1

        return min_window

    minWindow = min_window
