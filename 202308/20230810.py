# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/


class Solution:
    """81. Search in Rotated Sorted Array II

    There is an integer array `nums` sorted in non-decreasing order (not necessarily
    with **distinct** values).

    Before being passed to your function, `nums` is **rotated** at an unknown pivot
    index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k],
    nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For
    example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become
    `[4,5,6,6,7,0,1,2,4,4]`.

    Given the array `nums` **after** the rotation and an integer `target`, return `true`
    *if* `target` *is in* `nums`*, or* `false` *if it is not in* `nums`*.*

    You must decrease the overall operation steps as much as possible.

    """

    def search(self, nums: List[int], target: int) -> bool:
        # Initialize low and high pointers
        low, high = 0, len(nums) - 1

        # Perform binary search
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return True

            # Handle the case where nums[low] is equal to nums[mid]
            if nums[low] == nums[mid]:
                low += 1
                continue

            # If the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if the target is in the left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # If the right half is sorted
            else:
                # Check if the target is in the right half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # If the target is not found
        return False

    search = search
