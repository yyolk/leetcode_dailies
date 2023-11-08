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
        ...

    isReachableAtTime = is_reachable_at_time
