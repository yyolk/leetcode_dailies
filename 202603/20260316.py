# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid

class Solution:
    """1878. Get Biggest Three Rhombus Sums in a Grid

    You are given an m x n integer matrix grid.
    A rhombus sum is the sum of the elements that form the border of a regular
    rhombus shape in grid. The rhombus must have the shape of a square rotated 45
    degrees with each of the corners centered in a grid cell. Below is an image of
    four valid rhombus shapes with the corresponding colored cells that should be
    included in each rhombus sum:
    Note that the rhombus can have an area of 0, which is depicted by the purple
    rhombus in the bottom right corner.
    Return the biggest three distinct rhombus sums in the grid in descending order.
    If there are less than three distinct values, return all of them.
    """
    def get_biggest_three(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        rhombus_sums = set()
        for r in range(m):
            for c in range(n):
                # single cell (k=0 rhombus)
                rhombus_sums.add(grid[r][c])
                # max k limited by distance to borders
                max_k = min(c, n - c - 1, (m - r - 1) // 2)
                for k in range(1, max_k + 1):
                    # compute border sum using four sides
                    current_sum = 0
                    # side 1: top (r,c) to right (r+k,c+k) down-right
                    for i in range(k + 1):
                        current_sum += grid[r + i][c + i]
                    # side 2: right to bottom (r+2*k,c) down-left (exclude right)
                    for i in range(1, k + 1):
                        current_sum += grid[r + k + i][c + k - i]
                    # side 3: bottom to left (r+k,c-k) up-left (exclude bottom)
                    for i in range(1, k + 1):
                        current_sum += grid[r + 2 * k - i][c - i]
                    # side 4: left to top up-right (exclude left and top)
                    for i in range(1, k):
                        current_sum += grid[r + k - i][c - k + i]
                    rhombus_sums.add(current_sum)
        # top three distinct descending (handles <3 automatically)
        return sorted(rhombus_sums, reverse=True)[:3]

    getBiggestThree = get_biggest_three