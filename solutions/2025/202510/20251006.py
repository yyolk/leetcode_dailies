# https://leetcode.com/problems/swim-in-rising-water/


class Solution:
    """778. Swim in Rising Water

    You are given an `n x n` integer matrix `grid` where each value `grid[i][j]`
    represents the elevation at that point `(i, j)`.

    It starts raining, and water gradually rises over time. At time `t`, the water level
    is `t`, meaning **any** cell with elevation less than equal to `t` is submerged or
    reachable.

    You can swim from a square to another 4-directionally adjacent square if and only if
    the elevation of both squares individually are at most `t`. You can swim infinite
    distances in zero time. Of course, you must stay within the boundaries of the grid
    during your swim.

    Return *the minimum time until you can reach the bottom right square* `(n - 1, n -
    1)` *if you start at the top left square* `(0, 0)`."""

    def swim_in_water(self, grid: list[list[int]]) -> int:
        # Get the grid size n
        n = len(grid)
        if n == 0:
            return 0

        # Define the BFS function to check if reachable at time t
        def can_reach(t: int) -> bool:
            # Skip if start cell elevation > t
            if grid[0][0] > t:
                return False
            # Use deque for BFS queue
            from collections import deque

            q = deque([(0, 0)])
            # Track visited cells
            visited = set([(0, 0)])
            # Define 4-directional moves
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while q:
                x, y = q.popleft()
                # Check if reached the end
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Validate bounds, not visited, and elevation <= t
                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and (nx, ny) not in visited
                        and grid[nx][ny] <= t
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))
            return False

        # Set binary search low to max of start and end elevations
        low = max(grid[0][0], grid[n - 1][n - 1])
        # Set high to maximum elevation in grid
        high = max(max(row) for row in grid)
        # Perform binary search for minimum t
        while low < high:
            mid = (low + high) // 2
            # If reachable at mid, try smaller t
            if can_reach(mid):
                high = mid
            # Else, need larger t
            else:
                low = mid + 1
        return low

    swimInWater = swim_in_water
