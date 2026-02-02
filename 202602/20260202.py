# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii

class Solution:
    def minimum_cost(self, nums: list[int], k: int, dist: int) -> int:
        n = len(nums)
        s = k - 2  # Number of additional starts needed beyond the fixed one
        INF = 10**20

        # Compress values from nums[1:] for fenwick tree ranking
        unique = sorted(set(nums[1:]))
        m = len(unique)
        rank = {unique[i]: i + 1 for i in range(m)}

        class FenwickTree:
            def __init__(self, size: int):
                self.size = size
                self.tree = [0] * (size + 2)

            # Update frequency/sum at index by delta
            def update(self, idx: int, delta: int) -> None:
                while idx <= self.size:
                    self.tree[idx] += delta
                    idx += idx & -idx

            # Query prefix up to idx
            def query(self, idx: int) -> int:
                idx = min(idx, self.size)
                res = 0
                while idx > 0:
                    res += self.tree[idx]
                    idx -= idx & -idx
                return res

        ft_count = FenwickTree(m)
        ft_sum = FenwickTree(m)

        # Add a value to the structure
        def add(val: int) -> None:
            r = rank[val]
            ft_count.update(r, 1)
            ft_sum.update(r, val)

        # Remove a value from the structure
        def remove(val: int) -> None:
            r = rank[val]
            ft_count.update(r, -1)
            ft_sum.update(r, -val)

        # Query sum of the smallest 'need' values
        def get_smallest_sum(need: int) -> int:
            if ft_count.query(m) < need:
                return INF
            # Binary search for the smallest rank p where prefix count >= need
            lo, hi = 1, m
            while lo < hi:
                mi = lo + (hi - lo) // 2
                if ft_count.query(mi) >= need:
                    hi = mi
                else:
                    lo = mi + 1
            p = lo
            prev_cnt = ft_count.query(p - 1) if p > 1 else 0
            prev_sum = ft_sum.query(p - 1) if p > 1 else 0
            more = need - prev_cnt
            val = unique[p - 1]
            return prev_sum + more * val

        ans = INF
        left = 1
        right = 0
        max_start = n - k + 1

        # Iterate over possible starts i (1-based) for the second subarray
        for i in range(1, max_start + 1):
            # Extend right to the target
            target_right = min(i + dist, n - 1)
            while right < target_right:
                right += 1
                add(nums[right])
            # Shrink left to the target
            target_left = i + 1
            while left < target_left:
                remove(nums[left])
                left += 1
            # Get sum of smallest s elements in current window [left..right]
            extra = get_smallest_sum(s)
            if extra < INF:
                cost = nums[0] + nums[i] + extra
                ans = min(ans, cost)

        return ans

    minimumCost = minimum_cost