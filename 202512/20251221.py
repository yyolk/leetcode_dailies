# https://leetcode.com/problems/delete-columns-to-make-sorted-ii


class Solution:
    """955. Delete Columns to Make Sorted II

    Given n strings of equal length, find the minimum number of columns to delete
    so that the remaining strings are in lexicographic order.
    """
    def min_deletion_size(self, strs: list[str]) -> int:
        if not strs:
            return 0
        n = len(strs)
        m = len(strs[0])

        # ans tracks the minimum deletions needed
        ans = 0

        # active[i] is True if strs[i] and strs[i+1] are currently non-decreasing
        # using only the columns kept so far
        active = [False] * (n - 1)

        for col in range(m):
            # Try keeping this column: check if it violates any pair that is
            # not yet decided (active[j] == False)
            can_keep = True
            for i in range(n - 1):
                if not active[i] and strs[i][col] > strs[i + 1][col]:
                    can_keep = False
                    break

            if can_keep:
                # Keep the column: update decided pairs where equality holds
                for i in range(n - 1):
                    if not active[i] and strs[i][col] < strs[i + 1][col]:
                        active[i] = True
            else:
                # Must delete this column
                ans += 1

            # Early exit: all consecutive pairs are decided
            if all(active):
                break

        return ans

    minDeletionSize = min_deletion_size