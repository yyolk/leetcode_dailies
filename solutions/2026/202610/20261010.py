# https://leetcode.com/problems/minimum-sum-of-squared-difference/


class Solution:
    """2333. Minimum Sum of Squared Difference

    You are given two positive **0-indexed** integer arrays `nums1` and `nums2`, both of
    length `n`.

    The **sum of squared difference** of arrays `nums1` and `nums2` is defined as the
    **sum** of `(nums1[i] - nums2[i])2` for each `0 <= i < n`.

    You are also given two positive integers `k1` and `k2`. You can modify any of the
    elements of `nums1` by `+1` or `-1` at most `k1` times. Similarly, you can modify
    any of the elements of `nums2` by `+1` or `-1` at most `k2` times.

    Return *the minimum **sum of squared difference** after modifying array* `nums1` *at
    most* `k1` *times and modifying array* `nums2` *at most* `k2` *times*.

    **Note**: You are allowed to modify the array elements to become **negative**
    integers.

    Constraints:

    * `n == nums1.length == nums2.length`

    * `1 <= n <= 105`

    * `0 <= nums1[i], nums2[i] <= 105`

    * `0 <= k1, k2 <= 109`"""

    def min_sum_square_diff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        """...

        Proposed solution ...

        Args:
            nums1 (list of int): ...
            nums2 (list of int): ...
            k1 (int): ...
            k2 (int): ...

        Returns:
            int: ..."""
        ...

    minSumSquareDiff = min_sum_square_diff
