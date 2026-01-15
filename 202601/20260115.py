# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid


class Solution:
    """2943. Maximize Area of Square Hole in Grid

    You are given two integers n and m, and two integer arrays hBars and vBars.
    The grid has n+2 horizontal and m+2 vertical bars forming 1x1 cells.
    You may remove any subset of bars from hBars (horizontal) and vBars (vertical).
    Return the maximum possible area of a square-shaped hole after removals.
    """

    def maximize_square_hole_area(self, n: int, m: int, h_bars: list[int], v_bars: list[int]) -> int:
        # Sort the removable horizontal and vertical bars
        h_bars.sort()
        v_bars.sort()

        # Helper to find max consecutive removable bars + 1 (gap size)
        def max_gap(bars: list[int]) -> int:
            if not bars:
                return 1  # no removable → max gap of 1 (between fixed bars)
            max_count = 1
            count = 1
            for i in range(1, len(bars)):
                # consecutive removable bars differ by 1
                if bars[i] == bars[i - 1] + 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 1
            # +1 because k consecutive removable bars → (k+1) unit gap
            return max_count + 1

        # max possible square side = min of max horizontal gap and max vertical gap
        max_side = min(max_gap(h_bars), max_gap(v_bars))

        # area of the largest square hole
        return max_side * max_side

    maximizeSquareHoleArea = maximize_square_hole_area