# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/
from functools import cache


class Solution:
    """3459. Length of Longest V-Shaped Diagonal Segment

    You are given a 2D integer matrix `grid` of size `n x m`, where each element is
    either `0`, `1`, or `2`.

    A **V-shaped diagonal segment** is defined as:

    * The segment starts with `1`.

    * The subsequent elements follow this infinite sequence: `2, 0, 2, 0, ...`.

    * The segment:

      + Starts **along** a diagonal direction (top-left to bottom-right, bottom-right to
    top-left, top-right to bottom-left, or bottom-left to top-right).

      + Continues the **sequence** in the same diagonal direction.

      + Makes **at most one clockwise 90-degree** **turn** to another diagonal direction
    while **maintaining** the sequence.

    ![](https://assets.leetcode.com/uploads/2025/01/11/length_of_longest3.jpg)

    Return the **length** of the **longest** **V-shaped diagonal segment**. If no valid
    segment *exists*, return 0."""

    def len_of_v_diagonal(self, grid: list[list[int]]) -> int:
        # Handle empty grid case
        if not grid or not grid[0]:
            return 0
        # Retrieve grid dimensions
        n = len(grid)
        m = len(grid[0])
        # Define the four possible diagonal directions: up-left, up-right, down-right, down-left
        deltas = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        # Memoized DFS to find the longest valid extension from current position
        @cache
        def dfs(r: int, c: int, can_turn: bool, dir_: int, next_val: int) -> int:
            # Check if position is out of bounds or doesn't match expected value
            if not (0 <= r < n and 0 <= c < m and grid[r][c] == next_val):
                return 0
            # Update the next expected value in the sequence (0 or 2)
            next_val = 0 if grid[r][c] == 2 else 2
            # Get current direction delta
            dr, dc = deltas[dir_]
            # Compute next position if continuing in the same direction
            next_r_continue = r + dr
            next_c_continue = c + dc
            if can_turn:
                # Compute the turned direction (clockwise 90 degrees)
                turn_dir = (dir_ + 1) % 4
                # Get turned direction delta
                turn_dr, turn_dc = deltas[turn_dir]
                # Compute next position after turning
                next_r_turn = r + turn_dr
                next_c_turn = c + turn_dc
                # Return 1 plus the maximum of continuing or turning (no more turns after turning)
                return 1 + max(
                    dfs(next_r_continue, next_c_continue, can_turn, dir_, next_val),
                    dfs(next_r_turn, next_c_turn, False, turn_dir, next_val),
                )
            else:
                # If no turn allowed, only continue in current direction
                return 1 + dfs(
                    next_r_continue, next_c_continue, can_turn, dir_, next_val
                )

        # Initialize the maximum length found
        max_length = 0
        # Iterate over every cell in the grid
        for i in range(n):
            for j in range(m):
                # Start segments only from cells with value 1
                if grid[i][j] == 1:
                    # Compute the maximum extension over all four possible starting directions
                    max_ext = max(
                        dfs(i + deltas[0][0], j + deltas[0][1], True, 0, 2),
                        dfs(i + deltas[1][0], j + deltas[1][1], True, 1, 2),
                        dfs(i + deltas[2][0], j + deltas[2][1], True, 2, 2),
                        dfs(i + deltas[3][0], j + deltas[3][1], True, 3, 2),
                    )
                    # Update max_length with the segment length from this starting point (at least 1)
                    max_length = max(max_length, 1 + max_ext)
        # Return the longest V-shaped diagonal segment length found
        return max_length

    lenOfVDiagonal = len_of_v_diagonal
