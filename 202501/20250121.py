# https://leetcode.com/problems/grid-game/


class Solution:
    """2017. Grid Game

    You are given a **0-indexed** 2D array `grid` of size `2 x n`, where `grid[r][c]`
    represents the number of points at position `(r, c)` on the matrix. Two robots are
    playing a game on this matrix.

    Both robots initially start at `(0, 0)` and want to reach `(1, n-1)`. Each robot may
    only move to the **right** (`(r, c)` to `(r, c + 1)`) or **down** (`(r, c)` to `(r +
    1, c)`).

    At the start of the game, the **first** robot moves from `(0, 0)` to `(1, n-1)`,
    collecting all the points from the cells on its path. For all cells `(r, c)`
    traversed on the path, `grid[r][c]` is set to `0`. Then, the **second** robot moves
    from `(0, 0)` to `(1, n-1)`, collecting the points on its path. Note that their
    paths may intersect with one another.

    The **first** robot wants to **minimize** the number of points collected by the
    **second** robot. In contrast, the **second** robot wants to **maximize** the number
    of points it collects. If both robots play **optimally**, return *the **number of
    points** collected by the **second** robot.*"""

    def grid_game(self, grid: list[list[int]]) -> int:
        # Initialize the sum of points for the top row
        total_points_top_row = sum(grid[0])

        # Initialize points for the bottom row up to current position
        points_collected_bottom_row = 0

        # Initialize max points for second robot with infinity
        max_points_second_robot = float("inf")

        # Iterate through each column
        for current_column in range(len(grid[0])):
            # Subtract current column's points from top row total
            total_points_top_row -= grid[0][current_column]

            # Update max points for second robot based on current strategy
            max_points_second_robot = min(
                max_points_second_robot,
                max(total_points_top_row, points_collected_bottom_row),
            )

            # Add current column's points to bottom row total
            points_collected_bottom_row += grid[1][current_column]

        # Return the minimum of maximum points collected by second robot
        return max_points_second_robot

    gridGame = grid_game
