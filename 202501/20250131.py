# https://leetcode.com/problems/making-a-large-island/


class Solution:
    """827. Making A Large Island

    You are given an `n x n` binary matrix `grid`. You are allowed to change **at most
    one** `0` to be `1`.

    Return *the size of the largest **island** in* `grid` *after applying this
    operation*.

    An **island** is a 4-directionally connected group of `1`s."""

    def largest_island(self, grid: list[list[int]]) -> int:
        n = len(grid)
        label = 2  # Start labeling from 2 since 0 and 1 are already used
        island_sizes = defaultdict(int)
        
        # Step 1: Label islands and calculate their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = self.dfs(grid, i, j, label)
                    island_sizes[label] = size
                    label += 1
        
        # Step 2: Calculate the maximum island size after converting one 0 to 1
        max_size = max(island_sizes.values(), default=0)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                            neighbors.add(grid[x][y])
                    current_size = 1 + sum(island_sizes[label] for label in neighbors)
                    max_size = max(max_size, current_size)
        
        return max_size
    
    def dfs(self, grid: List[List[int]], i: int, j: int, label: int) -> int:
        n = len(grid)
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        grid[i][j] = label
        size = 1
        size += self.dfs(grid, i + 1, j, label)
        size += self.dfs(grid, i - 1, j, label)
        size += self.dfs(grid, i, j + 1, label)
        size += self.dfs(grid, i, j - 1, label)
        return size

    largestIsland = largest_island
