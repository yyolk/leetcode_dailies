# https://leetcode.com/problems/minimum-common-value

class Solution:
    """2540. Minimum Common Value
    
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    return the minimum integer common to both arrays. If there is no common
    integer amongst nums1 and nums2, return -1.
    
    Note that an integer is said to be common to nums1 and nums2 if both
    arrays have at least one occurrence of that integer.
    """
    def get_common(self, nums1: list[int], nums2: list[int]) -> int:
        # two pointers for O(n + m) time and O(1) space on sorted arrays
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            # first equal value found is the minimum common
            if nums1[i] == nums2[j]:
                return nums1[i]
            # advance pointer of smaller current value
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        # no common value after exhausting one array
        return -1

    getCommon = get_common