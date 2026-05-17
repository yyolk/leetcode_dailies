# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/


class Solution:
    """154. Find Minimum in Rotated Sorted Array II

    Suppose an array of length n sorted in ascending order is rotated between 1 and n
    times. For example, the array nums = [0,1,4,4,5,6,7] might become:
    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
    the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
    Given the sorted rotated array nums that may contain duplicates, return the
    minimum element of this array.
    You must decrease the overall operation steps as much as possible.
    """

    def find_min(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # minimum must be in right half after mid
                left = mid + 1
            elif nums[mid] < nums[right]:
                # minimum is at mid or in left half
                right = mid
            else:
                # duplicates: cannot decide side, shrink right
                right -= 1
        return nums[left]

    findMin = find_min
