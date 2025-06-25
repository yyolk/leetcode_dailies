# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/


class Solution:
    """2040. Kth Smallest Product of Two Sorted Arrays

    Given two **sorted 0-indexed** integer arrays `nums1` and `nums2` as well as an
    integer `k`, return *the* `kth` *(**1-based**) smallest product of* `nums1[i] *
    nums2[j]` *where* `0 <= i < nums1.length` *and* `0 <= j < nums2.length`."""

    def kth_smallest_product(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> int: ...

    kthSmallestProduct = kth_smallest_product
