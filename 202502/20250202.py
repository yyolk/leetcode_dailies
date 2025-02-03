# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/


class Solution:
    """1752. Check if Array Is Sorted and Rotated

    Given an array `nums`, return `true` *if the array was originally sorted in non-
    decreasing order, then rotated **some** number of positions (including zero)*.
    Otherwise, return `false`.

    There may be **duplicates** in the original array.

    **Note:** An array `A` rotated by `x` positions results in an array `B` of the same
    length such that `A[i] == B[(i+x) % A.length]`, where `%` is the modulo operation.
    """

    def check(self, nums: list[int]) -> bool:
        pivot_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                pivot_count += 1

        # If there is at most one pivot, the array is sorted and rotated
        return pivot_count <= 1
