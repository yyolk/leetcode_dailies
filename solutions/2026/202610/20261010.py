# https://leetcode.com/problems/minimum-sum-of-squared-difference/


class Solution:
    """2333. Minimum Sum of Squared Difference

    You are given two positive 0-indexed integer arrays nums1 and nums2,
    both of length n.

    The sum of squared difference of arrays nums1 and nums2 is defined as
    the sum of (nums1[i] - nums2[i])^2 for each 0 <= i < n.

    You are also given two positive integers k1 and k2. You can modify any
    of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you
    can modify any of the elements of nums2 by +1 or -1 at most k2 times.

    Return the minimum sum of squared difference after modifying array
    nums1 at most k1 times and modifying array nums2 at most k2 times.

    Note: You are allowed to modify the array elements to become negative
    integers.

    Constraints:

    * n == nums1.length == nums2.length
    * 1 <= n <= 10^5
    * 0 <= nums1[i], nums2[i] <= 10^5
    * 0 <= k1, k2 <= 10^9
    """

    def min_sum_square_diff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        # Absolute differences; k1 and k2 are interchangeable.
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2
        # Enough operations to zero every difference.
        if sum(diffs) <= total_k:
            return 0

        # Binary search the smallest achievable maximum difference.
        left, right = 0, max(diffs)
        while left < right:
            mid = (left + right) // 2
            # Operations needed to bring every difference down to mid.
            ops_needed = sum(max(0, d - mid) for d in diffs)
            if ops_needed <= total_k:
                right = mid
            else:
                left = mid + 1

        # Apply the cap, tracking leftover operations.
        remaining = total_k
        final_diffs = []
        for d in diffs:
            if d > left:
                remaining -= d - left
                final_diffs.append(left)
            else:
                final_diffs.append(d)

        # Spend leftover operations reducing some values at the cap by 1.
        for i in range(len(final_diffs)):
            if remaining == 0:
                break
            if final_diffs[i] == left:
                final_diffs[i] -= 1
                remaining -= 1

        return sum(d * d for d in final_diffs)

    minSumSquareDiff = min_sum_square_diff
