# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii


class Solution:
    """3315. Construct the Minimum Bitwise Array II

    You are given an array nums consisting of n prime integers.

    You need to construct an array ans of length n, such that, for each index
    i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e.
    ans[i] OR (ans[i] + 1) == nums[i].

    Additionally, you must minimize each value of ans[i] in the resulting
    array.

    If it is not possible to find such a value for ans[i] that satisfies the
    condition, then set ans[i] = -1.
    """
    def min_bitwise_array(self, nums: list[int]) -> list[int]:
        # Initialize result list
        ans = []
        # Process each prime in nums
        for p in nums:
            # Compute temp as p + 1 for 2-valuation
            temp = p + 1
            # Count the highest power of 2 dividing temp
            v = 0
            while temp % 2 == 0:
                # Divide by 2 and increment count
                temp //= 2
                v += 1
            # If no division by 2 possible, impossible for this p
            if v == 0:
                ans.append(-1)
            else:
                # Calculate minimal x as p minus 2 to the power (v-1)
                ans.append(p - (1 << (v - 1)))
        return ans

    minBitwiseArray = min_bitwise_array