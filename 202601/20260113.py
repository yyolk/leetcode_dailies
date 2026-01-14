# https://leetcode.com/problems/separate-squares-i


class Solution:
    """3453. Separate Squares I

    You are given a 2D integer array squares. Each squares[i] = [xi, yi, li]
    represents the bottom-left coordinates and side length of an axis-aligned
    square.

    Find the minimum y-coordinate of a horizontal line where the total area of
    squares above the line equals the total area below the line.

    Answers within 1e-5 of the actual answer will be accepted.

    Note: Squares may overlap. Overlapping areas are counted multiple times.
    """
    def separate_squares(self, squares: list[list[int]]) -> float:
        # Handle empty or zero-area cases early
        if not squares:
            return 0.0

        events = []
        total_area = 0
        for _, y, side in squares:
            if side <= 0:
                continue
            area = side * side
            total_area += area
            # +side at bottom (start contributing to rate)
            events.append((y, side))
            # -side at top (stop contributing)
            events.append((y + side, -side))

        if total_area == 0:
            return 0.0

        half = total_area / 2.0

        # Sort events: by y ascending, then negative deltas first at ties
        events.sort()

        current_rate = 0
        current_area = 0.0
        prev_y = None
        i = 0
        n = len(events)

        while i < n:
            y = events[i][0]

            # Add contribution from previous segment if rate positive
            if prev_y is not None and y > prev_y and current_rate > 0:
                segment_area = (y - prev_y) * current_rate
                if current_area + segment_area >= half:
                    needed = half - current_area
                    return prev_y + needed / current_rate

                current_area += segment_area

            # Apply all rate changes at current y
            while i < n and events[i][0] == y:
                current_rate += events[i][1]
                i += 1

            prev_y = y

        # Fallback (should reach exactly total_area at the end)
        return float(prev_y)

    separateSquares = separate_squares