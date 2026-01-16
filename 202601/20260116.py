# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field


class Solution:
    """2975. Maximum Square Area by Removing Fences From a Field

    There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n)
    containing some horizontal and vertical fences given in arrays hFences and vFences.

    Horizontal fences are from (hFences[i], 1) to (hFences[i], n) and vertical fences are
    from (1, vFences[i]) to (m, vFences[i]).

    Return the maximum area of a square field formed by removing some fences (or none),
    or -1 if impossible. Answer modulo 10^9 + 7.

    Note: Boundary fences at rows 1, m and columns 1, n cannot be removed.
    """
    def maximize_square_area(self, m: int, n: int, h_fences: list[int], v_fences: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Include boundaries and sort (deduplication via set not needed if inputs are valid)
        rows = [1] + sorted(h_fences) + [m]
        cols = [1] + sorted(v_fences) + [n]
        
        # All possible differences between horizontal lines
        row_diffs = {rows[j] - rows[i] for i in range(len(rows)) 
                                    for j in range(i + 1, len(rows))}
        
        max_side = 0
        
        # Check which differences exist in both row and column gaps
        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                diff = cols[j] - cols[i]
                if diff in row_diffs:
                    max_side = max(max_side, diff)
        
        if max_side == 0:
            return -1
            
        return (max_side * max_side) % MOD

    maximizeSquareArea = maximize_square_area