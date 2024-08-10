# https://leetcode.com/problems/regions-cut-by-slashes/


class Solution:
    """959. Regions Cut By Slashes

    An `n x n` grid is composed of `1 x 1` squares where each `1 x 1` square consists of
    a `'/'`, `'\\'`, or blank space `' '`. These characters divide the square into
    contiguous regions.

    Given the grid `grid` represented as a string array, return *the number of regions*.

    Note that backslash characters are escaped, so a `'\\'` is represented as `'\\\\'`.

    """

    def regions_by_slashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))  # Union-Find parent array

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                char = grid[i][j]
                
                # Connect the four triangles within the cell
                if char == '/':
                    # Connect top-right (1) with bottom-left (2)
                    union(index + 0, index + 3)
                    union(index + 1, index + 2)
                elif char == '\\':
                    # Connect top-left (0) with bottom-right (3)
                    union(index + 0, index + 1)
                    union(index + 2, index + 3)
                else:
                    # Connect all four triangles if the cell is blank
                    union(index + 0, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)
                
                # Connect the triangles between adjacent cells
                # Connect the right triangle of current cell with the left triangle of the right cell
                if j + 1 < n:
                    union(index + 1, 4 * (i * n + (j + 1)) + 3)
                # Connect the bottom triangle of current cell with the top triangle of the bottom cell
                if i + 1 < n:
                    union(index + 2, 4 * ((i + 1) * n + j) + 0)

        # Count the number of unique regions
        return sum(find(x) == x for x in range(4 * n * n))

    regionsBySlashes = regions_by_slashes
