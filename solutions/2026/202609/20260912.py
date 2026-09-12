# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

from bisect import bisect_left


class Solution:
    """3414. Maximum Score of Non-overlapping Intervals

    You are given a 2D integer array `intervals`, where `intervals[i] = [li, ri,
    weighti]`. Interval `i` starts at position `li` and ends at `ri`, and has a weight
    of `weighti`. You can choose *up to* 4 **non-overlapping** intervals. The **score**
    of the chosen intervals is defined as the total sum of their weights.

    Return the lexicographically smallest array of at most 4 indices from `intervals`
    with **maximum** score, representing your choice of non-overlapping intervals.

    Two intervals are said to be **non-overlapping** if they do not share any points. In
    particular, intervals sharing a left or right boundary are considered overlapping.

    Constraints:

    * `1 <= intevals.length <= 5 * 104`

    * `intervals[i].length == 3`

    * `intervals[i] = [li, ri, weighti]`

    * `1 <= li <= ri <= 109`

    * `1 <= weighti <= 109`
    """

    def maximum_weight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        # Sort by end so the latest compatible predecessor is binary-searchable.
        items = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        ends = [item[0] for item in items]

        # prev[i]: last item whose end is strictly before this start, else -1.
        prev = [bisect_left(ends, items[i][1]) - 1 for i in range(n)]

        empty = (0, ())

        def better(a: tuple, b: tuple) -> tuple:
            # Prefer higher score, then lexicographically smaller index tuple.
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] <= b[1] else b

        # dp[i][k]: best using items[:i] and at most k intervals.
        dp = [[empty] * 5 for _ in range(n + 1)]
        for i in range(1, n + 1):
            _r, _l, w, idx = items[i - 1]
            p = prev[i - 1]
            for k in range(5):
                best = dp[i - 1][k]
                if k:
                    base = dp[p + 1][k - 1] if p >= 0 else dp[0][k - 1]
                    take = (base[0] + w, tuple(sorted(base[1] + (idx,))))
                    best = better(best, take)
                dp[i][k] = best

        best = empty
        for k in range(5):
            best = better(best, dp[n][k])
        return list(best[1])

    maximumWeight = maximum_weight
