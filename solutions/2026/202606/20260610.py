# https://leetcode.com/problems/maximum-total-subarray-value-ii/

import heapq


class SparseTableRMQ:
    def __init__(self, data: list[int]):
        self.n = len(data)
        self.max_log = self.n.bit_length() + 1
        self.f_max = [[0] * self.max_log for _ in range(self.n)]
        self.f_min = [[0] * self.max_log for _ in range(self.n)]

        self.lg = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.lg[i] = self.lg[i >> 1] + 1

        for i in range(self.n):
            self.f_max[i][0] = data[i]
            self.f_min[i][0] = data[i]

        for j in range(1, self.max_log):
            for i in range(self.n - (1 << j) + 1):
                # build sparse for max
                self.f_max[i][j] = max(self.f_max[i][j - 1], self.f_max[i + (1 << (j - 1))][j - 1])
                # build sparse for min
                self.f_min[i][j] = min(self.f_min[i][j - 1], self.f_min[i + (1 << (j - 1))][j - 1])

    def query_max(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return max(self.f_max[l][k], self.f_max[r - (1 << k) + 1][k])

    def query_min(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return min(self.f_min[l][k], self.f_min[r - (1 << k) + 1][k])


class Solution:
    """3691. Maximum Total Subarray Value II

    You are given an integer array nums of length n and an integer k. You must
    select exactly k distinct non-empty subarrays nums[l..r] of nums. Subarrays
    may overlap, but the exact same subarray (same l and r) cannot be chosen
    more than once. The value of a subarray nums[l..r] is max(nums[l..r]) -
    min(nums[l..r]). The total value is the sum of the values of all chosen
    subarrays. Return the maximum possible total value you can achieve.
    Constraints: 1 <= n == nums.length <= 5*10^4, 0 <= nums[i] <= 10^9, 1 <= k
    <= min(10^5, n*(n+1)/2)
    """
    def max_total_value(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # sparse table for O(1) range max/min queries
        st = SparseTableRMQ(nums)

        # max-heap (min-heap with negatives): one entry per left endpoint
        # initially the largest for each l: [l, n-1]
        pq = []
        for l in range(n):
            val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
            heapq.heappush(pq, (-val, l, n - 1))

        ans = 0
        for _ in range(k):
            # extract current largest available range
            neg_val, l, r = heapq.heappop(pq)
            ans += -neg_val
            if r > l:
                # for this fixed l, add the next smaller r-1
                val = st.query_max(l, r - 1) - st.query_min(l, r - 1)
                heapq.heappush(pq, (-val, l, r - 1))
        return ans

    maxTotalValue = max_total_value