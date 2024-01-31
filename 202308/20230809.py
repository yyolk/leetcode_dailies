# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/


class Solution:
    """2720. Minimize the Maximum Difference of Pairs

    You are given a **0-indexed** integer array `nums` and an integer `p`. Find `p`
    pairs of indices of `nums` such that the **maximum** difference amongst all the
    pairs is **minimized**. Also, ensure no index appears more than once amongst the `p`
    pairs.

    Note that for a pair of elements at the index `i` and `j`, the difference of this
    pair is `|nums[i] - nums[j]|`, where `|x|` represents the **absolute** **value** of
    `x`.

    Return *the **minimum** **maximum** difference among all* `p` *pairs.* We define the
    maximum of an empty set to be zero.

    """

    def minimize_max(self, nums: List[int], p: int) -> int:
        # Step 1: Sort the input array
        nums.sort()
        n = len(nums)

        # Step 2: Initialize left and right pointers for binary search
        left, right = 0, nums[n - 1] - nums[0]

        # Step 3: Apply binary search to find the minimum maximum difference
        while left < right:
            mid = (left + right) // 2
            j, i = 0, 1

            # Step 4: Count the number of pairs with difference less than or equal to 'mid'
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    j += 1
                    i += 1
                i += 1

            # Step 5: Update pointers based on the count of pairs
            if j >= p:
                right = mid
            else:
                left = mid + 1

        # Step 6: Return the result
        return left

    minimizeMax = minimize_max
