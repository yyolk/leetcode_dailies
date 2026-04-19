# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values

class Solution:
    """1855. Maximum Distance Between a Pair of Values

    You are given two non-increasing 0-indexed integer arrays nums1 and nums2.
    A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j <
    nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The
    distance of the pair is j - i. Return the maximum distance of any valid
    pair (i, j). If there are no valid pairs, return 0. An array arr is
    non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
    """
    def max_distance(self, nums_1: list[int], nums_2: list[int]) -> int:
        # two pointers exploiting non-increasing order: i only advances
        max_dist = 0
        i = 0
        n1 = len(nums_1)
        n2 = len(nums_2)
        for j in range(n2):
            # advance i while invalid (nums1[i] > nums2[j]) and still in
            # bounds for this j
            while i < n1 and i <= j and nums_1[i] > nums_2[j]:
                i += 1
            # only update if we stopped inside nums1 (i < n1 guarantees a
            # valid index exists) and i <= j
            if i < n1 and i <= j:
                max_dist = max(max_dist, j - i)
        return max_dist

    maxDistance = max_distance