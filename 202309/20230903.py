# https://leetcode.com/problems/unique-paths/


class Solution:
    """62. Unique Paths

    There is a robot on an `m x n` grid. The robot is initially located at the **top-left
    corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner**
    (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point
    in time.

    Given the two integers `m` and `n`, return *the number of possible unique paths that the
    robot can take to reach the bottom-right corner*.

    The test cases are generated so that the answer will be less than or equal to `2 * 109`.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        """The unique paths the robot can take

        Proposed solution, uses dynamic programming.

        Args:
            m (int): input height of grid `m x n`
            n (int): input width of grid `m x n`
        
        Returns:
            int: the number of possible unique paths that the robot can take to reach the 
                bottom-right corner
        """
        # Create a 2D DP array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]

        # Init the first row and first column to 1 since there is only one first row or column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill in the DP array using a bottom-up approach
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to a cell (i, j) 
                # is the sum of the paths from the cell above (i - 1, j)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The result is stored in dp[m-1][n-1], which represents the bottom-right corner of the grid
        return dp[m - 1][n - 1]
