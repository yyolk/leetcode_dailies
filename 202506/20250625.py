# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
import bisect


class Solution:
    """2040. Kth Smallest Product of Two Sorted Arrays

    Given two **sorted 0-indexed** integer arrays `nums1` and `nums2` as well as an
    integer `k`, return *the* `kth` *(**1-based**) smallest product of* `nums1[i] *
    nums2[j]` *where* `0 <= i < nums1.length` *and* `0 <= j < nums2.length`."""

    def kth_smallest_product(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> int:
        def count_less_equal(mid: int) -> int:
            """Count the number of products nums1[i] * nums2[j] <= mid."""
            count = 0
            for num2 in nums2:
                if num2 > 0:
                    # Count i where nums1[i] <= mid // num2
                    count += bisect.bisect_right(nums1, mid // num2)
                elif num2 < 0:
                    # Find smallest i where nums1[i] * num2 <= mid
                    lo, hi = 0, len(nums1) - 1
                    while lo < hi:
                        mid_i = lo + (hi - lo) // 2
                        if nums1[mid_i] * num2 > mid:
                            lo = mid_i + 1
                        else:
                            hi = mid_i
                    # Check if lo is valid and satisfies condition
                    if lo < len(nums1) and nums1[lo] * num2 <= mid:
                        count += len(nums1) - lo
                else:  # num2 == 0
                    if mid >= 0:
                        count += len(nums1)
            return count

        # Binary search range based on min and max possible products
        low, high = -10**10, 10**10
        while low < high:
            mid = low + (high - low) // 2
            if count_less_equal(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low

    kthSmallestProduct = kth_smallest_product
