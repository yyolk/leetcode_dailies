# https://leetcode.com/problems/count-sub-islands/


class Solution:
    """1905. Count Sub Islands

    You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`'s
    (representing water) and `1`'s (representing land). An **island** is a group of
    `1`'s connected **4-directionally** (horizontal or vertical). Any cells outside of
    the grid are considered water cells.

    An island in `grid2` is considered a **sub-island** if there is an island in
    `grid1` that contains **all** the cells that make up **this** island in `grid2`.

    Return the ***number** of islands in* `grid2` *that are considered
    **sub-islands***.

    """

    def count_sub_islands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        sub_island_count = 0

        def dfs(i: int, j: int, is_sub: bool) -> bool:
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True

            # Mark as visited
            grid2[i][j] = 0

            # Check if this cell in grid1 is also land
            sub = grid1[i][j] == 1

            # Recursively check neighbors
            sub &= dfs(i + 1, j, is_sub)
            sub &= dfs(i - 1, j, is_sub)
            sub &= dfs(i, j + 1, is_sub)
            sub &= dfs(i, j - 1, is_sub)

            return sub

        for i in range(m):
            for j in range(n):
                # Found an island in grid2
                if grid2[i][j] == 1:
                    if dfs(i, j, True):
                        sub_island_count += 1

        return sub_island_count

    countSubIslands = count_sub_islands
