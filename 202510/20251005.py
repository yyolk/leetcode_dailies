# https://leetcode.com/problems/pacific-atlantic-water-flow/


class Solution:
    """417. Pacific Atlantic Water Flow

    There is an `m x n` rectangular island that borders both the **Pacific Ocean** and
    **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges,
    and the **Atlantic Ocean** touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an `m x n`
    integer matrix `heights` where `heights[r][c]` represents the **height above sea
    level** of the cell at coordinate `(r, c)`.

    The island receives a lot of rain, and the rain water can flow to neighboring cells
    directly north, south, east, and west if the neighboring cell's height is **less
    than or equal to** the current cell's height. Water can flow from any cell adjacent
    to an ocean into the ocean.

    Return *a **2D list** of grid coordinates* `result` *where* `result[i] = [ri, ci]`
    *denotes that rain water can flow from cell* `(ri, ci)` *to **both** the Pacific and
    Atlantic oceans*."""

    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # Handle edge case for empty grid
        if not heights or not heights[0]:
            return []
        
        # Get dimensions of the grid
        m, n = len(heights), len(heights[0])
        
        # Initialize visited matrices for Pacific and Atlantic
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        
        # Define DFS function to mark reachable cells in reverse flow
        def dfs(r: int, c: int, visited: list[list[bool]]) -> None:
            # Mark current cell as visited
            visited[r][c] = True
            # Directions: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds, not visited, and height condition for reverse flow
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
        
        # Start DFS from Pacific borders: top row and left column
        for c in range(n):
            dfs(0, c, pac)
        for r in range(m):
            dfs(r, 0, pac)
        
        # Start DFS from Atlantic borders: bottom row and right column
        for c in range(n):
            dfs(m - 1, c, atl)
        for r in range(m):
            dfs(r, n - 1, atl)
        
        # Collect cells reachable from both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    result.append([r, c])
        
        return result

    pacificAtlantic = pacific_atlantic
