# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

import collections
import heapq


class Solution:
    """3505. Minimum Operations to Make Elements Within K Subarrays Equal

    You are given an integer array `nums` and two integers, `x` and `k`.
    You can perform the following operation any number of times
    (including zero):

    * Increase or decrease any element of `nums` by 1.

    Return the minimum number of operations needed to have at least `k`
    non-overlapping subarrays of size exactly `x` in `nums`, where all
    elements within each subarray are equal.

    Constraints:

    * `2 <= nums.length <= 10**5`
    * `-10**6 <= nums[i] <= 10**6`
    * `2 <= x <= nums.length`
    * `1 <= k <= 15`
    * `2 <= k * x <= nums.length`
    """

    def min_operations(self, nums: list[int], x: int, k: int) -> int:
        # Lazy-deletion heap that tracks a running sum of live elements.
        class LazyHeap:
            def __init__(self, sign: int):
                self.heap: list[int] = []
                self.to_remove: dict[int, int] = collections.defaultdict(int)
                self.cnt = 0  # number of pending removals
                self.sign = sign  # +1 min-heap, -1 max-heap

            def push(self, val: int) -> None:
                heapq.heappush(self.heap, self.sign * val)

            def _full_remove(self) -> None:
                # Rebuild the heap, discarding all marked-for-removal items.
                result = []
                for item in self.heap:
                    if item in self.to_remove:
                        self.to_remove[item] -= 1
                        if self.to_remove[item] == 0:
                            del self.to_remove[item]
                    else:
                        result.append(item)
                self.heap[:] = result
                heapq.heapify(self.heap)

            def remove(self, val: int) -> None:
                self.to_remove[self.sign * val] += 1
                self.cnt += 1
                # Periodically rebuild to keep the heap size bounded.
                if self.cnt > len(self.heap) - self.cnt:
                    self._full_remove()
                    self.cnt = 0

            def pop(self) -> None:
                self.remove(self.top())

            def top(self) -> int:
                # Discard any invalid tops before returning.
                while self.heap and self.heap[0] in self.to_remove:
                    self.to_remove[self.heap[0]] -= 1
                    self.cnt -= 1
                    if self.to_remove[self.heap[0]] == 0:
                        del self.to_remove[self.heap[0]]
                    heapq.heappop(self.heap)
                return self.sign * self.heap[0]

            def __len__(self) -> int:
                return len(self.heap) - self.cnt

        # Sliding-window median maintained by two heaps + running sums.
        class SlidingWindow:
            def __init__(self):
                self.left = LazyHeap(-1)  # max-heap of the lower half
                self.right = LazyHeap(+1)  # min-heap of the upper half
                self.total1 = 0  # sum of lower half
                self.total2 = 0  # sum of upper half

            def add(self, val: int) -> None:
                if not self.left or val <= self.left.top():
                    self.left.push(val)
                    self.total1 += val
                else:
                    self.right.push(val)
                    self.total2 += val
                self._rebalance()

            def remove(self, val: int) -> None:
                if val <= self.left.top():
                    self.left.remove(val)
                    self.total1 -= val
                else:
                    self.right.remove(val)
                    self.total2 -= val
                self._rebalance()

            def _rebalance(self) -> None:
                # Keep |lower| >= |upper| and difference at most 1.
                if len(self.left) < len(self.right):
                    val = self.right.top()
                    self.total2 -= val
                    self.total1 += val
                    self.left.push(val)
                    self.right.pop()
                elif len(self.left) > len(self.right) + 1:
                    val = self.left.top()
                    self.total1 -= val
                    self.total2 += val
                    self.right.push(val)
                    self.left.pop()

            def median(self) -> int:
                return self.left.top()

        n = len(nums)
        INF = float("inf")
        # cost[i+1] = min ops to equalize the window nums[i-x+1 .. i]
        cost = [INF] * (n + 1)
        sw = SlidingWindow()
        for i in range(n):
            if i >= x:
                sw.remove(nums[i - x])
            sw.add(nums[i])
            if i >= x - 1:
                med = sw.median()
                # Sum of absolute deviations from the median.
                cost[i + 1] = (
                    med * len(sw.left) - sw.total1 + sw.total2 - med * len(sw.right)
                )

        # DP: dp[j] = min cost to place the current number of windows
        # using the first j elements.
        dp = [0] * (n + 1)
        for _ in range(k):
            new_dp = [INF] * (n + 1)
            for j in range((_ + 1) * x, n + 1):
                # Either skip position j-1 or place a window ending at j-1.
                new_dp[j] = min(new_dp[j - 1], dp[j - x] + cost[j])
            dp = new_dp
        return int(dp[-1])

    minOperations = min_operations
