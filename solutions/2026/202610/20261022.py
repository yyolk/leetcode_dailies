# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/


class Solution:
    """3942. Minimum Operations to Sort a Permutation

    You are given an integer array nums of length n, where nums is a
    permutation of the integers from 0 to n - 1.

    You may perform only the following operations:

    * Reverse the entire array.

    * Rotate Left by One: Move the first element to the end of the array,
      and rest elements to left by one position.

    Return an integer denoting the minimum number of operations required
    to sort the array in increasing order. If it is not possible to sort
    the array using only the given operations, return -1.

    Constraints:

    * 1 <= n == nums.length <= 10^5

    * 0 <= nums[i] <= n - 1

    * nums is a permutation of integers from 0 to n - 1.
    """

    def min_operations(self, nums: list[int]) -> int:
        n = len(nums)
        # Locate the position of 0.
        zero = nums.index(0)

        def is_sorted_cyclic(step: int) -> bool:
            # Check if values increase (or decrease for step=-1) along the cycle.
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True

        ans = float("inf")
        # Case: already in increasing cyclic order from 0.
        if is_sorted_cyclic(1):
            # Direct left-rotates to bring 0 to front.
            ans = min(ans, zero)
            # Reverse, rotate the other way, reverse back.
            ans = min(ans, n - zero + 2)
        # Case: decreasing cyclic order from 0.
        if is_sorted_cyclic(-1):
            # Rotate to put 0 at end, then reverse.
            ans = min(ans, zero + 2)
            # Reverse first, then rotate to bring 0 to front.
            ans = min(ans, n - zero)

        return -1 if ans == float("inf") else int(ans)

    minOperations = min_operations
