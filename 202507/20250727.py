# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/


class Solution:
    """2210. Count Hills and Valleys in an Array

    You are given a **0-indexed** integer array `nums`. An index `i` is part of a
    **hill** in `nums` if the closest non-equal neighbors of `i` are smaller than
    `nums[i]`. Similarly, an index `i` is part of a **valley** in `nums` if the closest
    non-equal neighbors of `i` are larger than `nums[i]`. Adjacent indices `i` and `j`
    are part of the **same** hill or valley if `nums[i] == nums[j]`.

    Note that for an index to be part of a hill or valley, it must have a non-equal
    neighbor on **both** the left and right of the index.

    Return *the number of hills and valleys in* `nums`."""

    def count_hill_valley(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        count = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            # Plateau from i to j-1
            if i > 0 and j < n:
                left = nums[i - 1]
                val = nums[i]
                right = nums[j]
                if left < val and val > right:
                    count += 1
                elif left > val and val < right:
                    count += 1
            i = j
        return count

    countHillValley = count_hill_valley
