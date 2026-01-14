# https://leetcode.com/problems/separate-squares-ii


class Solution:
    """3454. Separate Squares II

    You are given a 2D integer array squares. Each squares[i] = [xi, yi, li]
    represents the bottom-left coordinates and side length of an axis-aligned
    square.

    Return the minimum y-coordinate of a horizontal line where the union area
    strictly above the line equals the union area strictly below the line.
    Overlaps count once. Answer within 1e-5 error is accepted.
    """

    def separate_squares(self, squares: list[list[int]]) -> float:
        # Collect all x-coordinates for compression
        xs_set = set()
        events = []
        for x, y, l in squares:
            xs_set.add(x)
            xs_set.add(x + l)
            events.append((y, 1, x, x + l))      # start event
            events.append((y + l, -1, x, x + l))  # end event

        xs = sorted(xs_set)
        x_to_idx = {v: i for i, v in enumerate(xs)}

        # Segment tree for active x-union length
        class SegmentTree:
            def __init__(self, xs):
                self.n = len(xs) - 1
                self.tree = [0] * (4 * (self.n + 1))      # cover count
                self.covered = [0] * (4 * (self.n + 1))   # union length
                self.total_len = [0] * (4 * (self.n + 1))  # full length
                if self.n > 0:
                    self._build(1, 0, self.n - 1, xs)

            def _build(self, node, start, end, xs):
                if start == end:
                    self.total_len[node] = xs[start + 1] - xs[start]
                    return
                mid = (start + end) // 2
                self._build(2 * node, start, mid, xs)
                self._build(2 * node + 1, mid + 1, end, xs)
                self.total_len[node] = (self.total_len[2 * node] +
                                        self.total_len[2 * node + 1])

            def _recalc(self, node, start, end):
                if self.tree[node] > 0:
                    self.covered[node] = self.total_len[node]
                else:
                    if start == end:
                        self.covered[node] = 0
                    else:
                        self.covered[node] = (self.covered[2 * node] +
                                              self.covered[2 * node + 1])

            def update(self, node, start, end, l, r, val):
                if l > end or r < start:
                    return
                if l <= start and end <= r:
                    self.tree[node] += val
                    self._recalc(node, start, end)
                    return
                mid = (start + end) // 2
                self.update(2 * node, start, mid, l, r, val)
                self.update(2 * node + 1, mid + 1, end, l, r, val)
                self._recalc(node, start, end)

        # Sort events: y asc, starts before ends
        events.sort(key=lambda e: (e[0], -e[1]))

        # First pass: compute total union area
        seg = SegmentTree(xs)
        active_len = 0
        prev_y = None
        total_area = 0
        for y, delta, left, right in events:
            if prev_y is not None and y > prev_y:
                # Add area of strip [prev_y, y)
                total_area += (y - prev_y) * active_len
            l_idx = x_to_idx[left]
            r_idx = x_to_idx[right]
            if l_idx < r_idx:
                seg.update(1, 0, seg.n - 1, l_idx, r_idx - 1, delta)
            active_len = seg.covered[1]
            prev_y = y

        target = total_area / 2

        # Second pass: find minimum h where area below h == target
        seg = SegmentTree(xs)
        active_len = 0
        prev_y = None
        cum_area = 0.0
        for y, delta, left, right in events:
            if prev_y is not None and y > prev_y:
                if active_len > 0:
                    strip_area = (y - prev_y) * active_len
                    if cum_area + strip_area >= target:
                        # Partial strip needed
                        needed = target - cum_area
                        return prev_y + needed / active_len
                    cum_area += strip_area
            # Apply event
            l_idx = x_to_idx[left]
            r_idx = x_to_idx[right]
            if l_idx < r_idx:
                seg.update(1, 0, seg.n - 1, l_idx, r_idx - 1, delta)
            active_len = seg.covered[1]
            prev_y = y

        # Fallback (should not reach due to constraints)
        return float(prev_y)

    separateSquares = separate_squares