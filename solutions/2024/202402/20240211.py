# https://leetcode.com/problems/cherry-pickup-ii/


class Solution:
    """1463. Cherry Pickup II

    You are given a `rows x cols` matrix `grid` representing a field of cherries where
    `grid[i][j]` represents the number of cherries that you can collect from the `(i,
    j)` cell.

    You have two robots that can collect cherries for you:

    * **Robot #1** is located at the **top-left corner** `(0, 0)`, and

    * **Robot #2** is located at the **top-right corner** `(0, cols - 1)`.

    Return *the maximum number of cherries collection using both robots by following the
    rules below*:

    * From a cell `(i, j)`, robots can move to cell `(i + 1, j - 1)`, `(i + 1, j)`, or
    `(i + 1, j + 1)`.

    * When any robot passes through a cell, It picks up all cherries, and the cell
    becomes an empty cell.

    * When both robots stay in the same cell, only one takes the cherries.

    * Both robots cannot move outside of the grid at any moment.

    * Both robots should reach the bottom row in `grid`.

    """

    def cherry_pickup(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Create a 3D memoization array to store results of subproblems
        memo = [[[None] * cols for _ in range(cols)] for _ in range(rows)]

        def dp(row, col1, col2):
            # Base case: reached the bottom row
            if row == rows:
                return 0

            # Check memoization
            if memo[row][col1][col2] is not None:
                return memo[row][col1][col2]

            # Collect cherries from the current cell
            cherries = grid[row][col1]
            if col1 != col2:
                cherries += grid[row][col2]

            # Explore all possible moves for both robots
            max_cherries = 0
            for move1 in range(-1, 2):
                for move2 in range(-1, 2):
                    new_col1, new_col2 = col1 + move1, col2 + move2

                    # Check if the new positions are within the grid
                    if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                        # Recursively calculate the maximum cherries
                        max_cherries = max(
                            max_cherries, dp(row + 1, new_col1, new_col2)
                        )

            # Update memoization and return the result
            memo[row][col1][col2] = max_cherries + cherries
            return memo[row][col1][col2]

        # Start the dynamic programming process
        return dp(0, 0, cols - 1)

    cherryPickup = cherry_pickup
