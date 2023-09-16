# https://leetcode.com/problems/path-with-minimum-effort/


class Solution:
    """1631. Path With Minimum Effort

    You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of
    size `rows x columns`, where `heights[row][col]` represents the height of cell `(row,
    col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the
    bottom-right cell, `(rows-1, columns-1)` (i.e., **0-indexed**). You can move **up**,
    **down**, **left**, or **right**, and you wish to find a route that requires the minimum
    **effort**.

    A route's **effort** is the **maximum absolute difference**in heights between two
    consecutive cells of the route.

    Return *the minimum **effort** required to travel from the top-left cell to the bottom-
    right cell.*
    """

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """Minimum effort required to travel from top-left to bottom-right

        Proposed solution using depth-first search.

        Args:
            heights (List of List of int): 2D array of a landscape of columns and rows, each
                cell is the terrain's height

        Returns:
            int: the minimum sum of effort exherted for traveling from top left to bottom right
        """
        # Get the number of rows and columns in the grid
        rows, cols = len(heights), len(heights[0])
        # Define possible movement directions (up, down, left, right)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(x, y, mid, visited):
            # Mark this cell as visited
            visited[x][y] = True

            # Determine if we reached the bottom right cell
            if x == rows - 1 and y == cols - 1:
                return True
            # Traverse the directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < rows
                    and 0 <= new_y < cols
                    and not visited[new_x][new_y]
                ):
                    # Calculate the height difference between this and the last cell
                    diff = abs(heights[new_x][new_y] - heights[x][y])
                    # Check if the height difference is within the current mid value
                    if diff <= mid:
                        # Recursively explore the next cell
                        if dfs(new_x, new_y, mid, visited):
                            # Return True when a valid path is found
                            return True
            # Return False if no valid path is found
            return False

        # Initialize the binary search range (0 to max height difference)
        low, high = 0, max(max(row) for row in heights)
        # Initialize the result to an invalid value (placeholder)
        result = -1

        while low <= high:
            # Calculate the midpoint for the binary search
            mid = (low + high) // 2
            # Initialize the visited array for DFS
            visited = [[False] * cols for _ in range(rows)]

            # Check if a valid path exists with the current mid value
            if dfs(0, 0, mid, visited):
                # Update the result with the current mid value
                result = mid
                # Adjust the binary search range for a smaller mid
                high = mid - 1
            else:
                # Adjust the binary search range for a larger mid when no valid path
                # is found
                low = mid + 1
        # Return the result, which is now the minimum effort required
        return result
