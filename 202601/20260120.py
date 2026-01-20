# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i


class Solution:
    """3314. Construct the Minimum Bitwise Array I

    You are given an array nums consisting of n prime integers.

    You need to construct an array ans of length n, such that, for each index i,
    the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR
    (ans[i] + 1) == nums[i].

    Additionally, you must minimize each value of ans[i] in the resulting array.

    If it is not possible to find such a value for ans[i] that satisfies the
    condition, then set ans[i] = -1.
    """
    def min_bitwise_array(self, nums: list[int]) -> list[int]:
        # Initialize the result list
        ans = []
        # Process each prime in nums
        for num in nums:
            # Compute the count of trailing one bits in num's binary representation
            l = 0
            while (num >> l) & 1 == 1:
                l += 1
            # If no trailing ones, it's impossible (e.g., for 2)
            if l == 0:
                ans.append(-1)
            else:
                # Calculate the minimal value as num minus 2 raised to (l-1)
                ans.append(num - (1 << (l - 1)))
        return ans

    minBitwiseArray = min_bitwise_array