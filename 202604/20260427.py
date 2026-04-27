# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid

from collections import deque

class Solution:
    """1391. Check if There is a Valid Path in a Grid
    
    You are given an m x n grid. Each cell of grid represents a street. The
    street of grid[i][j] can be: 1 which means a street connecting the left
    cell and the right cell. 2 which means a street connecting the upper cell
    and the lower cell. 3 which means a street connecting the left cell and the
    lower cell. 4 which means a street connecting the right cell and the lower
    cell. 5 which means a street connecting the left cell and the upper cell. 6
    which means a street connecting the right cell and the upper cell.
    You will initially start at the street of the upper-left cell (0, 0). A
    valid path in the grid is a path that starts from the upper left cell (0,
    0) and ends at the bottom-right cell (m - 1, n - 1). The path should only
    follow the streets. Notice that you are not allowed to change any street.
    Return true if there is a valid path in the grid or false otherwise.
    """
    def has_valid_path(self, grid: list[list[int]]) -> bool:
        # Map each street type (index 1-6) to its possible outgoing (di, dj)
        # directions; empty at index 0 for convenience
        connections = [
            [],
            [(0, 1), (0, -1)],  # 1: left <-> right
            [(1, 0), (-1, 0)],  # 2: up <-> down
            [(0, -1), (1, 0)],  # 3: left <-> down
            [(0, 1), (1, 0)],   # 4: right <-> down
            [(0, -1), (-1, 0)], # 5: left <-> up
            [(0, 1), (-1, 0)]   # 6: right <-> up
        ]
        
        m, n = len(grid), len(grid[0])
        # 2D visited array (faster than set of tuples for grid access)
        visited = [[False] * n for _ in range(m)]
        
        q = deque([(0, 0)])
        visited[0][0] = True
        
        while q:
            i, j = q.popleft()
            # Destination reached via valid street connections
            if i == m - 1 and j == n - 1:
                return True
            
            # Iterate only over allowed exits from current street type
            for di, dj in connections[grid[i][j]]:
                ni, nj = i + di, j + dj
                # Neighbor in bounds and not yet visited
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    opp = (-di, -dj)
                    # Bidirectional check: neighbor must connect back
                    if opp in connections[grid[ni][nj]]:
                        visited[ni][nj] = True
                        q.append((ni, nj))
        
        return False

    hasValidPath = has_valid_path