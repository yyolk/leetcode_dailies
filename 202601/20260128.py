# https://leetcode.com/problems/minimum-cost-path-with-teleportations

class Solution:
    """Minimum Cost Path with Teleportations
    
    You are given a m x n 2D integer array grid and an integer k. You start at
    the top-left cell (0, 0) and your goal is to reach the bottom-right cell
    (m - 1, n - 1).
    
    There are two types of moves available:
    
    * Normal move: You can move right or down from your current cell (i, j),
      i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is
      the value of the destination cell.
    
    * Teleportation: You can teleport from any cell (i, j), to any cell (x, y)
      such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may
      teleport at most k times.
    
    Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).
    """
    def min_cost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        # Sort all cells by decreasing value for teleport processing
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort(reverse=True)
        
        # dp[i][j]: min cost to reach (i,j) using at most current teleports
        dp = [[INF] * n for _ in range(m)]
        
        directions = [(0, 1), (1, 0)]
        
        for tele in range(k + 1):
            if tele > 0:
                # Compute arrival costs via one additional teleport
                arrival_cost = INF
                pos = 0
                total = m * n
                while pos < total:
                    val = cells[pos][0]
                    group_min = INF
                    group_cells = []
                    # Collect all cells with current value
                    while pos < total and cells[pos][0] == val:
                        _, r, c = cells[pos]
                        group_cells.append((r, c))
                        group_min = min(group_min, dp[r][c])
                        pos += 1
                    # Best cost to any cell in this value group via teleport
                    best = min(arrival_cost, group_min)
                    # Assign same arrival cost to entire group
                    for r, c in group_cells:
                        dp[r][c] = min(dp[r][c], best)
                    # Update running min for lower-value groups
                    arrival_cost = min(arrival_cost, group_min)
            
            # Starting cell always reachable with cost 0
            dp[0][0] = 0
            
            # Propagate normal moves (right/down) in topological order
            for i in range(m):
                for j in range(n):
                    if dp[i][j] == INF:
                        continue
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < m and nj < n:
                            # Cost adds the destination cell value
                            alt = dp[i][j] + grid[ni][nj]
                            if alt < dp[ni][nj]:
                                dp[ni][nj] = alt
        
        return dp[m - 1][n - 1]
    
    minCost = min_cost