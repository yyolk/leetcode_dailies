# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/


class Solution:
    """3394. Check if Grid can be Cut into Sections

    You are given an integer `n` representing the dimensions of an `n x n` grid, with
    the origin at the bottom-left corner of the grid. You are also given a 2D array of
    coordinates `rectangles`, where `rectangles[i]` is in the form `[startx, starty,
    endx, endy]`, representing a rectangle on the grid. Each rectangle is defined as
    follows:

    * `(startx, starty)`: The bottom-left corner of the rectangle.

    * `(endx, endy)`: The top-right corner of the rectangle.

    **Note** that the rectangles do not overlap. Your task is to determine if it is
    possible to make **either two horizontal or two vertical cuts** on the grid such
    that:

    * Each of the three resulting sections formed by the cuts contains **at least** one
    rectangle.

    * Every rectangle belongs to **exactly** one section.

    Return `true` if such cuts can be made; otherwise, return `false`."""

    def check_valid_cuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def can_divide_by_dimension(dim: int) -> bool:
            """
            Checks if two cuts can be made along the given dimension (0 for x, 1 for y).

            Args:
                dim (int): 0 for vertical cuts (x-axis), 1 for horizontal cuts (y-axis).

            Returns:
                bool: True if two gaps exist, False otherwise.
            """
            # Sort by starting coordinate (startx or starty)
            sorted_rects = sorted(rectangles, key=lambda r: r[dim])
            gaps = 0
            max_end = sorted_rects[0][dim + 2]  # Initial furthest end (endx or endy)

            # Iterate through remaining rectangles to find gaps
            for rect in sorted_rects[1:]:
                start = rect[dim]
                end = rect[dim + 2]

                if start >= max_end:
                    gaps += 1
                    if gaps >= 2:
                        return True  # Two gaps found, cuts are possible
                max_end = max(max_end, end)  # Update the furthest end seen

            return gaps >= 2

        # Check both vertical (x) and horizontal (y) cuts
        return can_divide_by_dimension(0) or can_divide_by_dimension(1)

    checkValidCuts = check_valid_cuts
