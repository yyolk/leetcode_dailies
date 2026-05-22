# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    """33. Search in Rotated Sorted Array
    
    There is an integer array nums sorted in ascending order (with distinct
    values). Prior to being passed to your function, nums is possibly left
    rotated at an unknown index k (1 <= k < nums.length) such that the
    resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1],
    ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left
    rotated by 3 indices and become [4,5,6,7,0,1,2].
    
    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity.
    """
    def search(self, nums: list[int], target: int) -> int:
        # binary search bounds (O(1) space, O(log n) time)
        left = 0
        right = len(nums) - 1
        while left <= right:
            # midpoint to halve search space
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # determine which half is sorted (nums[left] <= nums[mid])
            if nums[left] <= nums[mid]:
                # left half sorted
                # target in sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right half sorted
                # target in sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # target not found
        return -1

    search = search