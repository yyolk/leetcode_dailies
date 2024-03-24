# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    """287. Find the Duplicate Number

    Given an array of integers `nums` containing `n + 1` integers where each integer is
    in the range `[1, n]` inclusive.

    There is only **one repeated number** in `nums`, return *this repeated number*.

    You must solve the problem **without** modifying the array `nums` and uses only
    constant extra space.

    """

    def find_duplicate(self, nums: list[int]) -> int:
        # Phase 1: Detect the intersection point of the two pointers
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Find the entrance to the cycle
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1

    findDuplicate = find_duplicate