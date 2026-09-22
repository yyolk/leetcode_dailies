# https://leetcode.com/problems/find-x-value-of-array-ii/


class Solution:
    """3525. Find X Value of Array II

    You are given an array of positive integers nums and a positive integer k.
    You are also given a 2D array queries, where queries[i] =
    [index_i, value_i, start_i, x_i].

    You may remove any suffix from nums once so that nums stays non-empty. The
    x-value of nums for a given x is the number of ways to do this so that the
    product of the remaining elements is congruent to x modulo k.

    For each query: persist nums[index_i] = value_i, then drop the prefix
    nums[0..(start_i - 1)] and report the x-value of the leftover array for
    x_i. Prefix and suffix may be empty.

    Constraints:

    * 1 <= nums[i] <= 10^9
    * 1 <= nums.length <= 10^5
    * 1 <= k <= 5
    * 1 <= queries.length <= 2 * 10^4
    """

    def result_array(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        """Count prefix products of each queried suffix by remainder mod k."""
        n = len(nums)
        # Each node: (range_product % k, counts[r] for prefixes of this range)
        prod = [1] * (4 * n)
        cnt = [[0] * k for _ in range(4 * n)]

        def merge(p: int, left: int, right: int) -> None:
            lp, lc = prod[left], cnt[left]
            rp, rc = prod[right], cnt[right]
            prod[p] = (lp * rp) % k
            out = cnt[p]
            for r in range(k):
                out[r] = lc[r]
            # right-side prefixes ride on the full left product
            for r in range(k):
                c = rc[r]
                if c:
                    out[(lp * r) % k] += c

        def build(p: int, l: int, r: int) -> None:
            if l == r:
                rem = nums[l] % k
                prod[p] = rem
                row = cnt[p]
                for i in range(k):
                    row[i] = 0
                row[rem] = 1
                return
            m = (l + r) // 2
            build(p * 2, l, m)
            build(p * 2 + 1, m + 1, r)
            merge(p, p * 2, p * 2 + 1)

        def update(p: int, l: int, r: int, idx: int, val: int) -> None:
            if l == r:
                rem = val % k
                prod[p] = rem
                row = cnt[p]
                for i in range(k):
                    row[i] = 0
                row[rem] = 1
                return
            m = (l + r) // 2
            if idx <= m:
                update(p * 2, l, m, idx, val)
            else:
                update(p * 2 + 1, m + 1, r, idx, val)
            merge(p, p * 2, p * 2 + 1)

        # Query returns (product % k, prefix-count list) for [ql, qr]
        def query(p: int, l: int, r: int, ql: int, qr: int) -> tuple[int, list[int]]:
            if ql <= l and r <= qr:
                return prod[p], cnt[p]
            m = (l + r) // 2
            if qr <= m:
                return query(p * 2, l, m, ql, qr)
            if ql > m:
                return query(p * 2 + 1, m + 1, r, ql, qr)
            lp, lc = query(p * 2, l, m, ql, qr)
            rp, rc = query(p * 2 + 1, m + 1, r, ql, qr)
            out = lc[:]
            for rmod in range(k):
                c = rc[rmod]
                if c:
                    out[(lp * rmod) % k] += c
            return (lp * rp) % k, out

        build(1, 0, n - 1)
        ans: list[int] = []
        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            _, counts = query(1, 0, n - 1, start, n - 1)
            ans.append(counts[x])
        return ans

    resultArray = result_array
