# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


class Solution:
    """1347. Minimum Number of Steps to Make Two Strings Anagram

    You are given two strings of the same length `s` and `t`. In one step you can choose
    **any character** of `t` and replace it with **another character**.

    Return *the minimum number of steps* to make `t` an anagram of `s`.

    An **Anagram** of a string is a string that contains the same characters with a
    different (or the same) ordering.
    """

    def min_steps(self, s: str, t: str) -> int:
        # Step 1: Count occurrences of characters in both strings
        # Assuming only lowercase English letters
        count_s = [0] * 26
        count_t = [0] * 26

        for char in s:
            count_s[ord(char) - ord('a')] += 1

        for char in t:
            count_t[ord(char) - ord('a')] += 1

        # Step 2: Calculate absolute differences for each character
        steps = 0
        for i in range(26):
            steps += abs(count_s[i] - count_t[i])

        # Step 3: Return the total number of steps
        # Divide by 2 since each step involves replacing one character
        return steps // 2

    minSteps = min_steps
