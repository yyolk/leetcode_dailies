# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/


class Solution:
    """2918. Minimum Equal Sum of Two Arrays After Replacing Zeros

    You are given two arrays `nums1` and `nums2` consisting of positive integers.

    You have to replace **all** the `0`'s in both arrays with **strictly** positive
    integers such that the sum of elements of both arrays becomes **equal**.

    Return *the **minimum** equal sum you can obtain, or* `-1` *if it is impossible*."""

    def min_sum(self, nums1: list[int], nums2: list[int]) -> int:
        # Sum of non-zero elements and count of zeros in nums1
        s1 = sum(num for num in nums1 if num != 0)
        z1 = nums1.count(0)

        # Sum of non-zero elements and count of zeros in nums2
        s2 = sum(num for num in nums2 if num != 0)
        z2 = nums2.count(0)

        # Case 1: No zeros in either array
        if z1 == 0 and z2 == 0:
            return s1 if s1 == s2 else -1
        # Case 2: No zeros in nums1, some in nums2
        elif z1 == 0:
            return s1 if s2 + z2 <= s1 else -1
        # Case 3: No zeros in nums2, some in nums1
        elif z2 == 0:
            return s2 if s1 + z1 <= s2 else -1
        # Case 4: Zeros in both arrays
        else:
            return max(s1 + z1, s2 + z2)

    minSum = min_sum
