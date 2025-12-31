# https://leetcode.com/problems/last-day-where-you-can-still-cross
from collections import deque


class Solution:
    """1970. Last Day Where You Can Still Cross

    Given a row x col grid, initially all land (0). Each day i (1-based), the cell
    cells[i-1] becomes water (1). Find the latest day where a path exists from any
    cell in the top row to any cell in the bottom row using only land cells and
    4-directional moves.
    """
    def latest_day_to_cross(self, row: int, col: int, cells: list[list[int]]) -> int:
        # Binary search for the last day a crossing is possible
        left, right = 0, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            # Construct grid with first 'mid' cells flooded (1 = water)
            grid = [[0] * col for _ in range(row)]
            for i in range(mid):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1
            
            # If path exists on day 'mid', try later days
            if self._can_cross(grid, row, col):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
    def _can_cross(self, grid: list[list[int]], row: int, col: int) -> bool:
        # BFS from all land cells in the top row
        visited = [[False] * col for _ in range(row)]
        q = deque()
        
        # Seed queue with all reachable top-row land cells
        for c in range(col):
            if grid[0][c] == 0:
                q.append((0, c))
                visited[0][c] = True
        
        # Standard BFS; early exit if bottom row reached
        while q:
            r, c = q.popleft()
            if r == row - 1:
                return True
            
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < row and 0 <= nc < col and
                    not visited[nr][nc] and grid[nr][nc] == 0):
                    visited[nr][nc] = True
                    q.append((nr, nc))
        
        return False

    latestDayToCross = latest_day_to_cross