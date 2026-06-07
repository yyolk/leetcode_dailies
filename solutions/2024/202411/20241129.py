# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/
import heapq


class Solution:
    """2577. Minimum Time to Visit a Cell In a Grid

    You are given a `m x n` matrix `grid` consisting of **non-negative** integers where
    `grid[row][col]` represents the **minimum** time required to be able to visit the
    cell `(row, col)`, which means you can visit the cell `(row, col)` only when the
    time you visit it is greater than or equal to `grid[row][col]`.

    You are standing in the **top-left** cell of the matrix in the `0th` second, and you
    must move to **any** adjacent cell in the four directions: up, down, left, and
    right. Each move you make takes 1 second.

    Return *the **minimum** time required in which you can visit the bottom-right cell
    of the matrix*. If you cannot visit the bottom-right cell, then return `-1`."""

    def minimum_time(self, grid: list[list[int]]) -> int:
        # Define movement directions: down, up, right, left
        movement_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Check if we can move from the start; if not, return -1
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        # Get grid dimensions
        grid_rows, grid_columns = len(grid), len(grid[0])

        # Initialize priority queue with start position and time 0
        priority_queue = [(0, 0, 0)]

        # Initialize visited array to keep track of visited cells
        visited_cells = [[False] * grid_columns for _ in range(grid_rows)]

        while priority_queue:
            # Pop the cell with the shortest time from the priority queue
            current_time, current_row, current_column = heapq.heappop(priority_queue)

            # Check if we've reached the bottom-right cell
            if current_row == grid_rows - 1 and current_column == grid_columns - 1:
                return current_time

            # If cell already visited, skip it
            if visited_cells[current_row][current_column]:
                continue

            # Mark current cell as visited
            visited_cells[current_row][current_column] = True

            # Check all possible directions
            for delta_row, delta_column in movement_directions:
                new_row, new_column = (
                    current_row + delta_row,
                    current_column + delta_column,
                )

                # Check if new position is within grid bounds and not visited
                if (
                    0 <= new_row < grid_rows
                    and 0 <= new_column < grid_columns
                    and not visited_cells[new_row][new_column]
                ):
                    # If we can enter without waiting
                    if grid[new_row][new_column] <= current_time + 1:
                        heapq.heappush(
                            priority_queue, (current_time + 1, new_row, new_column)
                        )
                    else:
                        # Calculate time difference
                        time_difference = grid[new_row][new_column] - current_time
                        if time_difference % 2 == 1:
                            # If odd, we can enter at exactly the required time
                            heapq.heappush(
                                priority_queue,
                                (grid[new_row][new_column], new_row, new_column),
                            )
                        else:
                            # If even, wait an extra second to avoid diagonal movement issue
                            heapq.heappush(
                                priority_queue,
                                (grid[new_row][new_column] + 1, new_row, new_column),
                            )

        # If we can't reach the bottom-right cell, return -1
        return -1

    minimumTime = minimum_time
