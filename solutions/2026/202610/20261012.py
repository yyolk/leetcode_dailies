# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/


class Solution:
    """2897. Apply Operations on Array to Maximize Sum of Squares

    You are given a 0-indexed integer array nums and a positive integer k.

    You can do the following operation on the array any number of times:

    * Choose any two distinct indices i and j and simultaneously update the
    values of nums[i] to (nums[i] AND nums[j]) and nums[j] to (nums[i] OR
    nums[j]). Here, OR denotes the bitwise OR operation, and AND denotes the
    bitwise AND operation.

    You have to choose k elements from the final array and calculate the sum of
    their squares.

    Return the maximum sum of squares you can achieve.

    Since the answer can be very large, return it modulo 10**9 + 7.

    Constraints:

    * 1 <= k <= nums.length <= 10**5

    * 1 <= nums[i] <= 10**9
    """

    def max_sum(self, nums: list[int], k: int) -> int:
        # Operations preserve per-bit counts and allow free redistribution of bits.
        # Maximize sum of squares of k numbers by assigning each bit to as many of
        # the top numbers as possible (up to min(count, k)).
        mod = 1_000_000_007
        bit_counts = [0] * 30
        for num in nums:
            for bit in range(30):
                if num & (1 << bit):
                    bit_counts[bit] += 1

        result = 0
        for _ in range(k):
            value = 0
            for bit in range(30):
                if bit_counts[bit] > 0:
                    value |= 1 << bit
                    bit_counts[bit] -= 1
            result = (result + value * value) % mod
        return result

    maxSum = max_sum
