# https://leetcode.com/problems/delete-columns-to-make-sorted-iii


class Solution:
    """960. Delete Columns to Make Sorted III

    Given n strings of equal length, find the minimum number of columns to
    delete so that in every remaining row, characters are non-decreasing.
    Return that minimum number of deletions.
    """
    def min_deletion_size(self, strs: list[str]) -> int:
        if not strs:
            return 0
        
        m, n = len(strs), len(strs[0])          # m rows, n columns
        
        # dp[j] = length of longest non-decreasing subsequence ending at column j
        dp = [1] * n
        
        # Consider columns in order; for each j, check all previous i < j
        for j in range(1, n):
            for i in range(j):
                # Check if column i can precede column j:
                # for every row, strs[row][i] <= strs[row][j]
                if all(strs[row][i] <= strs[row][j] for row in range(m)):
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # Longest sequence of columns we can keep
        max_keep = max(dp)
        
        # Minimum columns to delete
        return n - max_keep

    minDeletionSize = min_deletion_size