# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/


class Solution:
    """2294. Partition Array Such That Maximum Difference Is K

    You are given an integer array `nums` and an integer `k`. You may partition `nums`
    into one or more **subsequences** such that each element in `nums` appears in
    **exactly** one of the subsequences.

    Return *the **minimum** number of subsequences needed such that the difference
    between the maximum and minimum values in each subsequence is **at most*** `k`*.*

    A **subsequence** is a sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining elements.
    """

    def partition_array(self, nums: list[int], k: int) -> int:
        # Handle empty array case
        if not nums:
            return 0

        # Sort the array to group elements by value
        nums.sort()

        # Initialize count of subsequences and current maximum threshold
        count = 1
        current_max = nums[0] + k

        # Iterate through sorted array
        for num in nums:
            # If current number exceeds the maximum allowed value for current subsequence
            if num > current_max:
                count += 1
                current_max = num + k

        return count

    partitionArray = partition_array
