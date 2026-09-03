# https://leetcode.com/problems/construct-uniform-parity-array-ii/


class Solution:
    """3876. Construct Uniform Parity Array II

    You are given an array `nums1` of `n` **distinct** integers.

    You want to construct another array `nums2` of length `n` such that the elements in
    `nums2` are either **all odd or all even**.

    For each index `i`, you must choose **exactly one** of the following (in any order):

    * `nums2[i] = nums1[i]`\u200b\u200b\u200b\u200b\u200b\u200b\u200b

    * `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`, such that `nums1[i] -
    nums1[j] >= 1`

    Return `true` if it is possible to construct such an array, otherwise return
    `false`.

    Constraints:

    * `1 <= n == nums1.length <= 105`

    * `1 <= nums1[i] <= 109`

    * `nums1` consists of distinct integers."""

    def uniform_array(self, nums1: list[int]) -> bool:
        """...

        Proposed solution ...

        Args:
            nums1 (list of int): ...

        Returns:
            bool: ..."""
        ...

    uniformArray = uniform_array
