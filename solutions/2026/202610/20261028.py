# https://leetcode.com/problems/minimum-xor-path-in-a-grid/


class Solution:
    """3882. Minimum XOR Path in a Grid

    You are given a 2D integer array `grid` of size `m * n`.

    You start at the **top-left** cell `(0, 0)` and want to reach the **bottom-right**
    cell `(m - 1, n - 1)`.

    At each step, you **may** move either **right or down**.

    The **cost** of a path is defined as the **bitwise XOR** of all the values in the
    cells along that path, **including** the start and end cells.

    Return the **minimum** possible XOR value among all valid paths from `(0, 0)` to `(m
    - 1, n - 1)`.

    Constraints:

    * `1 <= m == grid.length <= 1000`

    * `1 <= n == grid[i].length <= 1000`

    * `m * n <= 1000`

    * `0 <= grid[i][j] <= 1023\u200b`"""

    def min_cost(self, grid: list[list[int]]) -> int:
        """...

        Proposed solution ...

        Args:
            grid (list of list of int): ...

        Returns:
            int: ..."""
        ...

    minCost = min_cost
