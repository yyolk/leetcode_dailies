# https://leetcode.com/problems/delete-columns-to-make-sorted


class Solution:
    """944. Delete Columns to Make Sorted

    You are given an array of n strings strs, all of the same length.

    The strings form a grid where you delete unsorted columns
    lexicographically. Return the number of columns to delete.
    """
    def min_deletion_size(self, strs: list[str]) -> int:
        if not strs:
            return 0
        
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        delete_count = 0
        # Iterate over each column index
        for col in range(num_cols):
            # Check if column is non-decreasing from top to bottom
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break  # Column is unsorted, no need to check further rows
        
        return delete_count

    minDeletionSize = min_deletion_size