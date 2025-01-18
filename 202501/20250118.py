# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
from collections import deque


class Solution:
    """1368. Minimum Cost to Make at Least One Valid Path in a Grid

    Given an `m x n` grid. Each cell of the grid has a sign pointing to the next cell
    you should visit if you are currently in this cell. The sign of `grid[i][j]` can be:

    * `1` which means go to the cell to the right. (i.e go from `grid[i][j]` to
    `grid[i][j + 1]`)

    * `2` which means go to the cell to the left. (i.e go from `grid[i][j]` to
    `grid[i][j - 1]`)

    * `3` which means go to the lower cell. (i.e go from `grid[i][j]` to `grid[i +
    1][j]`)

    * `4` which means go to the upper cell. (i.e go from `grid[i][j]` to `grid[i -
    1][j]`)

    Notice that there could be some signs on the cells of the grid that point outside
    the grid.

    You will initially start at the upper left cell `(0, 0)`. A valid path in the grid
    is a path that starts from the upper left cell `(0, 0)` and ends at the bottom-right
    cell `(m - 1, n - 1)` following the signs on the grid. The valid path does not have
    to be the shortest.

    You can modify the sign on a cell with `cost = 1`. You can modify the sign on a cell
    **one time only**.

    Return *the minimum cost to make the grid have at least one valid path*."""

    def min_cost(self, grid: list[list[int]]) -> int:
        # Get the dimensions of the grid
        grid_height, grid_width = len(grid), len(grid[0])

        # Define movement directions: right, left, down, up
        movement_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Initialize visited array to track visited cells
        cell_visited = [[False] * grid_width for _ in range(grid_height)]

        # Start BFS from top-left with initial cost of 0
        bfs_queue = deque([(0, 0, 0)])

        while bfs_queue:
            # Get current position and cost from queue
            current_row, current_col, current_cost = bfs_queue.popleft()

            # Skip if cell already visited
            if cell_visited[current_row][current_col]:
                continue
            cell_visited[current_row][current_col] = True

            # Check if we've reached the bottom right cell
            if (current_row, current_col) == (grid_height - 1, grid_width - 1):
                return current_cost

            # Check all possible directions
            for direction_index, (delta_row, delta_col) in enumerate(movement_directions):
                new_row, new_col = current_row + delta_row, current_col + delta_col
                # If new position is within grid and not visited
                if 0 <= new_row < grid_height and 0 <= new_col < grid_width and not cell_visited[new_row][new_col]:
                    # If direction matches cell's sign, no cost increase
                    if grid[current_row][current_col] == direction_index + 1:
                        bfs_queue.appendleft((new_row, new_col, current_cost))
                    else:
                        # Add to queue with increased cost for changing direction
                        bfs_queue.append((new_row, new_col, current_cost + 1))

        # No valid path found
        return -1

    minCost = min_cost
