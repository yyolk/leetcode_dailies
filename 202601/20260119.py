# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold


class Solution:
    """1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

    Given a m x n matrix mat and an integer threshold, return the maximum side-length
    of a square with a sum less than or equal to threshold or return 0 if there is no
    such square.
    """
    def max_side_length(self, mat: list[list[int]], threshold: int) -> int:
        if not mat or not mat[0]:
            return 0
            
        m, n = len(mat), len(mat[0])
        
        # Build 2D prefix sum (prefix[i+1][j+1] = sum of mat[0..i][0..j])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (prefix[i + 1][j] + prefix[i][j + 1] -
                                       prefix[i][j] + mat[i][j])
        
        def square_sum(r1, c1, side):
            # sum of square from (r1,c1) to (r1+side-1, c1+side-1)
            r2, c2 = r1 + side, c1 + side
            return (prefix[r2][c2] - prefix[r2][c1] -
                    prefix[r1][c2] + prefix[r1][c1])
        
        # Binary search on possible side length
        left, right = 0, min(m, n)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            found = False
            
            # Check if any square of side mid exists with sum <= threshold
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if square_sum(i, j, mid) <= threshold:
                        found = True
                        break
                if found:
                    break
                    
            if found:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

    maxSideLength = max_side_length