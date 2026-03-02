# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid

class Solution:
    """1536. Minimum Swaps to Arrange a Binary Grid

    Given an n x n binary grid, in one step you can choose two adjacent rows of
    the grid and swap them.
    A grid is said to be valid if all the cells above the main diagonal are
    zeros.
    Return the minimum number of steps needed to make the grid valid, or -1 if
    the grid cannot be valid.
    The main diagonal of a grid is the diagonal that starts at cell (1, 1) and
    ends at cell (n, n).
    """
    def min_swaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Compute rightmost 1 (0-based) for each row; row can go to pos i if <= i
        max_pos = []
        for row in grid:
            pos = -1
            for j in range(n):
                if row[j] == 1:
                    pos = j
            max_pos.append(pos)
        swaps = 0
        for i in range(n):
            # Find first j >= i where row at j can be placed at i
            for j in range(i, n):
                if max_pos[j] <= i:
                    swaps += j - i
                    # Simulate bubbling row j to i: shift i..j-1 right by 1
                    temp = max_pos[j]
                    for k in range(j, i, -1):
                        max_pos[k] = max_pos[k - 1]
                    max_pos[i] = temp
                    break
            else:
                # No suitable row found
                return -1
        return swaps

    minSwaps = min_swaps