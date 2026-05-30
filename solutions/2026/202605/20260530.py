# https://leetcode.com/problems/block-placement-queries/


class Solution:
    """3161. Block Placement Queries

    There exists an infinite number line, with its origin at 0 and extending
    towards the positive x-axis. You are given a 2D array queries, which
    contains two types of queries: 1. For a query of type 1, queries[i] = [1,
    x]. Build an obstacle at distance x from the origin. It is guaranteed that
    there is no obstacle at distance x when the query is asked. 2. For a query
    of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a
    block of size sz anywhere in the range [0, x] on the line, such that the
    block entirely lies in the range [0, x]. A block cannot be placed if it
    intersects with any obstacle, but it may touch it. Note that you do not
    actually place the block. Queries are separate. Return a boolean array
    results, where results[i] is true if you can place the block specified in
    the ith query of type 2, and false otherwise.
    """

    def get_results(self, queries: list[list[int]]) -> list[bool]:
        # compute max position needed for segment tree size
        max_pos = 0
        for q in queries:
            for v in q[1:]:
                if v > max_pos:
                    max_pos = v
        if max_pos == 0:
            return []
        # tree stores (max_internal_gap, leftmost_obst, rightmost_obst)
        # -1 means no obstacle in this range
        tree = [(0, -1, -1) for _ in range(4 * (max_pos + 2))]

        def merge(
            a: tuple[int, int, int], b: tuple[int, int, int]
        ) -> tuple[int, int, int]:
            # merge left and right child ranges
            maxa, lma, rma = a
            maxb, lmb, rmb = b
            if lma == -1:
                return b
            if lmb == -1:
                return a
            # crossing gap between rightmost of left and leftmost of right
            crossing = lmb - rma
            maxi = max(maxa, maxb, crossing)
            return (maxi, lma, rmb)

        def update(node: int, start: int, end: int, pos: int) -> None:
            # point update when adding obstacle at pos
            if start == end:
                tree[node] = (0, pos, pos)
                return
            mid = (start + end) // 2
            if pos <= mid:
                update(2 * node, start, mid, pos)
            else:
                update(2 * node + 1, mid + 1, end, pos)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def get_query(
            node: int, start: int, end: int, ql: int, qr: int
        ) -> tuple[int, int, int]:
            # query combined info over [ql, qr]
            if ql > end or qr < start:
                return (0, -1, -1)
            if ql <= start and end <= qr:
                return tree[node]
            mid = (start + end) // 2
            lefti = get_query(2 * node, start, mid, ql, qr)
            righti = get_query(2 * node + 1, mid + 1, end, ql, qr)
            return merge(lefti, righti)

        results: list[bool] = []
        for q in queries:
            if q[0] == 1:
                # type 1: add obstacle at this position
                x = q[1]
                update(1, 0, max_pos, x)
            else:
                # type 2: compute max possible block size up to x
                x = q[1]
                sz = q[2]
                info = get_query(1, 0, max_pos, 0, x)
                maxi, lmi, rmi = info
                if lmi == -1:
                    # no obstacles in [0, x]
                    can = x >= sz
                else:
                    left_gap = lmi
                    right_gap = x - rmi
                    max_gap = max(left_gap, maxi, right_gap)
                    can = max_gap >= sz
                results.append(can)
        return results

    getResults = get_results
