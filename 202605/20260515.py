# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    """153. Find Minimum in Rotated Sorted Array

    Suppose an array of length n sorted in ascending order is rotated between 1
    and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
    in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
    Given the sorted rotated array nums of unique elements, return the minimum
    element of this array.
    You must write an algorithm that runs in O(log n) time.
    """

    def find_min(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # if nums[mid] > nums[right], rotation pivot is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # else, minimum is at mid or in left half
            else:
                right = mid
        # left now points to the minimum element
        return nums[left]

    findMin = find_min
