# https://leetcode.com/problems/minimum-common-value/

class Solution:
    """2540. Minimum Common Value
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the
    minimum integer common to both arrays. If there is no common integer amongst nums1
    and nums2, return -1.

    Note that an integer is said to be common to nums1 and nums2 if both arrays have at
    least one occurrence of that integer.

    """

    def get_common(self, nums1: list[int], nums2: list[int]) -> int:
        # Initialize pointers for both arrays
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            # Check if the current elements in both arrays are equal
            if nums1[i] == nums2[j]:
                return nums1[i]  # Common element found

            # Move the pointer of the array with the smaller element
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1  # No common element found

    getCommon = get_common
 