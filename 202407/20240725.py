# https://leetcode.com/problems/sort-an-array/


class Solution:
    """912. Sort an Array

    Given an array of integers `nums`, sort the array in ascending order and return it.

    You must solve the problem **without using any built\\-in** functions in `O(nlog(n))`
    time complexity and with the smallest space complexity possible.

    """

    def sort_array(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2  # Finding the mid of the array
                left_half = arr[:mid]  # Dividing the elements into 2 halves
                right_half = arr[mid:]

                merge_sort(left_half)  # Sorting the first half
                merge_sort(right_half)  # Sorting the second half

                i = j = k = 0

                # Copy data to temp arrays left_half[] and right_half[]
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(nums)
        return nums

    sortArray = sort_array
