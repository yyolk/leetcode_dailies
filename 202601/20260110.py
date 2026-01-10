# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings


class Solution:
    """712. Minimum ASCII Delete Sum for Two Strings

    Given two strings s1 and s2, return the lowest ASCII sum of deleted
    characters to make two strings equal.
    """
    def minimum_delete_sum(self, s1: str, s2: str) -> int:
        # Swap to ensure s1 is longer or equal (minimizes dp array size)
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        # Total ASCII sums of both strings
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)

        # dp[j] will hold max ASCII sum of common subsequence for s1[:i] and s2[:j]
        dp = [0] * (len(s2) + 1)

        # Process each character in the longer string
        for i in range(len(s1)):
            prev_diag = 0
            # Process each character in the shorter string
            for j in range(len(s2)):
                # Save value from previous row (above cell)
                temp = dp[j + 1]
                if s1[i] == s2[j]:
                    # Match: add current char ASCII to previous diagonal
                    dp[j + 1] = prev_diag + ord(s1[i])
                else:
                    # No match: max from left or above
                    dp[j + 1] = max(dp[j + 1], dp[j])
                # Update diagonal for next column
                prev_diag = temp

        # Min delete sum = total - 2 * max common subsequence ASCII sum
        return total - 2 * dp[-1]

    minimumDeleteSum = minimum_delete_sum