# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

from collections import deque


class Solution:
    """2812. Find the Safest Path in a Grid

    You are given a 0-indexed 2D matrix grid of size n x n, where (r, c)
    represents a cell with thief if grid[r][c]=1 or empty if 0. Start at (0,0),
    reach (n-1,n-1) via adjacent moves. Path safeness is min over path cells of
    (min Manhattan to any thief). Return max such safeness over paths to end.
    """

    def maximum_safeness_factor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Precompute min dist to nearest thief via multi-source BFS (equals Manh.)
        dist = [[10**9] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:  # enqueue all thieves (sources with dist 0)
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 10**9:
                    dist[nx][ny] = dist[x][y] + 1  # first visit = shortest
                    q.append((nx, ny))

        # Binary search for max k where path exists using only cells with dist >=k
        def can_reach(k: int) -> bool:
            if dist[0][0] < k or dist[n - 1][n - 1] < k:  # start/end must qualify
                return False
            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visited[0][0] = True
            while q:
                x, y = q.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and not visited[nx][ny]
                        and dist[nx][ny] >= k
                    ):
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return False

        low, high = 0, min(dist[0][0], dist[n - 1][n - 1])
        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                low = mid + 1  # try higher
            else:
                high = mid - 1
        return high

    maximumSafenessFactor = maximum_safeness_factor
