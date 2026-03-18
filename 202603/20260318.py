# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k

class Solution:
    """3070. Count Submatrices with Top-Left Element and Sum Less Than k
    
    Return the number of submatrices that include grid[0][0] as top-left corner
    and whose sum is <= k.
    """
    def count_submatrices(self, grid: list[list[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        count = 0
        
        # prefix[i][j] = sum of submatrix from (0,0) to (i-1,j-1)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # build 2D prefix sum
                prefix[i][j] = (prefix[i-1][j] + 
                               prefix[i][j-1] - 
                               prefix[i-1][j-1] + 
                               grid[i-1][j-1])
                
                # every possible bottom-right corner (i-1,j-1)
                # with top-left fixed at (0,0)
                if prefix[i][j] <= k:
                    count += 1
        
        return count

    countSubmatrices = count_submatrices