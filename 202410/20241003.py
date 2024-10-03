# https://leetcode.com/problems/make-sum-divisible-by-p/


class Solution:
    """1590. Make Sum Divisible by P

    Given an array of positive integers `nums`, remove the **smallest** subarray
    (possibly **empty**) such that the **sum** of the remaining elements is divisible by
    `p`. It is **not** allowed to remove the whole array.

    Return *the length of the smallest subarray that you need to remove, or* `-1` *if
    it's impossible*.

    A **subarray** is defined as a contiguous block of elements in the array.

    """

    def min_subarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        total = sum(nums)
        if total % p == 0:
            return 0

        # We need to find the smallest subarray with sum % p == total % p
        target = total % p
        current_sum = 0
        # Map remainder to the last index it was seen
        last_seen = {0: -1}
        # Initialize with worst case
        min_length = n

        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            if (current_sum - target) % p in last_seen:
                min_length = min(min_length, i - last_seen[(current_sum - target) % p])

            # Update the last seen index for current remainder
            last_seen[current_sum] = i

        # If min_length is still n, it means we couldn't find any subarray to remove
        return min_length if min_length < n else -1

    minSubarray = min_subarray
