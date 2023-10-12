# https://leetcode.com/problems/find-in-mountain-array/


class Solution:
    """1095. Find in Mountain Array

    *(This problem is an **interactive problem**.)*

    You may recall that an array `arr` is a **mountain array** if and only if:

    * `arr.length >= 3`

    * There exists some `i` with `0 < i < arr.length - 1` such that:

            + `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`

            + `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

    Given a mountain array `mountainArr`, return the **minimum** `index` such that
    `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

    **You cannot access the mountain array directly.** You may only access the array
    using a `MountainArray` interface:

    * `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).

    * `MountainArray.length()` returns the length of the array.

    Submissions making more than `100` calls to `MountainArray.get` will be judged
    *Wrong Answer*. Also, any solutions that attempt to circumvent the judge will result
    in disqualification.


    This is MountainArray's API interface.
    You should not implement it, or speculate about its implementation

        class MountainArray:
            def get(self, index: int) -> int:
            def length(self) -> int:

    """

    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        """Find the target in the MountainArray using its interface.

        Proposed solution

        Args:
            target (int): The element to look for in thhe MountainArray.
            mountain_arr (MountainArray): The input MountainArray to search.

        Returns:
            int: The minimum index of MountainArray which is the target value.
        """
        n = mountain_arr.length()

        # Find the peak index (the highest value in the mountain)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        # Index of the peak
        peak = left

        # Search the left side of the peak
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        # Search the right side of the peak
        left, right = peak, n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1

        # Target not found
        return -1
