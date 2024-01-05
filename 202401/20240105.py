# https://leetcode.com/problems/longest-increasing-subsequence/
import bisect


class Solution:
    """300. Longest Increasing Subsequence

    Given an integer array `nums`, return *the length of the longest **strictly
    increasing*** ***subsequence***.
    """

    def length_of_l_i_s(self, nums: list[int]) -> int:
        # Initialize an empty list to store the increasing subsequence
        dp = []

        # Iterate through each element in the input array
        for n in nums:
            # Find the index where the current element should be inserted
            insert_index = bisect.bisect_left(dp, n)

            # If the insert index is at the end of dp, append the current element
            if insert_index == len(dp):
                dp.append(n)
            else:
                # If not, update the element at the insert index with the current element
                dp[insert_index] = n
        
        # The length of dp is the length of the longest increasing subsequence
        return len(dp)

    lengthOfLIS = length_of_l_i_s
