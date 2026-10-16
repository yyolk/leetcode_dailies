# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/


class Solution:
    """2916. Subarrays Distinct Element Sum of Squares II

    You are given a 0-indexed integer array nums.

    The distinct count of a subarray of nums is defined as:

    * Let nums[i..j] be a subarray of nums consisting of all the indices from
      i to j such that 0 <= i <= j < nums.length. Then the number of distinct
      values in nums[i..j] is called the distinct count of nums[i..j].

    Return the sum of the squares of distinct counts of all subarrays of
    nums.

    Since the answer may be very large, return it modulo 10**9 + 7.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Constraints:

    * 1 <= nums.length <= 10**5

    * 1 <= nums[i] <= 10**5
    """

    def sum_counts(self, nums: list[int]) -> int:
        # Use a Fenwick tree for range add and range sum of distinct counts.
        # When extending the right endpoint, only starts after the previous
        # occurrence of the current value gain one distinct element.
        n = len(nums)
        # Fenwick tree sized for 1-based indices up to n.
        fenwick = _FenwickTree(n + 1)
        last_seen: dict[int, int] = {}
        mod = 10**9 + 7
        total = 0
        # Current sum of squares of distinct counts for all subarrays ending
        # at the previous index.
        current_sum_squares = 0

        for i, value in enumerate(nums):
            # Previous occurrence of this value, or -1 if first time.
            prev = last_seen.get(value, -1)
            # Starts that gain a new distinct: from prev+1 to i (0-based).
            # Query the sum of current distinct counts over those starts.
            # Convert to 1-based: prev+2 to i+1.
            sum_of_counts = fenwick.range_sum(prev + 2, i + 1)
            # Number of new subarrays that gain +1 distinct.
            num_new = i - prev
            # Each gains 2*old + 1 to its square.
            current_sum_squares = (
                current_sum_squares + 2 * sum_of_counts + num_new
            ) % mod
            total = (total + current_sum_squares) % mod
            # Update the counts for those starts by +1.
            fenwick.range_add(prev + 2, i + 1, 1)
            last_seen[value] = i

        return total

    sumCounts = sum_counts


class _FenwickTree:
    """Fenwick tree supporting range add and range sum (1-based)."""

    def __init__(self, size: int) -> None:
        self.size = size
        # Two trees for the range-update range-query formula.
        self.b1 = [0] * size
        self.b2 = [0] * size

    def _add(self, tree: list[int], index: int, delta: int) -> None:
        while index < self.size:
            tree[index] += delta
            index += index & -index

    def range_add(self, left: int, right: int, delta: int) -> None:
        # Apply +delta to [left, right] inclusive (1-based).
        if left > right:
            return
        self._add(self.b1, left, delta)
        self._add(self.b1, right + 1, -delta)
        self._add(self.b2, left, delta * (left - 1))
        self._add(self.b2, right + 1, -delta * right)

    def _prefix(self, index: int) -> int:
        s1 = 0
        s2 = 0
        i = index
        while i > 0:
            s1 += self.b1[i]
            s2 += self.b2[i]
            i -= i & -i
        return s1 * index - s2

    def range_sum(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self._prefix(right) - self._prefix(left - 1)
