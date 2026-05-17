# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    """4. Median of Two Sorted Arrays

    Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return
    **the median** of the two sorted arrays.

    The overall run time complexity should be `O(log (m+n))`.
    """

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """Find median of sorted arrays

        Proposed solution, with constraint the overall time complexity is O(log (m+n)).
        Uses binary search.

        Args:
            nums1 (list of int): the 1st sorted input array of numbers
            nums2 (list of int): the 2nd sorted input array of numbers

        Returns:
            float: the median of the input arrays
        """
        # Ensure nums1 is the smaller array to optimize the binary search
        if len(nums1) > len(nums2):
            # Swap the inputs
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # imin = min index, imax = max index, half_length of the sum of all elements
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            # Binary search for partition of nums1
            i = (imin + imax) // 2
            # Calculate corresponding partition of nums2
            j = half_len - i

            # Check if we need to adjust the partition
            if i < m and nums2[j - 1] > nums1[i]:
                # Increase i, because i is too small
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # Decrease i, because i is too big
                imax = i - 1
            else:
                # i is perfect, calculate median
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                # If the total number of elements is odd, return the max_of_left
                if (m + n) % 2 == 1:
                    return max_of_left

                # Calculate the minimum element on the right side of the partition
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                # Return the average of max_of_left and min_of_right for an even total
                return (max_of_left + min_of_right) / 2.0
