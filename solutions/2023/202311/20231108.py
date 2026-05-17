# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/


class Solution:
    """2849. Determine if a Cell Is Reachable at a Given Time

    You are given four integers `sx`, `sy`, `fx`, `fy`, and a **non-negative** integer
    `t`.

    In an infinite 2D grid, you start at the cell `(sx, sy)`. Each second, you **must**
    move to any of its adjacent cells.

    Return `true` *if you can reach cell* `(fx, fy)` *after **exactly*** `t`
    ***seconds***, *or* `false` *otherwise*.

    A cell's **adjacent cells** are the 8 cells around it that share at least one corner
    with it. You can visit the same cell several times.
    """

    def is_reachable_at_time(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        """Can a cell be reached within the alloted time.

        Proposed solution with mathematical observation.

        Args:
            sx: Starting point x coordinate.
            sy: Starting point y coordinate.
            fx: Finish point x coordinate.
            fy: Finish point y coordinate.
            t: Time in seconds that are alloted.

        Returns:
            True if the finished cell can be reached from the starting cell in the
            alloted time.
        """
        # If the starting and finishing cells are the same, check if t is greater than 1
        if sx == fx and sy == fy:
            if t == 1:
                # You can't stay in the same cell for exactly 1 second
                return False
            else:
                # You can stay in the same cell for t seconds
                return True

        # Check if the Manhattan distance between starting and finishing cells is less
        # than or equal to t
        return abs(sx - fx) <= t and abs(sy - fy) <= t

    isReachableAtTime = is_reachable_at_time
