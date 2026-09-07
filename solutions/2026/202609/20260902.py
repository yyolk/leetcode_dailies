# https://leetcode.com/problems/construct-uniform-parity-array-i/


class Solution:
    """3875. Construct Uniform Parity Array I

    You are given an array `nums1` of `n` **distinct** integers.

    You want to construct another array `nums2` of length `n` such that the
    elements in `nums2` are either **all odd or all even**.

    For each index `i`, you must choose **exactly one** of the following (in any
    order):

    * `nums2[i] = nums1[i]`

    * `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`

    Return `true` if it is possible to construct such an array, otherwise,
    return `false`.

    Constraints:

    * `1 <= n == nums1.length <= 100`

    * `1 <= nums1[i] <= 100`

    * `nums1` consists of distinct integers.
    """

    def uniform_array(self, nums1: list[int]) -> bool:
        # Always possible: all-even or all-odd keeps the array as-is; mixed
        # parity allows subtracting opposite-parity values to make everything
        # odd (odd-even=odd, even-odd=odd). n=1 is trivially uniform.
        return True

    uniformArray = uniform_array
