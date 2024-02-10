# https://leetcode.com/problems/palindromic-substrings/


class Solution:
    """647. Palindromic Substrings

    Given a string `s`, return *the number of **palindromic substrings** in it*.

    A string is a **palindrome** when it reads the same backward as forward.

    A **substring** is a contiguous sequence of characters within the string.

    """

    def count_substrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # Create a 2D array to store whether a substring is a palindrome or not
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromic
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Check for substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1

        return count

    countSubstrings = count_substrings
