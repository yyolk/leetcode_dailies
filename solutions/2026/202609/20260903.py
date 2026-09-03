# https://leetcode.com/problems/construct-uniform-parity-array-ii/


class Solution:
    """3876. Construct Uniform Parity Array II

    You are given an array `nums1` of `n` **distinct** integers.

    You want to construct another array `nums2` of length `n` such that the
    elements in `nums2` are either **all odd or all even**.

    For each index `i`, you must choose **exactly one** of the following
    (in any order):

    * `nums2[i] = nums1[i]`

    * `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`, such that
    `nums1[i] - nums1[j] >= 1`

    Return `true` if it is possible to construct such an array, otherwise
    return `false`.

    Constraints:

    * `1 <= n == nums1.length <= 10^5`

    * `1 <= nums1[i] <= 10^9`

    * `nums1` consists of distinct integers.
    """

    def uniform_array(self, nums1: list[int]) -> bool:
        # Minimum has no smaller j, so its parity is forced as the target.
        mn = min(nums1)
        if mn % 2 == 1:
            # Target odd: odds keep themselves; any even subtracts the min odd.
            return True
        # Target even: every odd needs a smaller odd to subtract (to flip).
        # The smallest odd has none, so impossible unless there are no odds.
        return all(x % 2 == 0 for x in nums1)

    uniformArray = uniform_array
