# https://leetcode.com/problems/sum-of-sortable-integers/


class Solution:
    """3886. Sum of Sortable Integers

    You are given an integer array `nums` of length `n`.

    An integer `k` is called **sortable** if `k` **divides** `n` and you can
    sort `nums` in **non-decreasing** order by sequentially performing the
    following operations:

    * Partition `nums` into **consecutive subarrays** of length `k`.

    * **Cyclically rotate each subarray independently** any number of times to
    the left or to the right.

    Return an integer denoting the sum of all possible sortable integers `k`.

    Constraints:

    * `1 <= n == nums.length <= 105`

    * `1 <= nums[i] <= 105`
    """

    def sortable_integers(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        # Check every divisor k of n.
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            if self._can_sort_with_k(nums, k):
                total += k
        return total

    def _can_sort_with_k(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        prev_max = 0
        for start in range(0, n, k):
            block = nums[start : start + k]
            # Count strict descents; more than one means not a valid rotation.
            descents = 0
            for j in range(k - 1):
                if block[j] > block[j + 1]:
                    descents += 1
                    if descents > 1:
                        return False
            # If one descent, the wrap-around must also be non-increasing.
            if descents == 1 and block[-1] > block[0]:
                return False
            # Min of the sorted rotation must not violate previous max.
            curr_min = min(block)
            curr_max = max(block)
            if curr_min < prev_max:
                return False
            prev_max = curr_max
        return True

    sortableIntegers = sortable_integers
