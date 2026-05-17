# https://leetcode.com/problems/maximum-score-of-a-good-subarray/


class Solution:
    """1793. Maximum Score of a Good Subarray

    You are given an array of integers `nums` **(0-indexed)** and an integer `k`.

    The **score** of a subarray `(i, j)` is defined as `min(nums[i], nums[i+1], ...,
    nums[j]) * (j - i + 1)`. A **good** subarray is a subarray where `i <= k <= j`.

    Return *the maximum possible **score** of a **good** subarray.*
    """

    def maximum_score(self, nums: list[int], k: int) -> int:
        """Maximum possible score of a good subarray

        Proposed solution using bisect.

        Args:
            nums (list of int): Input integer array of nums.
            k (int): A threshold value between i and j for determining good subarrays.

        Returns:
            int: The maximum possible score of a good subarray.
        """
        # Initialize left and right indices with k
        left, right = k, k
        # Initialize min_val with the value at index k
        min_val = nums[k]
        # Initialize max_score with min_val
        max_score = min_val

        while left > 0 or right < len(nums) - 1:
            if left == 0 or (
                right < len(nums) - 1 and nums[right + 1] > nums[left - 1]
            ):
                # Expand the right side of the subarray
                right += 1
            else:
                # Expand the left side of the subarray
                left -= 1
            # Update min_val
            min_val = min(min_val, nums[left], nums[right])
            # Update max_score
            max_score = max(max_score, min_val * (right - left + 1))

        return max_score

    maximumScore = maximum_score
