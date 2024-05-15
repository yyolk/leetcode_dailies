# https://leetcode.com/problems/find-the-safest-path-in-a-grid/
from collections import deque
import heapq


class Solution:
    """2812. Find the Safest Path in a Grid

    You are given a **0-indexed** 2D matrix `grid` of size `n x n`, where `(r, c)`
    represents:

    * A cell containing a thief if `grid[r][c] = 1`

    * An empty cell if `grid[r][c] = 0`

    You are initially positioned at cell `(0, 0)`. In one move, you can move to any
    adjacent cell in the grid, including cells containing thieves.

    The **safeness factor** of a path on the grid is defined as the **minimum**
    manhattan distance from any cell in the path to any thief in the grid.

    Return *the **maximum safeness factor** of all paths leading to cell* `(n - 1, n -
    1)`*.*

    An **adjacent** cell of cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c -
    1)`, `(r + 1, c)` and `(r - 1, c)` if it exists.

    The **Manhattan distance** between two cells `(a, b)` and `(x, y)` is equal to `|a -
    x| + |b - y|`, where `|val|` denotes the absolute value of val.

    """
    def __init__(self):
        # Define row direction offsets
        self.roww = [0, 0, -1, 1]

        # Define column direction offsets
        self.coll = [-1, 1, 0, 0]

    def bfs(self, grid, score, n):
        # Initialize a queue for BFS
        q = deque()

        # Initialize scores for thieves and add them to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    score[i][j] = 0
                    q.append((i, j))

        # Perform BFS to calculate safeness scores
        while q:
            x, y = q.popleft()
            s = score[x][y]

            # Check adjacent cells
            for i in range(4):
                new_x = x + self.roww[i]
                new_y = y + self.coll[i]

                if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > s + 1:
                    score[new_x][new_y] = s + 1
                    q.append((new_x, new_y))

    def maximum_safeness_factor(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            # Check if start or end cell contains a thief
            return 0

        # Initialize scores matrix
        score = [[float('inf')] * n for _ in range(n)]

        # Calculate safeness scores
        self.bfs(grid, score, n)

        # Initialize visited matrix
        vis = [[False] * n for _ in range(n)]

        # Priority queue for cell safeness
        pq = [(-score[0][0], 0, 0)]

        # Heapify the priority queue
        heapq.heapify(pq)

        while pq:
            # Pop the cell with the highest safeness
            safe, x, y = heapq.heappop(pq)
            # Convert back to positive value
            safe = -safe

            # Check if reached the end cell
            if x == n - 1 and y == n - 1:
                return safe

            # Mark cell as visited
            vis[x][y] = True

            # Check adjacent cells
            for i in range(4):
                new_x = x + self.roww[i]
                new_y = y + self.coll[i]

                if 0 <= new_x < n and 0 <= new_y < n and not vis[new_x][new_y]:
                    # Calculate minimum safeness
                    s = min(safe, score[new_x][new_y])

                    # Push cell to priority queue
                    heapq.heappush(pq, (-s, new_x, new_y))
                    # Mark cell as visited
                    vis[new_x][new_y] = True

        # Return -1 if no path found
        return -1

    maximumSafenessFactor = maximum_safeness_factor
