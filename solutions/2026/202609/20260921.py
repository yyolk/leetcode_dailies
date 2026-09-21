# https://leetcode.com/problems/find-x-value-of-array-i/


class Solution:
    """3524. Find X Value of Array I

    You are given an array of positive integers nums, and a positive integer k.

    You may perform an operation once: remove any non-overlapping prefix and
    suffix so that nums remains non-empty. The x-value is the number of ways to
    do this so that the product of the remaining elements is congruent to x
    modulo k.

    Return an array result of size k where result[x] is the x-value of nums for
    0 <= x <= k - 1.

    The chosen prefix and suffix may be empty. Equivalently, count every
    non-empty contiguous subarray by the remainder of its product modulo k.

    Constraints:

    * 1 <= nums[i] <= 10^9
    * 1 <= nums.length <= 10^5
    * 1 <= k <= 5
    """

    def result_array(self, nums: list[int], k: int) -> list[int]:
        """Count subarray products by remainder modulo k."""
        result = [0] * k
        # prev[r] = number of subarrays ending at the previous index with
        # product % k == r
        prev = [0] * k
        for num in nums:
            rem = num % k
            curr = [0] * k
            # start a new subarray at this index
            curr[rem] += 1
            # extend every subarray that ended at the previous index
            for r, cnt in enumerate(prev):
                if cnt:
                    curr[(r * rem) % k] += cnt
            for r in range(k):
                result[r] += curr[r]
            prev = curr
        return result

    resultArray = result_array
