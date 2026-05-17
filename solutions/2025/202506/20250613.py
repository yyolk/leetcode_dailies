# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/


class Solution:
    """2616. Minimize the Maximum Difference of Pairs

    You are given a **0-indexed** integer array `nums` and an integer `p`. Find `p`
    pairs of indices of `nums` such that the **maximum** difference amongst all the
    pairs is **minimized**. Also, ensure no index appears more than once amongst the `p`
    pairs.

    Note that for a pair of elements at the index `i` and `j`, the difference of this
    pair is `|nums[i] - nums[j]|`, where `|x|` represents the **absolute** **value** of
    `x`.

    Return *the **minimum** **maximum** difference among all* `p` *pairs.* We define the
    maximum of an empty set to be zero."""

    def minimize_max(self, nums: list[int], p: int) -> int:
        """
        Find the minimum maximum difference among p pairs of indices from nums.

        Args:
            nums (list[int]): A 0-indexed integer array
            p (int): Number of pairs to form

        Returns:
            int: Minimum maximum difference among all p pairs
        """
        # Handle edge case where no pairs are needed
        if p == 0:
            return 0

        # Sort the array to make it easier to find pairs with small differences
        nums.sort()

        # Define helper function to check if we can form p pairs with max difference <= mid
        def can_form_pairs(mid: int) -> bool:
            i = 0
            count = 0
            # Iterate through the array, trying to form pairs greedily
            while i < len(nums) - 1 and count < p:
                # Check if adjacent elements can form a pair
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 2  # Skip the next element as it's used in the pair
                else:
                    i += 1  # Move to next element if no pair is formed
            return count >= p

        # Binary search on the possible maximum difference
        left = 0
        right = nums[-1] - nums[0]  # Maximum possible difference

        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                # If we can form p pairs with this difference, try a smaller difference
                right = mid
            else:
                # If we can't, we need a larger difference
                left = mid + 1

        return left

    minimizeMax = minimize_max
