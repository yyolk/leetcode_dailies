# https://leetcode.com/problems/cyclically-rotating-a-grid/

class Solution:
    """1914. Cyclically Rotating a Grid
    
    You are given an m x n integer matrix grid, where m and n are both even
    integers, and an integer k. The matrix is composed of several layers. A
    cyclic rotation of the matrix is done by cyclically rotating each layer in
    the matrix. To cyclically rotate a layer once, each element in the layer
    will take the place of the adjacent element in the counter-clockwise
    direction. Return the matrix after applying k cyclic rotations to it.
    """
    def rotate_grid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        for l in range(min(m, n) // 2):
            top = l
            left = l
            bottom = m - 1 - l
            right = n - 1 - l
            # Collect layer elements in clockwise traversal order
            layer = []
            for c in range(left, right + 1):
                layer.append(grid[top][c])
            for r in range(top + 1, bottom + 1):
                layer.append(grid[r][right])
            for c in range(right - 1, left - 1, -1):
                layer.append(grid[bottom][c])
            for r in range(bottom - 1, top, -1):
                layer.append(grid[r][left])
            # Compute effective shift with modulo for efficiency (k up to 1e9)
            cycle_len = len(layer)
            shift = k % cycle_len
            # Left rotate the layer list to achieve counter-clockwise rotation
            rotated = layer[shift:] + layer[:shift]
            # Write back the rotated elements in same traversal order
            idx = 0
            for c in range(left, right + 1):
                grid[top][c] = rotated[idx]
                idx += 1
            for r in range(top + 1, bottom + 1):
                grid[r][right] = rotated[idx]
                idx += 1
            for c in range(right - 1, left - 1, -1):
                grid[bottom][c] = rotated[idx]
                idx += 1
            for r in range(bottom - 1, top, -1):
                grid[r][left] = rotated[idx]
                idx += 1
        return grid

    rotateGrid = rotate_grid