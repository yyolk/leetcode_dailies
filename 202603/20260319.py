# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y

class Solution:
    """3212. Count Submatrices With Equal Frequency of X and Y
    
    Given a 2D character matrix grid, where grid[i][j] is either "X", "Y",
    or ".", return the number of submatrices that contain grid[0][0], have an
    equal frequency of "X" and "Y", and at least one "X".
    """
    def number_of_submatrices(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # 2D prefix sums for counts of X and Y
        prefix_x = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_y = [[0] * (n + 1) for _ in range(m + 1)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                # contribution of current cell to counts
                add_x = 1 if grid[i][j] == "X" else 0
                add_y = 1 if grid[i][j] == "Y" else 0
                
                # update prefix using inclusion-exclusion
                prefix_x[i + 1][j + 1] = (
                    prefix_x[i + 1][j] + prefix_x[i][j + 1]
                    - prefix_x[i][j] + add_x
                )
                prefix_y[i + 1][j + 1] = (
                    prefix_y[i + 1][j] + prefix_y[i][j + 1]
                    - prefix_y[i][j] + add_y
                )
                
                # check this prefix submatrix (0,0) to (i,j)
                cx = prefix_x[i + 1][j + 1]
                cy = prefix_y[i + 1][j + 1]
                if cx == cy and cx > 0:
                    ans += 1
        return ans
    
    numberOfSubmatrices = number_of_submatrices