# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/


class Solution:
    """995. Minimum Number of K Consecutive Bit Flips

    You are given a binary array `nums` and an integer `k`.

    A **k-bit flip** is choosing a **subarray** of length `k` from `nums` and
    simultaneously changing every `0` in the subarray to `1`, and every `1` in the
    subarray to `0`.

    Return *the minimum number of **k-bit flips** required so that there is no* `0` *in
    the array*. If it is not possible, return `-1`.

    A **subarray** is a **contiguous** part of an array.

    """

    def min_k_bit_flips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        # To keep track of flip operations
        flips = [0] * n
        # Current flip state
        flip = 0

        for i in range(n):
            # Update current flip state based on previous flips
            if i >= k:
                flip ^= flips[i - k]

            # If nums[i] is 0 and the current flip state is 0, we need to flip
            if nums[i] == flip:
                # If flipping is not possible
                if i + k > n:
                    return -1
                # Mark the flip
                flips[i] = 1
                flip ^= 1
                flip_count += 1

        return flip_count

    minKBitFlips = min_k_bit_flips
